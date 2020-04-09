import base64
import logging
import time

from PIL import Image
from pytesseract import image_to_string, pytesseract
from selenium import webdriver, common
from selenium.webdriver.chrome.options import Options


class BotParsePhone(object):
    """
    Для парсера 100 и более номеров можно использовать без головые браузеры.
    Примерная скорость парсера таким метод составляет 12-20 сек на одни номер.
    """

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(options=self.chrome_options)
        # укажите ваш путь до tesseract
        self.tesseract = pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        self.image_src = None

    def phone_recognize(self):
        image = Image.open(f"./img/{self.image_src[5:15]}.png")

        return image_to_string(image)  # выводит номер телефона строкой

    def get_phone(self, url: str):
        """
        Функция ищет на странице объявления элемент 'Показать телефон' и кликает его, чтобы
        выполнились страшные скрипты и загрузилась картинка с номером телефона.
        """
        try:
            self.driver.get(url)
            time.sleep(3)
            button = self.driver.find_element_by_xpath(
                "//button[(@class='button-button-2Fo5k button-size-l-3LVJf button-success-1Tf-u width-width-12-2VZLz')]"
            )

            button.click()
            time.sleep(1)

            # сохранения изображения напрямую, без кропа. Получаем зашифрованное данные(фото)
            image = self.driver.find_element_by_xpath("//img[@class='button-content-phone_size_l-1O5VB']")
            self.image_src = image.get_attribute('src').split(',')[1]
            self.decode_bytes_img()
        except common.exceptions.NoSuchElementException as error:
            logging.error(f"NoSuchElementException: {error}")
            return False

    def decode_bytes_img(self):
        # Декодирование полученных данных и сохранение в формате .png
        img = base64.decodebytes(bytearray(self.image_src, 'utf-8'))
        with open(f"./img/{self.image_src[5:15]}.png", 'wb') as image_png:
            image_png.write(img)


if __name__ == '__main__':
    pass
