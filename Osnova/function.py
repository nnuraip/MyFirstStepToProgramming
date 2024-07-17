# def приветствие():
#     print("привет, нурай")
# for i in range(11):
#     приветствие()

# def validator_password(num):
#     print(num*2)
# validator_password(3)

# def validator_password(num ,a , b , c, d):
#     return num+a+b+c +d
# print(validator_password(3,5,8,6,7))

# def name(first_name):
#     return f"Hello, {first_name}"
# for i in range(11):
#     print(name(input("Type ur name:  ").capitalize()))

# def full_name(first, last, username="не знаю"):
#     return f"Hello {first.capitalize()}{last.capitalize()} login:{username}"
# print(full_name("paten ", "nurai", username = "nnuraip"))

# def database(iin = None):
#     if iin is None:
#         print("Вы забыли указать ИИН.")
#     user = {
#         "080401652844": {
#             "name": "Nurai",
#             "surname": "Paten"
#         },
#         "000000000000":{
#             "name": "Zhans",
#             "surname": "Aryn"
#         }
#     }
#     if not iin.isdigit():
#         return "ИИН должен состоять только из цифр"
#     elif len(iin)!=12:
#         return "ИИН должен содержать 12 цифр"
#     else:
#         return user.get(iin,"ИИН не найден" )
# for i in range(10):
#     get_iin = input("Ur iin: ")
#     print(database(get_iin))

  

# def validator_password(p,p2):
#     if p!=p2:
#          print('Пароли не совпадают!!!')
#     if len(p)<8:
#          print(f"Пароль слишком короткий  {p}")

#     isnum = False
#     islow=False
#     isup=False
#     issimv=False
#     for i in p:
#         if i in '1234567890':
#             isnum = True
#             break
#         if i.islower():
#             islow = True
#             break
#         if i.isupper():
#             isup=True
#             break
#         if i in "!@#$%^&*()_+>?<":
#             issimv=True
#             break
#     if issimv == False:
#         print("В пароле нет специальных символов") 
#     elif islow == False:
#         print("В пароле нет буквы нижнего регистра")
#     elif isup == False:     
#         print("В пароле нет буквы верхнего регистра")
#     elif isnum == False:
#         print("Пароль не содержит цифру")
#     else:
#          print("everything is OK")
    
# get_p = input("Введите ваш пароль: ")
# get_p2 = input("Повторите ваш пароль:  ")
# validator_password(get_p,get_p2)
    
#1 задание = Сложение двух чисел
# def summa(a , b ):
#     return a+b
# print(summa(3,5))

# 2 задание = Проверка четности числа
# def четность(a):
#     if a%2==0:
#       return True
#     else:
#       return False
# print(четность(2))

# 3 задание = Возведение числа в квадрат
# def квадрат(a):
#    return a*a
# print(квадрат(-2))

# 4 задание = Проверка, является ли строка палиндромом
# def Палиндром(text):
#     if text == text[::-1]:
#       return True
#     else:
#       return False
# print(Палиндром("ата"))
# print(Палиндром("папа"))

# 5 задание = Нахождение максимального из двух чисел
# def max(a,b):
#     if a>b:
#       return a
#     elif a<b:
#       return b
#     else:
#        return "They are equal"
# print(max(5,8))

# 6 задание = Нахождение факториала числа
# def factorial (a): 
#    s=1
#    for i in range (1, a+1):
#       s = s * i
#    return s
# print(factorial(5))

# 7 задание = Конвертация градусов Цельсия в градусы Фаренгейта
# def temp_cels (a):
#     return a*1.8 + 32
# print(temp_cels(5))

# 8 задание = Проверка, является ли число простым 
# def prostoe(a):
#     s=0
#     for i in range (2,a):
#         if a%i==0:
#          s=1
#          break
#         if s==1:
#          return "ne prostoe chislo"
#         return "prostoe chislo"   
# print(prostoe(10))

# 9 задание =  Нахождение суммы чисел в списке 
# my_list = [1,2,3,4,5]
# def sum(a):
#     s=0
#     for i in a:
#      s=s+i
#     return s
# print(sum(my_list))

# 10 задание = Подсчет количества гласных в строке
# def glas(a):
#     s=0
#     for i in a:
#         if i in "аяуюоеёэиы" or i in "aeiouy":
#             s+=1
#     return s
# print(glas("нурай"))

### Задача 1: Сумма чисел в диапазоне
# def sum_range(start, end):
#     s=0
#     for i in range (start, end+1):
#         s+=i
#     return s
# print(sum_range(1, 5))

### Задача 2: Поиск минимального числа в списке
# my_list = [1,2,3,4,-10 ,5,6, -8]
# def find_min(numbers):
#     min = numbers[0]
#     for i in numbers:
#         if i<min:
#             min=i
#         else:
#             continue
#     return min
# print("Минимальное число в списке: ",find_min(my_list))

### Задача 3: Подсчет согласных
# def count_consonants(text):
#     s=0
#     for i in text:
#         if i in "Б,В,Г,Д,Ж,З,Й,К,Л,М,Н,П,Р,С,Т,Ф,Х,Ц,Ч,Ш,Щ" or i in "B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z ":
#             s+=1
#     return s
# print("согласных букв ", count_consonants("нурай".upper()))

### Задача 4: Переворот строки
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("uuuuiii"))

### Задача 5: Проверка високосного года
# def is_leap_year(year):
#     if year%4==0:
#         return "високосный год"
#     return "не високосный год"
# print(is_leap_year(1992))

### Задача 6: Произведение всех элементов списка
# my_list = [1,2,3,4,5]
# def product_of_list(numbers):
#     s=1
#     for i in numbers:
#      s=s*i
#     return s
# print(product_of_list(my_list))


### Задача 7: Проверка подстроки
# def contains_substring(s, substring):
#     if substring in s:
#         return "подстрока содержится в строке"
#     return "подстрока не содержится в строке"
# print(contains_substring("asdfg", "d"))

### Задача 8: Поиск индекса элемента
# def find_index(lst, element):
#     index = lst.find(element)
#     if index == -1:
#         return "строка не содержит подстроку"
#     else:
#         return index
# print(find_index("asdfggh", "f"))

### Задача 9: Удаление пробелов
# def remove_spaces(s):
#     return s.replace(" ", "")
# print(remove_spaces("pjd dekrfmnvm rnf f f  ee "))

### Задача 10: Проверка на число
# def is_number(s):
#     if s.isnumeric() == True :
#         num = int(s)
#         return  True
#     return False
# print( is_number("123"))