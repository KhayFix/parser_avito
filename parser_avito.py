import logging
import os
from datetime import datetime

from bs4 import BeautifulSoup

from utils import get_html, writing_in_csv
from find_html_tags import get_metro, get_photo, get_price, get_url, get_title
from find_phone import BotParsePhone

logging.basicConfig(
    filename=f"{os.getcwd()}/logs/{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.log",
    level=logging.DEBUG,
    filemode='w',
    format='%(levelname)s %(asctime)s : %(message)s',
)

BASE_URL_AVITO = 'https://www.avito.ru'
base_url_avito = BASE_URL_AVITO
parse_phone = BotParsePhone()


def parser_page_avito(soup):  # -> list()
    list_data_parser = []

    soup = soup
    try:
        all_ads_page = soup.findAll('div', class_='item__line')
    except AttributeError as error:
        logging.error(f"AttributeError: {error}")
    else:
        logging.info(f"{20 * '*'} Processing page a parser{20 * '*'}")

        for page_elements in all_ads_page:
            title = get_title(page_elements)
            url = get_url(page_elements)
            price = get_price(page_elements)
            photo = get_photo(page_elements)
            metro = get_metro(page_elements)

            dict_of_received_data = save_data_parser(
                title=title,
                photo=photo,
                url=url,
                price=price,
                metro=metro,
            )
            list_data_parser.append(dict_of_received_data)

        logging.info(f'Part of the received data: {list_data_parser[-1]}')
        logging.info(f"All received amount product on page: {len(list_data_parser)}")

    return list_data_parser


def beautiful_soup_avito(html):
    html = html
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    else:
        return None


def save_data_parser(title: str, photo: str, url: str, price: str, metro: str, phone=None):  # -> dict()
    """ Промежуточное сохранение в dict """

    dict_of_received_data = {
        'Телефон': phone,
        'Название товара': title,
        'Фото': photo,
        'Ссылка': f"{base_url_avito}{url}",
        'Цена': price.replace('\n', '').replace('₽', 'Руб.'),
        'Метро': metro.replace('\t', ''),
    }
    return dict_of_received_data


def page_product(link: str, product_name, max_price=None, min_price=None):  # -> int
    """
    Получаем колличество страниц с сайта.
    :return: int(page)
    Колличество объявлений по ссылке передаются в логи.
    В случает AttributeError делается запись в логи.
    :return: 1
    """
    split_link = link.split("/")

    html = get_html(url=link, product_name=product_name, max_price=max_price, min_price=min_price)
    soup = beautiful_soup_avito(html)
    try:
        all_amount_ads_on_pages = soup.find('span', class_='page-title-count-1oJOc').text
        pages = soup.find_all('span', class_='pagination-item-1WyVp')
        page = pages[-2].text
    except AttributeError as error:
        logging.error(f"AttributeError: {error}")
        return 1
    else:
        logging.info(f"Ads on request '{product_name}' in {split_link[3].title()} - {all_amount_ads_on_pages}")
        logging.info(f'All pages: {page}')
        return int(page)


def run(link: str, product_name: str, pages_all=False, get_phone=False, max_price=None, min_price=None, ):
    """
    Для работы парcера обязательно укажите ссылку и название продукта:
    link = 'https://www.avito.ru/ekaterinburg/telefony?' or
    'https://www.avito.ru/ekaterinburg/tovary_dlya_kompyutera/komplektuyuschie'
    product_name='xiaomi' or product_name='gtx+1060' .
    Для поиск в конкретном диапозоне цен нужно их указать, по умолчанию стоит None.
    max_price=10000,
    min_price=1000,

    По умолчанию парсинг первой страницы т.к. pages_all=False.
    Для поиска по всем страницам page_all нужно первести в стостояние True,
    или указать до какой страницы произвести парсинг page_all=2.

    Для получения телефонных номером find_phone перевести в стостояние True,
    но вы должны знать,что скорость получения одного номера составляет 12-20 сек.
    """
    all_data = []
    if pages_all is True:
        page = page_product(link=link, product_name=product_name, max_price=max_price, min_price=min_price)
    else:
        page = 1

    for number_page in range(1, page + 1):
        html = get_html(
            url=link,
            page=number_page,
            product_name=product_name,
            max_price=max_price,
            min_price=min_price,
        )
        soup = beautiful_soup_avito(html)
        datas = parser_page_avito(soup)
        # при find_phone = True, запускается BotParsePhone для получения телефонного номера
        if get_phone:
            for key in datas:
                phone_image = parse_phone.get_phone(url=key['Ссылка'])
                if phone_image is not False:
                    phone_str = parse_phone.phone_recognize()
                    key['Телефон'] = phone_str

        all_data.append(datas)

    writing_in_csv(all_data)


if __name__ == "__main__":
    pass
