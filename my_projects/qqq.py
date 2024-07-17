error_pass = ["1,2,3", "qwerty", "asd", " "]
kasp = {
    'nurai':{
        "name" : "nurai",
        "surname": "paten",
        "password":"111",
        "balance": 2000,
     },
    'dariga': {
        "name" : "dariga",
        "surname": "ddd",
        "password":"222",
        "balance": 1000,
     }
    }
AUTH = None
while True:
    table = input("""
    1.Авторизоваться
    2.Зарегестрироваться
    3.Посмотреть баланс
    4.Перевести средства
    5.Выйти              
    >>> """
    )

    if table=="1":
        if AUTH is None:
            username = input("Введите имя: ")
            password = input("Введите пароль: ")
            if username in kasp and kasp[username]["password"]==password:
                AUTH=username
                print("вы успешно авторизовались")
            else:
                print("неверный логин или пароль")
        else:
            print("вы уже авторизованы")


    elif table =="2":
        if AUTH is None:
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            username = input("Введите логин: ")
            password = input("Введите пароль: ")
            password_2 = input("Повторите пароль: ")

            while password != password_2 or password in error_pass:
                A1 = "Пароли не совпадают!"
                A2 = "У вас слишком простой пароль!"
                A3 = A1 + " - " + A2

                if password != password_2:
                    print(A1)
                elif password in error_pass:
                    print(A2)
                else:
                    print(A3)

                password = input("Введите пароль: ")
                password_2 = input("Повторите пароль: ")

            else:
                kasp[username] = {
                        "name": name,
                        "surname": surname,
                        "password": password,
                        "balance": 0                    }
                AUTH = username
                print("Вы успешно зарегистрировались!")


    elif table =="3":
            if AUTH is None:
                   print("Вы не авторизованы")
            else:
                    print("Ваш баланс: ", kasp[username]["balance"], " kzt")


    elif table =="4":
        if AUTH is None:
            print("Вы не авторизованы")
        else:    
            transfer_funds_to = input("Введите имя получателя: ")
            if transfer_funds_to in kasp:
                        the_amount_of_transfer_fund = int(input("Сумма перевода:  "))
                        kasp[f"{transfer_funds_to}"]["balance"]+=the_amount_of_transfer_fund
                        kasp[username]["balance"]=kasp[username]["balance"]-the_amount_of_transfer_fund
                        print(f"Вы успешно перевели {the_amount_of_transfer_fund} тенге пользователю {transfer_funds_to}")
            else:
                        print("Такого пользователя нет")



    elif table =="5":
        if AUTH is None:
            print("Вы не авторизованы")
     
        else:
            AUTH = None
            print("вы вышли из аккаунта")
    
    else: 
              print("Ошибка")

