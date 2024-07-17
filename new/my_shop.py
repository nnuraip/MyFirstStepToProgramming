
tovar = {
    '1' : 50000,
    '2' : 25000,
    '3' : 89000,
    '4' : 500
}

my_list = []


def korzina_sum(item_number, kol, prise_dict_tovar):
    prise = prise_dict_tovar.get(item_number)
    if prise is None:
        return 'Нет такого товара'
    
    return prise * kol


option = input('''
    нажмите на enter чтобы перейти к покупкам''')
while True:

    user_tovar = input("""выберите товар:
    1) Утюг - 50.000kzt
    2) Плойка - 25.000kzt
    3) Стиральная машина - 89.000kzt
    4) Расческа - 500kzt
    5) Перейти к оплате

""")
    if user_tovar in tovar:
        try:
            kol = int(input('укажите количество товара: '))
        except:
            kol = int(input('укажите правильное кол-во: '))
        else:
            print(korzina_sum(user_tovar, kol, tovar))
    
    else:
       print("такого товара нет")
       break


