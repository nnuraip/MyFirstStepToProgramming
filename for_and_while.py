# for i in ['name', 2 , True]:
# for i in range(1,11):
#   print(i)
# for i in range (0, 9):
# names = ['Мадияр', 'Дарига', 'Шахусейн', 'Темирлан', 'Алтынбек', 'Илья', 'Нурай', 'Нургиса', 'Марсель']
# for i in names:
#     if i == 'Марсель':
#         continue
#     else:
#         print("Hello," ,i)

# text = "Привет, сегодня было жарко".split()
# for i in text:
#     if i =="было":
#         for j in i:
#             print(j)
#     else:
#         continue

# my_list = []
# for i in range (1,11):
#     name = input(f"Ведите фрукт {i}:  ")
#     my_list.append(name)
# print (my_list)


# data = {
#     "name" : "Madira",
#     "age" : "16",
#     "job" : "student"
# }
# for k, v in data.items():

#     print(v)

# names = ['Мадияр', 'Дарига', 'Шахусейн', 'Темирлан', 'Алтынбек', 'Илья', 'Нурай', 'Нургиса', 'Марсель']

# for i in names:
    
#     print(i)

# numb = 1,2,3,4,5
# sum = 0
# for i in numb:
#     sum=sum+i
# print(sum)

# for i in range (1,21):
#     if i%2 ==0:

#       print(i, "is even")

# names = ['Мадияр', 'Дарига', 'Шахусейн']
# for i in names:
    
#     print(i,len(i))

# lll = []
# for i in range (1,101):
#     if i%2 ==1:
#         lll.append(i)
# print(lll)

# words = []
# for i in range (1,101):
#     print(words)

# for i in a:
#         if len(i)>5:        
#          words.append("длинное")
# else: words.append("not длинное")
# print(words)
        
# for i in range (0,21,3):
#     print(i)


# for i in range (1,-11,-1):
#     print(i)


# text = "Hello"

# for i in text[::-1]:
#     print(i)


# text = "Hello"

# for i in range (1,11):
#     print(text)

# for i in range(1,10):
#     a=""
#     for j in range(1,10):
#         a+=f"{i}*{j} ={i*j}  \t"
#     print(a)
# p = []
# for i in range(1,11):
#     if i%2==0:
#      p.append(i*i)
         
# print(p)
    
# sum = 0
# for i in range(1,11):
#     sum+=i
# print(i)
# users = {}
# user_name  = input("log: ")
# passw=input("passw: ")
# passw2= input("verify passw: ")
# error_pass = ["1,2,3", "qwerty", "asd", " "]
# while passw != passw2 or passw in error_pass:
#     if passw in error_pass:
#      print("your password is too simple")
#     elif passw != passw2:
#         print("they are same")
#     passw=input("passw: ")
#     passw2= input("verify passw: ")
# else:
#     users.update({"login": user_name})
#     users.update({"password": passw})
#     print(users)


# Калькулятор
# while True:
#     operation = input("""
# 1.Сложение
# 2.Вычитание
# 3.Умножение
# 4.Деление
# >>>""")
#     a=int(input("Введите первое число: "))
#     b=int(input("Введите второе число: "))
#     if operation =="1":
#      print(f"{a}+{b}=",a+b)
#     elif operation =="2":
#      print(f"{a}-{b}=",a-b)
#     elif operation =="3":
#       print(f"{a}*{b}=",a*b)
#     elif operation =="4":
#      print(f"{a}/{b}=",a/b)
#     else:
#      print("Повторите попытку")

