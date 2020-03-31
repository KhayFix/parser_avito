import logging


def get_metro(page_elements):
    """
    :param page_elements:
    :return: str('Динамо, 1,2 км'...)
    """
    try:
        metro = page_elements.find('span', class_='item-address-georeferences-item').text
    except AttributeError as error:
        logging.error(f"AttributeError: {error}")
        metro = 'None'
    return metro


def get_owners_name(page_elements):
    pass


def get_photo(page_elements):
    """
    :param page_elements:
    :return:
    """
    try:
        photo = page_elements.find('img', class_='large-picture-img')['src']
    except TypeError as error:
        logging.error(f'TypeError :{error}')
        photo = 'None'
    return photo


def get_price(page_elements):
    """
    :param page_elements:
    :return:
    """
    try:
        price = page_elements.find('span', class_='snippet-price').text
    except AttributeError as error:
        logging.error(f'AttributeError: {error}')
        price = 'None'
    return price


def get_phone(page_elements):
    pass


def get_title(page_elements):
    """
    :param page_elements:
    :return:
    """
    try:
        title = page_elements.find('a', class_='snippet-link').text
    except AttributeError as error:
        logging.error(f'AttributeError: {error}')
        title = 'None'
    return title


def get_url(page_elements):
    """
    :param page_elements:
    :return:
    """
    try:
        url = page_elements.find('a', class_='snippet-link')['href']
    except TypeError as error:
        logging.error(f'TypeError :{error}')
        url = 'None'
    return url
