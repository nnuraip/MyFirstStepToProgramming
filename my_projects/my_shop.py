
tovar = {
    '1' : 50000,
    '2' : 25000,
    '3' : 89000,
    '4' : 500
}
my_list=[]
def korzina_sum(user_tovar, kol, tovar):
    price = tovar.get(user_tovar)
    return price * kol


option = input('''
    нажмите на enter чтобы перейти к покупкам''')
file = open("receipt.txt","w")
while True:

    user_tovar = input("""выберите товар:
    1) Утюг - 50.000kzt
    2) Плойка - 25.000kzt
    3) Стиральная машина - 89.000kzt
    4) Расческа - 500kzt
    5) Перейти к оплате

""")
    receipt = {
    1: "Утюг               50.000kzt ",
    2: "Плойка             25.000kzt ",
    3: "Стиральная машина  89.000kzt ",
    4: "Расческа           500kzt    "
    }
    if user_tovar in tovar:
        try:
            kol = int(input('укажите количество товара: '))
        except:
            kol = int(input('укажите правильное кол-во: '))
        else:
            price1 = korzina_sum(user_tovar, kol, tovar)
            my_list.append(price1)
            file = open("receipt.txt","a")
            file.write(f"{receipt[int(user_tovar)]}*{kol} = {price1} \n")

    elif user_tovar=="5":
        total_sum = 0
        for i in my_list:
            total_sum+=i
        file.write(f"                          Итого:  {total_sum}kzt")
        break
    else:
       print("такого товара нет")
