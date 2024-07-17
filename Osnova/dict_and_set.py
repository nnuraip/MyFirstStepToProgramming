# u= [
#     1,2,3,"ojkn", 2.5, 4
# ]


# my_tuple = (
#     1, 2, 3
# )
# print(u)
# print(my_list[0:5:2])
# print(my_list)
# text = "   Hello  "
# print(text.strip())

# o = {
    # 1, 3, 2 , 8, 6, 3, 8, "fnjieu"
# }
# print(hash("fnjieu"))
# print(o)

# my_list = [
#     2, 5, 8, 4 , 8 , 5
# ]
# print(
#     list(set(my_list))
#       )


# a = { 8,3,4, 1,2,"atr"}
# b = {4,5,6,7,'a',3}
# print(1 in a)
# print(
#     a.isdisjoint(b)
# )
# print(a.union(b), a|b)
# print(
#     a.intersection(b), a&b
# )
# print(a.difference(b), a-b)
# print(b.difference(a))
# print(a.symmetric_difference(b), a^b)

# print(a.issubset({8,3,4, 1,2,"atr",8,6,9}))  #проверяет, являетсч ли текущее множество подмножеством другого
# print(a.issuperset({1,2,3}))  #проверяет, являетсч ли текущее множество надмножеством другого
# my_set2= { 5 }
# my_set2.add("hello")
# my_set2.add("dfgvjn")
# my_set2.discard(5) #если находит элемент, то удаляет его. а если нет, то ничего не делает
# print(my_set2)
# my_set2.remove("hello")
# a= my_set2.pop()
# print(f"I deleted {a}")
# my_set2.add(a)

# my_set2.clear()
# print(my_set2)

# users= {
#         "080401652844": {
#             "name": "Nurai",
#             "surname": "Paten",
#             "age": 16
#         },
#         "000000000000": {
#             "name": "Zhans",
#             "surname": "Aryn",
#             "age": 16
#         }
# } 
# print(users["000000000000"]['surname'])
# users.pop("000000000000")
# print(users)

# users.popitem()
# print(users)
# cars = {
#     'bmw': {
#         'volume': 3.0, 
#         'model': "BMW M F90",
#         'milleage': 90000
#     },
#     'mers': {
#         "volume": 4.4, 
#         "model": "E63 213",
#         'milleage': 95000
#     }
# }
# cars['mers']['milleage']+=1000
# print(cars['mers']['milleage'])

# print(cars.items())
# print(cars.keys())
# print(cars['bmw'].keys())
# print(cars['mers'].values())
# print(cars.get('mers', "there is no such key"))
# print(cars.get('bm', "there is no such key"))

# my_dict.update({"name": "nurai"})
# print(my_dict["name"])

# users_age = {
#     "nurai": 16,
#     "madiyar": 85
# }
# users_age.update({"altynbek":17})
# users_age["dariga"] = 20
# print(users_age)

# a = {
#     1: 784,
#     2: "hello str",
#     3: [1,2,3],
#     4: (1,2,3),
#     5: True,
#     6: None,
#     7: 5.5,
#     8: { 
#         "city": 'Almaty'
#         }
# }
# print(a[8]['city'])


# person  = {
#     "nurai":{
#         'bank':{
#             'balance': 1000,
#             'card_number': '4400 4200 1313 3333',
#             'recvisit': "789456123"  
#         },
#         'account':{
#             "instagram":{
#                 "login": "nnuraip",
#                 "password": "123123"
#             },
#             "telegram":{
#                 "login": "nnuraip",
#                 "numb": "8777 526 3129"
#             }
#         },
#         "info":{
#             'first_name': 'nurai',
#             'last_name':'paten',
#             'age': 16
#         },
#         'address':'PARIS'
        
        
# }}
# nurai_info = person['nurai']['info']     
# print("имя:     ", nurai_info['first_name'])
# print("фамилия: ", nurai_info['last_name'])
# print("возраст: ", nurai_info['age'])

# print(person['nurai']['bank'])
# person['nurai']['bank']['balance']+=1000
# print(person['nurai']['bank']['balance'])

# insta_login  = person['nurai']['account']["instagram"]["login"]
# insta_password  = person['nurai']['account']["instagram"]["password"]

# insta_login = 'qwerty'


# person['nurai'].update({"address": "USA"})

# person['nurai']["account"]['github'] = {"login": 'nnurai', 'password': 'asdf'}
# person['nurai']["info"] = {"email": 'nnurai@gmail.com'}
# print(person)
# print("---------------------------------")
# person['nurai'].pop("address")
# print(person)


