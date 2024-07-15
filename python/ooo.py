a= input("введите строку:  ")
b = input("подстрока:  ")
index = a.find(b)
if index == -1:
    print("строка не содержит подстроку")
else:
    print("строка содержит подстроку")