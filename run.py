from parser_avito import run

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

if __name__ == "__main__":
    link = 'https://www.avito.ru/ekaterinburg/telefony'
    product_name = 'zte'
    page_all = False
    get_phone = False
    max_price = None
    min_price = None

    run(
        link,
        product_name=product_name,
        get_phone=get_phone,
        pages_all=page_all,
        max_price=max_price,
        min_price=min_price
    )
