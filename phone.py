import time
from selenium import webdriver
# from PIL import Image


class Bot(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.navigate()  # TODO поменять имя

    def take_screenshot(self):
        self.driver.save_screenshot("avito_s.png")

    # def crop(self, location, size):
    #     image = Image.open("avito_s.png")
    #     x = location['x']
    #     y = location['y']
    #     width = size['width']
    #     height = size['height']
    #
    #     image.crop((x, y, x + width, y + height)).save('phone.gif')

    def navigate(self):
        self.driver.get('https://www.avito.ru/ekaterinburg/telefony/zte_axon_7_mini_1498209454')
        button = self.driver.find_element_by_xpath(
            "//button[@class='button-button-2Fo5k button-size-l-3LVJf button-success-1Tf-u width-width-12-2VZLz']"
        )
        time.sleep(2)
        button.click()
        time.sleep(1)

        self.take_screenshot()
        # кропаем картинку с номером
        image = self.driver.find_element_by_xpath("//img[@class='button-content-phone_size_l-1O5VB']")
        location = image.location  # dict {'x': 1233, 'y': 12532}
        size = image.size  # dict {'width': 50, 'height': 50}
        print(location, size)
        # self.crop(location, size)


def main():
    b = Bot()


if __name__ == '__main__':
    main()