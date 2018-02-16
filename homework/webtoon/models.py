from django.db import models
import re, os, errno
import requests
from bs4 import BeautifulSoup

PATH_MODULE = os.path.abspath(__name__)  # __name__ 모듈이라는 파일이 있는 위치를 뽑아내기위한 abspath
ROOT_DIR = os.path.dirname(PATH_MODULE)
PATH_DATA_DIR = os.path.join(ROOT_DIR, 'data')
os.makedirs(PATH_DATA_DIR, exist_ok=True)


class Webtoon(models.Model):
    webtoon_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    week_webtoon = models.CharField(max_length=100, blank=True)
    img_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{title} : {id}'.format(
            title=self.title,
            id=self.webtoon_id,
        )

    def get_webtoon_detail(self, refresh_html=False):

        url = f'http://comic.naver.com/webtoon/list.nhn'
        # url = f'http://comic.naver.com/webtoon/list.nhn?titleId={webtoon_id}&weekday={week_webtoon}'
        # 밑의 params를 이용해서 딕셔너리로 만들면 위의 ?이후에 ()=() 부분을 자동으로 채워준다.
        params = {
            'titleId': self.webtoon_id,
        }

        # soup = BeautifulSoup(response.text, 'lxml')

        file_path = os.path.join(PATH_DATA_DIR, f'naver_webtoon_detail{self.webtoon_id}.html')
        try:
            file_mode = 'wt' if refresh_html else 'xt'
            with open(file_path, file_mode) as f:
                response = requests.get(url, params)
                source = response.text
                f.write(source)
        except FileExistsError as e:
            print(f'"{file_path}" file is already exists!')

        source = open(file_path, 'rt', encoding='utf8').read()
        soup = BeautifulSoup(source, 'lxml')
        tbody = soup.find('div', class_='webtoon').find('table')

        result = []
        for tr in tbody.find_all('tr', attrs={'class': None})[1:]:
            episode_url = tr.find('a').get('href')
            match_id = re.search(r'.*?no=(\d+).*?', episode_url)

            episode_id = match_id.group(1)
            episode_title = tr.find('td', class_='title').find('a').text
            episode_img_url = tr.find('img').get('src')
            episode_date = tr.find('td', class_='num').text

            result.append([
                episode_id,
                episode_title,
                episode_img_url,
                episode_date,
            ])

        for lists in result:
            Episode(
                webtoon=self,
                episode_id=lists[0],
                episode_title=lists[1],
                episode_img_url=lists[2],
                episode_date=lists[3]
                ).save()


            # self.episode_id= episode_id
            # self.episode_title = episode_title
            # self.episode_img_url = episode_img_url
            # self.episode_date = episode_date
            # self.save()
            # result.append({
            #     'Episode_id': episode_id,
            #     'Episode_title': episode_title,
            #     'Episode_img_url': episode_img_url,
            #     'Episode_date': episode_date,
            # })




class Episode(models.Model):
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    episode_id = models.CharField(max_length=100)
    episode_title = models.CharField(max_length=100)
    episode_img_url = models.CharField(max_length=100, blank=True)
    episode_date = models.CharField(max_length=100, blank=True)

    # def __init__(self, episode_id, episode_img_url, episode_title, episode_date):
    #     self.episode_id = episode_id
    #     self.episode_img_url = episode_img_url
    #     self.episode_title = episode_title
    #     self.episode_date = episode_date

    def __str__(self):
        return '{webtoon_title} - {title}, {id}'.format(
            webtoon_title=self.webtoon.title,
            title=self.episode_title,
            id=self.episode_id,
        )
