
import requests
from bs4 import BeautifulSoup
from urllib import parse


def get_car_info_cpo(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    card_list = soup.select('.card-list a')
    card = soup.select('.card-content')
    for index, i in enumerate(card):
        print('https://www.toyotacpo.com.tw' + card_list[0]['href'])
        print(i.select('.card-title > .car-name')[0].string)
        print(i.select('.card-title > .car-shop')[0].string)
        print(i.select('.car-info .info-item')[0].string)
        print(i.select('.car-info .info-item')[1].string)
        print(i.select('.items-end .car-price')[0].getText())
        print('--------------------------------')


def get_car_info(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    card = soup.select('div > div.product-small.box > div.box-text.box-text-products')
    len = int(card.__len__() / 2)
    for index, i in enumerate(card):
        if (index >= len):
            continue
        print(i.select('div.title-wrapper > p')[0].getText())
        print(i.select('div.title-wrapper > p > a')[0]['href'])
        print(i.select('div.price-wrapper > span > span > bdi')[0].getText())
        print(i.select('h4')[0].getText())
        print('--------------------------------')

if __name__ == "__main__":
    params = [
        ('Order', 'asc'),
        ('Sort', 'SellPrice'),
        ('Model', 'ALTIS'),
        ('Model', 'PRIUS'),
        ('Model', 'PRIUS C'),
        ('Year', '0,5'),
        ('Price', '0,500000'),
        ('Mileage', '0,60000')
    ]
    get_car_info_cpo('https://www.toyotacpo.com.tw/Home/List?' + parse.urlencode(params))

    params = {
        'pwb-brand': 'toyota',
        'rng_min_price': '168000',
        'rng_max_price': '500000',
        'pa_kilometers': '10000-30000km,30000-60000km'
    }
    get_car_info('https://sscars.com.tw/car/?' + parse.urlencode(params))