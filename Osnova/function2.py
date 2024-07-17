# from os import system
# system('clear')

# def funct(num, num2=10):
#     return num+num2
# print(funct(5))

# def h(a, *args):
#     return args
# print(h("marselle", "ilya", "dariga", True, 5.3))

# a=[1,2,3,4]
# b=[5,*a, 6,7]
# c=[9,6,3]
# print (b)
# a.extend(c)
# print(a)

# def user_info(**kwarks):
#     return kwarks
# print(user_info(name ='nurai', age = 16))

# def o(a,s=10, *args, **kwarks):
#     return kwarks
# print(o(5,20, "nurai","aaaaa",25, 5.2, name ='nurai', age = 16))

# r={'name':'nurai', 'age': 16}
# def f2(name, age):
#     return f'name is {name}, age is {age}'
# print(f2(**r))

# def sum_int(*args):
#     s=0
#     for i in args:
#     #  if type(i)==int:
#     #     s+=i
#     #  else:
#     #     continue
#         if isinstance(i,int):
#             s+=i
#     return s
# print(sum_int(1,2,3,4,5,6,"5"))

# def complex_calc(a,b, *args): #принимает обязательные параметры(а,б) и случайный параметр аргс
#     if isinstance(a,int) and isinstance(b,int): #проверяет, являются ли обязательные параметры интаджерами
#         result= a+b #сложение а и б, резултат которого сохраняется в переменной резалт
#         for num in args: #проходится по случайному параметру(аргс)
#             if not isinstance(num,int): #если значение аргс не интаджер
#                 continue #то пропускает
#             else:#иначе
#                 result*=num #сложение а и б умножает на значения аргс и сохраняет в переменной резалт
#     else:#если а или б не является интаджером
#         return "they are not int" #то вернет 
#     return result #возвращает резалт
# print(complex_calc(5,7,2,5)) #дает значения а,б,аргс и печатает результат функции

# n= lambda a,b=10: a+b
# n1= lambda a,b=10: a-b
# n2= lambda a,b=10: a*b
# n3= lambda a,b=10: a/b
# print(n(2))
# print(n1(2))
# print(n2(2))
# print(n3(2))


#Встроенные функции 
# a=[1,5,2,3,4]
# print(len(a))
# print(sum(a)) 
# print(sorted(a))
# print(sorted(a,reverse=True))

# my_list = [-9,1,2,True,"ee"]
# print(any(my_list)) #если один элемент тру, то возвращает тру
# print(all(my_list)) #если все элементы тру, то возврщает тру

# def person_info(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
# person_info(name = "nurai", age = 16, city = "Almaty")

# def average_age(**kwargs):
#     avg=0
#     students = 0
#     for k,v in kwargs.items():
#         students = students+1
#         avg = avg + v
#     return avg/students
# print(average_age(nurai =16, 
#                   marselle=21, 
#                   zhansultan= 16, 
#                   dariga= 19,
#                   magamed = 24, 
#                   nurgisa = 24, 
#                   altynbek = 17, 
#                   ilia = 48, 
#                   madiar = 29, 
#                   temirlan = 14,
#                   shahhusein = 21))

# def average_age(**kwargs):
#     return kwargs.keys()
# print(average_age(nurai =16, 
#                   marselle=21, 
#                   zhansultan= 16, 
#                   dariga= 19,
#                   magamed = 24, 
#                   nurgisa = 24, 
#                   altynbek = 17, 
#                   ilia = 48, 
#                   madiar = 29, 
#                   temirlan = 14,
#                   shahhusein = 21))

# names =['nurai', 'marselle', 'zhansultan', 'dariga', 'magamed', 'nurgisa', 'altynbek', 'ilia', 'madiar', 'temirlan', 'shahhusein']
# def d(*args):
#     a=''
#     for i in args:
#         a=a+i

#     return a
# print(d(names))