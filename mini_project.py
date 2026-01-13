products = []
def add_product(name, price, count):
    if price <= 0 or count <= 0:
        print("Цена и количество товара не может быть меньше или равно нулю.")
        return
    product = {
        "name": name,
        "price": price,
        "count": count
    }
    products.append(product)

def show_products():
    if len(products) == 0:
        print("Товаров нет")
        return
    index = 1
    for product in products:
        print(f"{index}. {product["name"]}-{product["price"]} тг, {product["count"]} шт")
        index += 1

def get_total_price():
    total = 0
    for product in products:
        total += product["price"]
    return total

while(True):
    choise = input("\n1. Добавить товар \n2. Показать товары \n3. Показать общую сумму \n0. Выход \nВведите ваш выбор: ")
    if choise == "1":
        name = input("Введите название товара: ")
        price = int(input("Цена товара: "))
        count = int(input("Введите количество данного товара: "))
        add_product(name, price, count)
    elif choise == "2":
        show_products()
    elif choise == "3":
        print(f"Общая сумма: {get_total_price()} тг")
    elif choise == "0":
        print("Выход...")
        break
    else:
        print("Ошибка ввода.")