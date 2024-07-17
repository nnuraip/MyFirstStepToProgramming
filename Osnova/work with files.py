# from os import system
# system('clear')
# Работа с файлами в Python включает в себя открытие, чтение, 
# запись и закрытие файлов. Вы можете использовать функцию open() 
# для открытия файла, указать режим (чтение, запись, добавление) 
# и затем использовать методы, такие как read(), write(), 
# и другие для взаимодействия с содержимым файла. 
# Не забывайте закрывать файл с помощью close(), чтобы освободить ресурсы.

# file = open(filename,mode)
# file = open("example.txt", "w")
# file.write("Hello, how r u?")
# file = open("example.txt", "a")
# file.write("i am fine")

# from datetime import datetime as dt
# import random
# my_list = ["Орел","Решка"]
# file = open("orel_ili_reshka.txt","w")
# while True:
#     game_time = dt.now().strftime("%H:%M:%S    %D") 
#     file = open("orel_ili_reshka.txt","a") 
#     a = input("Орел или Решка:  ").capitalize()
#     file.write(game_time)
#     file.write(f"    Ответ игрока: {a}")       
#     if a=="Орел":
#          file.write(" ")
#     if a not in my_list:
#         print("Проверьте свой ответ!")
#         file.write("  -Орфографическая ошибка\n")
#     else:
#         comp = random.choice(my_list)
#         print("Правильный ответ:  ", comp)        
#         file.write(f"  Выпало: {comp}")
#         if comp =="Орел":  
#              file.write(" ")   
 
#         if a==comp:
#             print("Вы выиграли!!")
#             file.write("  Результат: Выигрыш\n")
#         else:
#             print("Вы проиграли!!")        
#             file.write("  Результат: Проигрыш\n") 

  


    