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


a = { 8,3, 1,2,"atr"}
b = {4,5,6,7,'a',3}
# print(
#     a.isdisjoint(b)
# )
print(a.union(b), a|b)
# print(
#     a.intersection(b), a&b
# )
# print(a.difference(b), a-b)
# print(b.difference(a))
# print(a.symmetric_difference(b))


# my_set2= { 5 }
# my_set2.add("hello")
# my_set2.add("dfgvjn")


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