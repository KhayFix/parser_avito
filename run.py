from parser_avito import run

"""
Для работы парcера обязательно укажите ссылку и название продукта:
link = 'https://www.avito.ru/ekaterinburg/telefony?' or
'https://www.avito.ru/ekaterinburg/tovary_dlya_kompyutera/komplektuyuschie'
product_name='xiaomi' or product_name='gtx+1060'.
По умолчанию парсятся все страницы, если нужно указать до какой парсить введите 
run(link, product_name='xiaomi', pages=3).
Для поиск в конкретном диапозоне цен нужно их указать, по умолчанию стоит None.
max_price=10000,
min_price=1000,
"""

if __name__ == "__main__":
    product_name = 'zte'
    max_price = None
    min_price = None
    link = 'https://www.avito.ru/ekaterinburg/telefony?'
    run(link, product_name=product_name, max_price=max_price, min_price=min_price, pages=2)
