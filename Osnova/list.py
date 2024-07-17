# text = "Мир API широк и разнообразен. Этот курс посвящен API REST, но существует также много других типов API. Бывает, люди начинают просматривать GitHub в поисках проектов API, или когда просматривают различные API в своей собственной компании, они удивляются, что API выглядят незнакомыми по сравнению с API, описанным в этом курсе. Да, есть много типов API, с которыми мы можем встретиться."

# text2 = "привет, как у тебя дела?"
# # print(text2[3:10:2])
# # print(len(text2))
# print(text2.split())
# # print("]".join(text2))
  
# my_list = [ "привет, как у тебя дела?5",5, 30,25]
# print(my_list)
# print(my_list.count(5))
# print(my_list.index(25))
# print(my_list[1])
# print(my_list[0][1])
# my_list.append("fffaaa")
# print(my_list)
# deleted_obj = my_list.pop(2)
# print(deleted_obj)
# my_list.remove("привет, как у тебя дела?5")
# print(my_list)

# names = []
# sec_list = [1,2,3]
# names.append("Nurai")
# names.append("Altynbek")
# names.append("Nurai")
# names.append("nurgisa")
# names.append("dariga")
# names.append("Shah")
# names.append("Marselle")
# names.append("Temirlan")
# names.extend(sec_list)
# names.insert(1, "python")
# names.clear()
# print(names)



# my_list = [
#     "Привет", [ [[[1,[[[[['win',['ik',['prince', True, ["winner"]]]],'world']]],3]]]]]
# ]
# t1 = my_list[0] #привет
# t2 = my_list[1][0][0][0][0] #1

# t3 = my_list[1][0][0][0][1][1] #3
# t4 = my_list[1][0][0][0][1][0][0][0][1] #world
# t5 = my_list[1][0][0][0][1][0][0][0][0][0] # win
# t6 = my_list[1][0][0][0][1][0][0][0][0][1][0] #ik
# t7 = my_list[1][0][0][0][1][0][0][0][0][1][1][0] #prince
# t8 = my_list[1][0][0][0][1][0][0][0][0][1][1][1] #True
# t9 = my_list[1][0][0][0][1][0][0][0][0][1][1][2][0] #winner
# print(t1, t2, t3, t4, t5, t6, t7, t8, t9)

# my_list = ["rgf", 123, 1.2 , True , 5 ,5,5,5]
# my_tuple = (
#    1, 2, 3
#  )
# my_dict =  {
#      "nurai": "nur",
#      "madiyar": "mad"
#  }

my_list1 = ['nurai', True, False,1,2,3,4,5,{'name':'ooo'}, {1,32}]
# print(isinstance(my_list1,list))

# my_list1.insert(3,'iiiii')
# print(my_list1)
# my_list1.remove(False)
# last_element = my_list1.pop()
# print(last_element)
# print(my_list1)
# my_list1.clear()
# print(my_list1.count(5))
# i = [1,5,6,8,2]
# i.sort()#reverse=True
# print(i)  




# # isinstance(my_list, list)

# my_list = [1, 2, 3, 4, 5]
# my_list_2 = [7, 8]
# # my_list1 = list('maslkdm')

# # Добавление элемента в конец списка
# my_list.append(6)
# print(my_list)  # [1, 2, 3, 4, 5, 6]

# # Расширение списка
# my_list.extend(my_list_2)
# print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8]

# # Вставка элемента на позицию
# my_list.insert(6, "Что добавить")
# print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# # Удаление элемента
# my_list.remove('Что добавить')
# print(my_list)  # [0, 1, 2, 4, 5, 6, 7, 8]

# # Удаление и возврат элемента по индексу
# last_element = my_list.pop(7)
# print(last_element)  # 8
# print(my_list)       # [0, 1, 2, 4, 5, 6, 7]

# # Очистка списка
# my_list.clear()
# print(my_list)  # []

# my_list = [1, 3, 2, 4, 5]

# # Поиск индекса элемента
# index_of_three = my_list.index(3)
# print(index_of_three)  # 2

# # Подсчет вхождений элемента
# count_of_twos = my_list.count(2)
# print(count_of_twos)  # 1

# # Сортировка списка
# my_list.sort()
# print(my_list)  # [1, 2, 3, 4, 5]

# # Сортировка в обратном порядке
# my_list.sort(reverse=True)
# print(my_list)  # [5, 4, 3, 2, 1]

# test_list = [1, 'sksk', 3, 4, "sk", 10]

# # Разворот списка
# test_list.reverse()
# print(test_list)  # [1, 2, 3, 4, 5]

# # Копирование списка
# my_list_copy = test_list.copy()
# print(my_list_copy)  # [1, 2, 3, 4, 5]


# # a = [1, 2, 3, 4, 5]

# # b = a.copy()  # Создание копии списка
# # b.append(6)

# # print(a)
# # print(b)

# a= input("введите строку:  ")
# b = input("подстрока:  ")
# index = a.find(b)
# if index == -1:
#     print("строка не содержит подстроку")
# else:
#     print("строка содержит подстроку")