# def show_menu() -> int:
# print("\nВыберите необходимое действие:\n"
# "1. Отобразить весь справочник\n"
# "2. Найти абонента по фамилии\n"
# "3. Найти абонента по номеру телефона\n"
# "4. Добавить абонента в справочник\n"
# "5. Сохранить справочник в текстовом формате\n"
# "6. Закончить работу")
# choice = int(input())
# return choice

# def work_with_phonebook():
# choice = show_menu()
# phone_book = read_csv('phonebook.csv')


# while (choice != 6):
# if choice == 1:
# print_result(phone_book)
# elif choice == 2:
# name = get_search_name()
# print(find_by_name(phone_book, name))
# elif choice == 3:
# number = get_search_number()
# print(find_by_number(phone_book, number))
# elif choice == 4:
# user_data = get_new_user()
# add_user(phone_book, user_data)
# write_csv('phonebook.csv', phone_book)
# elif choice == 5:
# file_name = get_file_name()
# write_txt(file_name, phone_book)
# choice = show_menu()

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_csv(filename: str, data) -> str:
    file = open(filename, 'w', encoding='utf-8')
    for lines in data:
        s = ', '.join(f'{v}' for k, v in lines.items())
        file.write(s + '\n')


def write_txt(filename: str, data) -> str:
    file = open(filename + '.txt', 'w', encoding='utf-8')
    for lines in data:
        s = ', '.join(f'{v}' for k, v in lines.items())
        file.write(s + '\n')

def get_file_name()-> str:
    name_of_the_file = input('Введите название файла для сохранения -> ')
    return name_of_the_file

def show_menu() -> int:
    print('\Выберрите тип зароса:\n'
          '1. Показать справочник\n'
          '2. Поиск абонента по фамилии\n'
          '3. Поиск абонента по номеру телефона\n'
          '4. Добавить абонента в справочник\n'
          '5. Удалить абонента из справочника\n'
          '6. Сохранитьсправочник\n'
          '7. Закончить работу со справочником')
    choice = int(input())
    return choice

def print_result(data) -> list:
    print(*data, sep='\n')

def find_by_name(data, name) -> str:
    for key in data:
        if key['Фамилия'].upper() == name.upper():
            return key.values()
    return('Такого пользователя нет')

def find_by_number(data, phone_number) -> str:
    for key in data:
        if key['Телефон'] == phone_number:
            return key.values()
    return('Такого пользователя нет')
        

def get_new_user() -> dict:
    record = {
        'Фамилия': input('Введите фамилию -> '),
        'Имя': input('Введите имя -> '),
        'Телефон': input('Введи номер телефона -> '),
        'Описание': input('Введи описание -> ')
    }
    return record

def add_user(data, new_record) -> list:
    data.append(new_record)
    print(*data, sep='\n')



def delete_user(data: list, last_name: str) -> str:
    for i in range(len(data)):
        if data[i].get("Фамилия") == last_name:
            del data[i]
            return f"Абонент {last_name} успешно удален"
        return "Такой абонент отсутствует в списке"

phone_book = read_csv('phonebook.csv')

choice = show_menu

while (choice != 7):
    if choice == 1:
        print_result(phone_book)
    elif choice == 2:
        name = (input('Введи фамилию абонента -> ')) 
        print(*(find_by_name(phone_book, name)))
    elif choice == 3:
        number = input('Введи номер телефона абонента -> ')
        print(*(find_by_number(phone_book, number)))
    elif choice == 4:
        user_data = get_new_user()
        add_user(phone_book, user_data)
        write_csv('phonebook.csv', phone_book)
    elif choice == 5:
        user_data = input('Введи фамилию пользователя для удаления -> ')
        delete_user(phone_book, user_data)
        write_csv('phonebook.csv', phone_book)
    elif choice == 6:
        file_name = get_file_name()
        write_txt(file_name, phone_book)
    choice = show_menu()