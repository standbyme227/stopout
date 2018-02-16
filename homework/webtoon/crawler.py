import re

import os, errno
import requests
from bs4 import BeautifulSoup
from pathlib import Path


PATH_MODULE = os.path.abspath(__name__)  # __name__ 모듈이라는 파일이 있는 위치를 뽑아내기위한 abspath
ROOT_DIR = os.path.dirname(PATH_MODULE)
PATH_DATA_DIR = os.path.join(ROOT_DIR, 'data')
os.makedirs(PATH_DATA_DIR, exist_ok=True)


def search_webtoon(title, refresh_html=False):
    url = f'http://comic.naver.com/search.nhn'
    params = {
        'keyword': title,
    }
    # response = requests.get(url, params)
    # soup = BeautifulSoup(response.text, 'lxml')

    file_path = os.path.join(PATH_DATA_DIR, f'{title}.html')
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
    result_list = soup.find('div', id='content').find('div', class_='resultBox').find('ul', class_='resultList')

    result = []
    for h5 in result_list.find_all('h5'):
        title = h5.find('a').text
        webtoon_url = h5.find('a').get('href')
        match_id = re.search(r'.*?(\d+).*?', webtoon_url)
        webtoon_id = match_id.group(1)
        result.append({
            'Title': title,
            'Webtoon_id': webtoon_id,
        })
    return result



        # episode_url = tr.find('a').get('href')
        # match_id = re.search(r'.*?no=(\d+).*?', episode_url)
        #
        # episode_id = match_id.group(1)






class EpisodeData:

    def __init__(self, episode_id, episode_img_url, episode_title, episode_date):
        self.episode_id = episode_id
        self.episode_img_url = episode_img_url
        self.episode_title = episode_title
        self.episode_date = episode_date

    def __str__(self):
        return f'{self.webtoon_title} {self.webtoon_date}'



def get_webtoon_detail(webtoon_id, refresh_html=False):

    url = f'http://comic.naver.com/webtoon/list.nhn'
    # url = f'http://comic.naver.com/webtoon/list.nhn?titleId={webtoon_id}&weekday={week_webtoon}'
    # 밑의 params를 이용해서 딕셔너리로 만들면 위의 ?이후에 ()=() 부분을 자동으로 채워준다.
    params = {
        'titleId': webtoon_id,
    }

    # soup = BeautifulSoup(response.text, 'lxml')

    file_path = os.path.join(PATH_DATA_DIR, f'naver_webtoon_detail_{webtoon_id}.html')
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

        result.append({
            'Episode_id':episode_id,
            'Episode_title':episode_title,
            'Episode_img_url':episode_img_url,
            'Episode_date':episode_date,
        })
    return result


if __name__ == '__main__':
    pass