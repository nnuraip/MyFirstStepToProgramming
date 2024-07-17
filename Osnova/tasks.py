# №1
# def neg(a):
#     if a>0:
#         return "число не отрицательное"
#     elif a<0:
#         return "число отрицательное"
#     else:
#         return "число = 0"
# print(neg(-5))
    
# №2
# def dlina(ff):
#     return len(ff)
# print(dlina("jedfh"))

# # №3
# def last(ff):
#     return ff[len(ff)-1]
# print(last("jedfh u6i"))

# №4
# def even(d):
#     if d%2==0:
#         return "число четное"
#     else:
#         return "число не четное"
# print(even(5))

# №5
# a="asdf"
# b="awert"
# def equal(l,h):
#     if l[0]==h[0]:
#         return "they are same"
#     else:
#         return "they are not same"
# print(equal(a,b))

# №6
# def last(ff):
#    a=ff[len(ff)-1]
#    if a=="ь":
#       return ff[len(ff)-2]
#    else:
#       return a
# print(last("jedfh u6iь"))

#№1
# def first(ff):
#     a=str(ff)
#     return a[0]
# print(first(456))

#№2
# def last(ff):
#     a=str(ff)
#     return a[len(a)-1]
# print(last(5468))

#№3
# def s(d):
#     a=str(d)
#     return int(a[0])+int(a[-1])
# print(s(456))

# #№4
# def kol(l):
#     a=str(l)
#     return len(a)
# print(kol(456789))

# # №5
# def equal(l,h):
    
#     if str(l)[0]==str(h)[0]:
#         return "they are same"
#     else:
#         return "they are not same"
# print(equal(569,584))

# # №6
# a=[1, 2, 3, 4, 5, 6]
# def m(s):
#     my_list=[]
#     for i in s:
#         if len(my_list) == 3:
#             break
#         my_list.append(i)
#     return my_list
# print(m(a))

# №1
# def s(k):
#     if len(k)>1:
#         return k[-2]
# print(s("ljdnf"))

# №2
# def f(i,e):
#     if i%e==0:
#         return "первое число без остатка делится на второе."
#     else:
#         return "первое число без остатка не делится на второе."
# print(f(10,5))

# # №3
# def a(l):
#     my_list=[]
#     for i in l:
#         my_list.append(i)
#     return my_list
# print(a('abcde'))

# # # №4
# a=[1, 2, 3, 4, 5, 6]
# def m(s):
#     my_list=[]
#     for i in s[2:]:
#         if len(my_list) == 3:
#             break
#         my_list.append(i)
#     return my_list
# print(m(a))

# №5
# a = {
#     'year': '2025',
#     'month': '12',
#     'day': '31',
# }
# def dat(f):
#     return f"{f['year']}-{f['month']}-{f['day']}"

# print(dat(a))

# level 1.4
#  №1
# def num(a):
#     p=[]
#     for i in range(1,a+1):
#         p.append(i)
#     return p
# print(num(100))

#  №2
# def num(a):
#     p=[]
#     for i in range(a,1):
#         p.append(i)
#     return p
# print(num(-100))

# №3
# def num(a):
#     p=[]
#     for i in range(a,0,-1):
#         p.append(i)
#     return p
# print(num(100))


#  №4
# def num(a):
#     p=[]
#     for i in range(1,a+1):
#         if i%2==0:
#           p.append(i)
#         else:
#            continue
#     return p
# print(num(100))

#  №5
# def num(a):
#     p=[]
#     for i in range(1,a+1):
#         if i%3==0:
#           p.append(i)
#         else:
#            continue
#     return p
# print(num(100))

#  №6
# a= [1, 2, 3, 4, 5, 6]
# def s(n):
#     return n[4:]
# print(s(a))

#  №7
# s = 'abcdeabc'
# def r(s):
#     return set(s)
# print(r(s))

# уровень 1,5
#  №1
# def num(a):
#     sum = 0
#     for i in range(a + 1):
#         sum = sum+i
#     return sum
# print(num(100))

# #  №2
# def num(a):
#     sum = 0
#     for i in range(a + 1):
#         if i%2==0:
#             sum = sum+i
#     return sum
# print(num(100))


# #  №3
# def num(a):
#     sum = 0
#     for i in range(a + 1):
#         if i%2==1:
#             sum = sum+i
#     return sum
# print(num(100))

#  №4
# def num(a,b):
#     return a%b
# print(num(12,10))

#  №5
# a=[1, 2, 3, 4, 5, 6]
# def k(d):
#     return d[::2]
# print (k(a))

# Уровень 1.6 
# #  №1
# a=[1, 2, 3, 4, 5]
# def o(g):
#     return sum(g)
# print(o(a))

# #  №2
# a=[1, 2, 3, 4, 5]
# def kvadrat(g):
#     sum=0
#     for i in g:
#         sum=sum+i**2
#     return sum
# print(kvadrat(a))

# # #  №3
# a=[1, 2, 3, 4, 5]
# def kvadrat(g):
#     sum=0
#     for i in g:
#         sum=sum+i**0.5
#     return sum
# print(kvadrat(a))

#  №4
# a=[1, 2, -3, 4, -5]
# def sum_pol(num):
#     sum=0
#     for i in num:
#         if i>0:
#             sum+=i
#     return sum
# print(sum_pol(a))

#  №5
# a=[-1, 2, -3, 4, 5, 11]
# def sum_pol(num):
#     sum=0
#     for i in num:
#         if 0<i<10:
#             sum+=i
#     return sum
# print(sum_pol(a))

#  №6 - chat gpt
# s = 'abcde'
# for i in range(len(s) -1, -1, -1):
#     print(s[i])

# Уровень 1.7
# #  №1
# a= {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3, 
# 	'd': 4,
# }
# def s(e):
#     sum= len(list(e.values()))
#     return sum
# print(s(a))

#  №2
# a= {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3, 
# 	'd': 4,
# }
# def s(e):
#     for i in e.items():
#     	sum= list(e.values()**2)
# 	return sum
# print(s(a))