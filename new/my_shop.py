
tovar = {
    '1' : 50000,
    '2' : 25000,
    '3' : 89000,
    '4' : 500
}
my_list=[]
def korzina_sum(user_tovar, kol, tovar):
    price = tovar.get(user_tovar)
    if price is None:
        return 'Нет такого товара'
    
    return price * kol


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
    receipt = {
    1: "Утюг - 50.000kzt",
    2: "Плойка - 25.000kzt",
    3: "Стиральная машина - 89.000kzt",
    4: "Расческа - 500kzt"
    }
    if user_tovar in tovar:
        try:
            kol = int(input('укажите количество товара: '))
        except:
            kol = int(input('укажите правильное кол-во: '))
        else:
            my_list.append(f"{receipt[int(user_tovar)]}*{kol}={korzina_sum(user_tovar, kol, tovar)} ")
    elif user_tovar=="5":
        print(my_list)
    else:
       print("такого товара нет")
       break


