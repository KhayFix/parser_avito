import csv
import logging

import requests

HEADERS_CSV = (
    'Телефон',
    'Цена',
    'Название товара',
    'Фото',
    'Метро',
    'Ссылка',
)

headers_csv = HEADERS_CSV


def get_html(url: str, product_name=None, max_price=None, min_price=None, page=None):
    """
    Функция создает подключение к серверу по полученному url и параметрам переданными в params,
    и возвращает responce.text.

    : param url: Ссылка для подключения к указанному ресурсу.
    : param product_name: Название товара(марка) которое будет парситися.
    : param max_price: Максимальная цена, которая будет отображенна в поиске.
    : param min_price: Минимальная цена, если указана max_price и min_price, то поиск производится в этом диапазоне цен.
    : param page: Номер страницы, на которую будет произведет переход.

    timeout=5 сек, при следующих подключениях, если идет парсинг более 1-ой страницы.
    В случает ошибки сервера возвращает False и пишет в логи.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/40.0.2214.38 Safari/537.36',
        'Accept-Language': 'ru',
    }
    params = {
        'pmax': max_price,
        'pmin': min_price,
        'q': product_name,
        'p': page,
    }

    try:
        with requests.Session() as session:
            responce = session.get(url, params=params, headers=headers, timeout=5)
        if responce.url == 'https://www.avito.ru/blocked':
            logging.info('IP temporarily blocked')

        responce.raise_for_status()
        logging.info(f'response from server : {responce} {responce.url}')
        return responce.text
    except (requests.RequestException, requests.exceptions.HTTPError, ValueError) as errors:
        logging.error(f'Network error: ERROR - {errors}')
        return False


def writing_in_csv(parser_page_data):
    """
    Функция принимает следующие данные:
    [[{'Название товара': 'ZTE ', 'Фото': 'https://', 'Ссылка': 'https://', ...},...],
    ...[{'Название товара': 'ZTE ', 'Фото': 'https://', 'Ссылка': 'https://', ...}]].
    Полученный данные записываются в файл csv.
    """
    with open('parser_avito.csv', 'w', newline='', encoding='utf-8') as data_parser:
        writer = csv.DictWriter(data_parser, headers_csv, delimiter=',')
        writer.writeheader()
        [writer.writerow(data) for datas_page in parser_page_data for data in datas_page]


if __name__ == "__main__":
    headers_csv = HEADERS_CSV
