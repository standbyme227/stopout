import re
from bs4 import BeautifulSoup
from crawler import search_webtoon, get_webtoon_detail

# source = open('./data/naver_webtoon_list.html', 'rt', encoding='utf8').read()
# soup = BeautifulSoup(source, 'lxml')



if __name__ == '__main__':
    # result = get_week_list()
    # for item in result:
    #     print(f'{item["Weekday"]} - {item["Title"]}: {item["Id"]}')

    params = input('웹툰의 이름을 입력해주세요.')
    search = search_webtoon(params)

    for item in search:
        print(f'{item["Title"]} - {item["Webtoon_id"]}')

    # params = '신의 탑'
    # search = search_webtoon(params)


    params = input('웹툰의 아이디를 입력해주세요.')
    result_detail = get_webtoon_detail(params)

    for item in result_detail:
        print(f'{item["Episode_id"]} - {item["Episode_title"]} - {item["Episode_date"]}')


