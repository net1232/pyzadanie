# 1. показать
# 2. добавить
# 3. сохранить
# 0. выйти

def load_notes_txt():
    notes = []
    with open("data/notes.txt", "r", encoding="utf-8") as file:
        for i in file:
            clean = i.strip()
            if clean != "":
                notes.append(clean)
    return notes

def show_notes_txt(notes):
    if len(notes) == 0:
        print("Заметок нет")
        return
    number = 1
    for i in notes:
        print(number, ".", i)
        number += 1

def add_note_txt(notes):
    text = input("Введите заметку: ").strip()
    if text == "":
        print("Пустую заметку нельзя добавить")
        return
    notes.append(text)
    print("Добавлено!")

def save_notes_txt(notes):
    with open("data/notes.txt", "w", encoding="utf-8") as file:
        for i in notes:
            file.write(i + "\n")

notes = load_notes_txt()

while True:
    print("\n1. Показать\n2. Добавить \n3. Сохранить \n0. Выход\n")
    choise = input("Выбор: ")

    if choise == "1":
        show_notes_txt(notes)
    elif choise == "2":
        add_note_txt(notes)
    elif choise == "3":
        save_notes_txt(notes)
    elif choise == "0":
        save_notes_txt(notes)
        print("Выход...")
        break
    else:
        print("Ошибка ввода.")
        