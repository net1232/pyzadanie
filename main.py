#1
# def welcome():
#     print("Hello!")
# welcome()

#2
# def welcome(name):
#     print(f"Hello {name}")
# name = input("Введите ваше имя: ")
# welcome(name)

#3
# def summator(a, b):
#     print(a+b)
# a = 2
# b = 5
# summator(a, b)

#4
# def inspect(age):
#     if age >= 18:
#         print("Доступ разрешен")
#     else:
#         print("Доступ запрещен")
# age = int(input("Введите ваш возраст: "))
# inspect(age)

#5
# def sqare(n):
#     print(n**2)
# n = int(input("Введите число: "))
# sqare(n)

#6
# def inspect(n):
#     if n %2 == 0:
#         print("Четное")
#     else:
#         print("Нечетное")
# n = int(input("Введите число: "))
# inspect(n)

#7
# def summator(listok):
#     print(sum(listok))
# numbers = [1,2,3,4,5]
# summator(numbers)

#8
# def max_num(numbers):
#     print(max(numbers))
# numbers = [1,8,2,3,4,5]
# max_num(numbers)

#9
# def len_list(listok):
#     print(len(listok))
# numbers = [1,2,3,4,5]
# len_list(numbers)

#10
# def inspect(listoc, element):
#     if element in listoc:
#         print("Найдено")
#     else:
#         print("Не найдено")

# numbers = [1,2,3,4,5]
# number = int(input("Введите число, которое вы ищите: "))
# inspect(numbers, number)

#11
# def score_chet(listok):
#     score = 0
#     for i in listok:
#         if i %2 == 0:
#             score += 1
#     return score

# nums = [1,2,3,4,5,6,7,8,9]
# print(f"Количество четных чисел в списке: {score_chet(nums)}")

#12
# def new_list(old_list):
#     listok = []
#     for i in old_list:
#         if i > 10:
#             listok.append(i)
#     return listok

# numbers = [3, 15, 7, 20, 1, 12]
# print(f"Новый лист: {new_list(numbers)}")

#13
# def calculator(a, b, operation):
#     if operation == 1:
#         return a + b
#     elif operation == 2:
#         return a - b
#     else:
#         return "Ошибка ввода."
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# operation = int(input("Введите 1 если хотите сложить оба числа, или 2 если хотите вычесть второе число от первого: "))

# print(f"Итог: {calculator(a,b,operation)}")

#14
# def score_len(strock):
#     score = 0
#     for i in strock:
#         score += 1
#     print(score)

# text = "Python"
# score_len(text)

#15
# def min_num(numbers):
#     print(min(numbers))
# numbers = [5,3,9,1,7]
# min_num(numbers)