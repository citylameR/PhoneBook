"""
Телефонный справочник
"""

import os
import json

DATA_FILE = 'phonebook.dat'


def load_data():
    """Загрузка данных из файла"""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_data(data):
    """Сохранение данных в файл"""
    with open(DATA_FILE, 'w', 'utf-8') as f:
        json.dump(data, f)


def show_page(data, page_size, page_num):
    """Вывод страницы записей"""
    start = (page_num - 1) * page_size
    end = start + page_size
    print(f'Страница {page_num}')
    for row in data[start:end]:
        print(f"{row['last_name']} {row['first_name']} {row['middle_name']}")
        print(f"Телефон рабочий: {row['work_phone']}")
        print(f"Телефон личный: {row['personal_phone']}")
        print()


def add_record(data):
    """Добавление новой записи"""
    record = {
        'last_name': input('Фамилия: '),
        'first_name': input('Имя: '),
        'middle_name': input('Отчество: '),
        'company': input('Компания: '),
        'work_phone': input('Рабочий телефон: '),
        'personal_phone': input('Личный телефон: ')
    }
    data.append(record)


def edit_record(data):
    """Редактирование записи"""
    index = int(input('Введите индекс записи для редактирования: '))
    record = data[index]

    for key in record:
        value = input(f'{key} ({record[key]}): ')
        if value:
            record[key] = value


def search_records(data):
    """Поиск записей"""
    query = input('Введите запрос: ')
    result = []
    for row in data:
        for value in row.values():
            if query in value:
                result.append(row)
                break

    return result


def main():
    data = load_data()

    while True:
        print('1. Показать страницу')
        print('2. Добавить запись')
        print('3. Редактировать запись')
        print('4. Найти записи')
        print('5. Выход')

        choice = input('Выберите пункт: ')

        if choice == '1':
            page_size = 3
            page_num = int(input('Введите номер страницы: '))
            show_page(data, page_size, page_num)
        elif choice == '2':
            add_record(data)
        elif choice == '3':
            edit_record(data)
        elif choice == '4':
            result = search_records(data)
            show_page(result, len(result), 1)
        elif choice == '5':
            save_data(data)
            break
        else:
            print('Неверный выбор!')


if __name__ == "__main__":
    main()