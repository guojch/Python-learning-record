#!/usr/bin/python3

"""
爬取豆瓣电影TOP250
"""

import requests
from bs4 import BeautifulSoup
import pymysql
import time

DOWNLOAD_URL = 'https://movie.douban.com/top250'
MYSQL_HOST = ''
MYSQL_USERNAME = ''
MYSQL_PASSWORD = ''


def get_content(url):
    # 使用requests获取网页
    return requests.get(url, headers={
        # 使用U-A伪装成浏览器发送请求
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }).text


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    # 电影列表
    movie_li_list = soup.find('ol', attrs={'class': 'grid_view'}).find_all('li')
    for movie in movie_li_list:
        movie_rank = movie.find('em', attrs={'class': ''}).get_text()  # 电影排名
        movie_name = movie.find('span', attrs={'class': 'title'}).get_text().replace('\'', '').replace('"', '')  # 电影名字
        movie_info = movie.find('div', attrs={'class': 'bd'}).find('p').get_text().strip().replace('\'', '').replace(
            '"', '')  # 电影信息
        movie_star = movie.find('span', attrs={'class': 'rating_num'}).get_text()  # 电影评分

        # 创建数据连接
        conn = pymysql.connect(MYSQL_HOST, MYSQL_USERNAME, MYSQL_PASSWORD, 'python',
                               cursorclass=pymysql.cursors.DictCursor)
        # 创建一个游标对象 cursor
        cursor = conn.cursor()
        # 查询是否存着记录
        cursor.execute("SELECT * FROM douban_movie WHERE name = '%s'" % movie_name)
        result = cursor.fetchone()

        try:
            if result:
                cursor.execute("UPDATE douban_movie SET info='%s',star='%s',rank='%s' WHERE id=%s" % (
                    movie_info, movie_star, movie_rank, result['id']))
            else:
                cursor.execute("INSERT INTO douban_movie (name, info, star, rank) VALUES ('%s', '%s', '%s', '%s')" % (
                    movie_name, movie_info, movie_star, movie_rank))
            conn.commit()
        except:
            conn.rollback()
        finally:
            # 记录最后更新时间
            filename = 'last_update_time.txt'
            with open(filename, 'w') as file:
                file.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            conn.close()
    # 下一页链接
    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return DOWNLOAD_URL + next_page['href']
    else:
        return None


def main():
    url = DOWNLOAD_URL
    while True:
        html = get_content(url)
        url = parse_html(html)
        print(url)
        if url is None:
            break
    print('success')


if __name__ == '__main__':
    main()
