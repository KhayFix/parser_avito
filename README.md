Парсер avito
--
Парсер написан в ознакомительных целях. Код не идеальный, да и сама реализация тоже.

Установка
---
Создайте виртуальное окружение и активируйте его. Потом в виртуальном кружении выполните:
   
    pip install -r requirements.txt
    
Если вы захотите получить телефонный номер с сайта,
то вам потребуется установка "Tesseract-OCR".
Если он вам не нужен, то все что написанно ниже, а также "Tesseract-OCR", вам не потребуется.    
  
Что это такое можно прочитать тут: 
* https://github.com/tesseract-ocr/tesseract/wiki 

Для работы с браузером через selenium потребуется установка драйвера:

У Firefox это geckodriver:
* https://github.com/mozilla/geckodriver/releases/

У Chrome это chromedriver:
* https://chromedriver.chromium.org/downloads