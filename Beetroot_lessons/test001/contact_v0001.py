import json
from rich.console import Console
from rich.table import Table

contacts = {}

help_text = """
Ви можете керувати роботою скрипта за допомогою наступних кодів:
a — додати контакт;
d — видалити контакт;
p — надрукувати список контактів;
q — завершити роботу скрипта;
h — надрукувати текстову підказку з командами керування скриптом.
"""

welcome_text = """
Добрий день, everybody!

Це скрипт книги контактів.
""" + help_text
air = "\n" + "*" * 20 + "\n"
print(welcome_text, air)

# Підгружаємо жсон файл і розбираємо його на словник
try:
    with open('contacts.json', 'r') as f:
        data = json.loads(f.read())
        for key, value in data.items():
            contacts[int(key)] = value
except:
    print("Ваш список контактів ще порожній або якийсь москаль видалив файл. Не "
          "переймайтесь, ми то виправимо!", air)

while 1:
    action = input("Введіть команду:\n")

    # Інструкції щодо додавання нового контакту

    if action == "a":
        name = input('Введіть імʼя контакту:\n')
        phone = input('Введіть телефон:\n')
        address = input('Введіть адресу:\n')
        try:
            contacts[(list(contacts.keys())[-1]) + 1] = {'name': name, 'phone': phone,
                                                         'address': address}
        except:
            contacts[1] = {'name': name, 'phone': phone, 'address': address}

    # Інструкції щодо видалення контакту

    elif action == "d":
        deleted_item = input(
            'Введіть ID контакту, що ви бажаєте видалити або команду «отмєна», якщо '
            'передумали:\n').lower()
        if deleted_item == "отмєна":
            print('Окєй, нічого не видаляєм', air)
        elif deleted_item.isdigit():
            deleted_name = contacts[int(deleted_item)]['name']
            del contacts[int(deleted_item)]
            print(f'Контакт {deleted_name} успішно видалено з бази', air)

    # Інструкції щодо друку списку контактів

    elif action == "p":
        if contacts:
            table = Table(title="Список контактів")

            table.add_column("ID", justify="right", style="cyan", no_wrap=True)
            table.add_column("Імʼя")
            table.add_column("Телефон")
            table.add_column("Адреса")

            for k, v in contacts.items():
                table.add_row(str(k), v['name'], v['phone'], v['address'])

            console = Console()
            console.print(table)
        else:
            print('Список контактів порожній, тож ще нема чого друкувати!', air)

    # Інструкції щодо відображення підказок

    elif action == "h":
        print(help_text, air)

    # Інструкції щодо виходу з програми

    elif action == "q":
        with open("contacts.json", "w") as f:
            data_to_save = json.dumps(contacts, ensure_ascii=False)
            f.write(data_to_save)
        print("Хай щастить! Слава Україні!")
        break
    else:
        print("Здається ви ввели невідому мені команду, спробуйте ще раз або отримайте "
              "підказку за командою h")