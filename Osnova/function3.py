# def my_decorator(func):
#     def wrapper():
#         print('start')
#         print(func())
#         print('end')
#     return wrapper

# @my_decorator
# def hello():
#     return 'qwerty'

# @my_decorator
# def kkk():
#     return 'asdf'

# hello()
# kkk()


# from time import time
# def timing_decorator(func):
#     def wrapper():
#         start_time= time()
#         print(func())
#         end_time = time()
#         # print(f'func {func.__name__} worked {round(end_time-start_time)}')
#         print(f'func {func.__name__} worked {end_time-start_time:.2f}')
#     return wrapper


# @timing_decorator
# def hello():
#     return 'qwerty'

# @timing_decorator
# def kkk():
#     return 'asdf'

# # hello()
# # kkk()

# # def func():
# #     return func()
# # print(func())


# def recurs(n): 
#     print(n)  #,end=' '
#     if n<=1:
#         return 0
#     return recurs(n-1)
# print(recurs(10))
