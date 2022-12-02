from bs4 import BeautifulSoup
import requests


def weather_tyumen():
    url = 'https://yandex.com.am/weather/?lat=57.15298462&lon=65.54122925'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    return (bs.find('h1', 'title title_level_1 header-title__title').text + '\n' +
            bs.find('span', 'temp__value temp__value_with-unit').text + '°C, ' +
            bs.find('div', 'link__condition day-anchor i-bem').text + '\nВетер: ' +
            bs.find('span', 'wind-speed').text + ' ' + bs.find('span', 'fact__unit').text + '\n' +
            bs.find('div', 'term term_orient_h fact__feels-like').text + '°C')

def weather_perm():
    url = 'https://yandex.com.am/weather/?lat=58.01045227&lon=56.2294426'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    return (bs.find('h1', 'title title_level_1 header-title__title').text + '\n' +
            bs.find('span', 'temp__value temp__value_with-unit').text + '°C, ' +
            bs.find('div', 'link__condition day-anchor i-bem').text + '\nВетер: ' +
            bs.find('span', 'wind-speed').text + ' ' + bs.find('span', 'fact__unit').text + '\n' +
            bs.find('div', 'term term_orient_h fact__feels-like').text + '°C')