import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

payloads = {'page': 1}
url = 'https://9animetv.to/filter?keyword=&type=&status=all&genre=&season=&language=&year=&sort=all&'
file = open('anime.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['სათაური', 'ეპიზოდები'])

while payloads['page'] <= 5:
    response = requests.get(url, params=payloads)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    animes_soup = soup.find('div', class_='block_area-content block_area-list film_list film_list-grid')
    animes = animes_soup.find_all('div', class_='flw-item item-qtip')
    for anime in animes:
        title = anime.h3.a.text
        episode = anime.find('div', class_='tick-item tick-eps')
        episodes = episode.text.strip()
        print(title, episodes)
        csv_obj.writerow([title, episodes])
    payloads['page'] += 1
    sleep(randint(15, 20))

file.close()