# import os
# os.system("mkdir a s d f")
# os.system("rm -rf a s d f")
# os.mkdir("hhh")
# os.remove("hhh")
# os.system("ls")

# for i in range(10):
#     # os.system(f"mkdir folder{i}")
#     os.system(f"rm -rf folder{i}")

# import four
# print(four.my_list)
# from f import qqq
# print(qqq.my_dict)


from datetime import datetime as dt
# #import datetime #date , #time

# date = datetime.now().date()
# time = datetime.now().time()
# print(date)
# print(time)

print(dt.now().strftime("%H:%M:%S    %D"))
# print(dt.now().strftime("%H:%M:%S    %d.%m.%Y"))
# import random, os
#  # from random import randint, choice, randrange, sample, shuffle, choices, random
    
# my_list = ['Мадияр', 'Дарига', 'Шахусейн', 
#             'Темирлан', 'Алтынбек', 'Илья', 
#             'Нурай', 'Нургиса', 'Марсель', 
#             'Магамед']
# while len(my_list)!=1:
#     os.system('clear')
#     user = random.choice(my_list)
#     my_list.remove(user)
#     print("Проиграл польз: ", user)
#     input("Enter to continue >>>")
# else:
#     print("Winner: ", my_list[0])


# import random
# a = [1,2,3,4,5,6,7,8,9]
# print(random.choices(a, k=3))
# print(random.sample(a, 3))  #не повторяет
# print(random.randint(0,10))
# print(random.randrange(90,100,2))
# random.shuffle(a)
# print(a)


# import random, os
# my_list = ["Орел","Решка"]
# while True:
#     a = input("Орел или Решка:  ").capitalize()
#     if a not in my_list:
#         print("Проверьте свой ответ!")
#     else:
#         comp = random.choice(my_list)
#         print("Правильный ответ:  ", comp)
#         if a==comp:
#             print("Вы выиграли!!")
#         else:
#             print("Вы проиграли!!") 

# import calendar
# cal = calendar.prcal(200)
# print(cal)

# weekday = calendar.weekday(2024,7,2)
# print(weekday)

# isleap = calendar.isleap(2024)
# print(isleap)

# import time

# seconds = time.time()
# print(seconds)
# local_time = time.ctime(seconds)
# print(local_time)

# print("Now")
# time.sleep(4)
# print("After 4 sec")

# Созданные модули
# Встроенные модули
# Скачанные модули которые называются библиотеками

# для того, чтобы скачать библиотеку надо использовать пакетный менеджер Пайтон под названием pip
# Пример:
# Linux: pip install "название библиотеки"
# Windows: pip3 install "название библиотеки"
