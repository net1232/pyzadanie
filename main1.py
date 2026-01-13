#1
# def greet():
#     def say_hello():
#         print("hello")
#     say_hello()
# greet()

#2
# def print_name(name):
#     def inner(name):
#         print(name)
#     inner(name)

# name = "Amir"
# print_name(name)

#3
# def square(num):
#     def calc(num):
#         return num **2
#     print(calc(num))
# num = 5
# square(num)

#4
# def check_number(num):
#     def is_positive(num):
#         return num > 0
#     number = is_positive(num)
#     if number == True:
#         print("Положительное")
#     else:
#         print("Отрицательное")
# num = int(input("Введите число: "))
# check_number(num)

# #8
# def greeting(text):
#     def inner(name):
#         return f"{text} {name}"
#     return inner

# print(greeting("Hello", ))

#9
# def access_control(role):
#     def check(role):
#         return role == "Admin"
#     return check(role)
# role = "Admin"
# print(access_control(role))

#10
# def validate_user(name, age):
#     def check_name(name):
#         return len(name) > 0
#     def check_age(age):
#         return age >= 18
#     name = check_name(name)
#     age = check_age(age)
#     if name == True and age == True:
#         print("Все разрешено")
#     else:
#         print("Доступ запрещен")
# validate_user(input("Введите ваше имя: "), int(input("Введите ваш возраст: ")))





#11
# def check_auth(login, password):
#     def check_login(login):
#         return len(login) > 0
#     def check_password(password):
#         return len(password) >= 6
#     if check_login(login) == True and check_password(password) == True:
#         return "Вход выполнен"
#     else:
#         return "Ошибка авторизации."
# print(check_auth("Kiril", "123321098"))
# print(check_auth("", "1233456743222"))
# print(check_auth("Kiril", "12"))
# print(check_auth("", ""))

#12
# def validate_product(name, price):
#     def check_name(name):
#         return len(name) > 0
#     def check_price(price):
#         return price > 0
#     if check_name(name) and check_price(price):
#         print("Товар добавлен")
#     else:
#         print("Ошибка ввода")
# validate_product("Milk", 12)

#13
# def validate_email(email):
#     def has_at(email):
#         return "@" in email
#     def has_dot(email):
#         return "." in email
#     if has_at(email) == True and has_dot(email):
#         print("Emal корректен")
#     else:
#         print("Email некоректен")
# validate_email("Horhfhh@.gmail")

#14
# def check_course_access(complited_lessons, exam_passed):
#     def lessons_done(complited_lessons):
#         return complited_lessons >= 10
#     def exam_done(exam_passed):
#         return exam_passed == True
#     if lessons_done(complited_lessons) and exam_done(exam_passed):
#         print("Курс завершен")
#     else:
#         print("Доступ закрыт")
# check_course_access(18, True)

#15
# def check_permission(age, has_permission):
#     def is_adult(age):
#         return age >= 18
#     def has_parent_permission(has_permission):
#         return has_permission == True
#     if is_adult(age) or has_parent_permission(has_permission):
#         print("Доступ разрешен")
#     else:
#         print("Доступ запрещен")
# check_permission(16, True)