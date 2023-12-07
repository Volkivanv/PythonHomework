# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

from os.path import exists
from csv import DictReader, DictWriter


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


class FirstNameError(Exception):
    def __init__(self, txt):
        self.txt = txt


class LastNameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    # Проверка на правильность имени
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise FirstNameError("Не валидное имя")
            else:
                is_valid_first_name = True
        except FirstNameError as err:
            print(err)
            continue
    # Проверка на правильность фамилии
    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input("Введите фамилию: ")
            if len(last_name) < 2:
                raise LastNameError("Не валидная фамилия")
            else:
                is_valid_last_name = True
        except LastNameError as err:
            print(err)
            continue
    # Проверка на правильность телефонного номера
    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input('Введите номер: '))
            if len(str(phone_number)) != 11:
                raise LenNumberError('Неверная длина номера')
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер")
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]


#Создание нового файла
def create_file(file_name):
    # context manager
    with open(file_name, 'w', encoding='utf-8', newline="") as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


#Чтение файла
def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


#внесение записи в файл
def write_file(file_name, lst):
    res = read_file(file_name)
    for el in res:
        if el['Телефон'] == str(lst[2]):
            print("Такой телефон уже есть")
            return
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def order_print(lst):
    print(f" | Имя | Фамилия | Телефон |")
    for i in range(0, len(lst)):
        print(f"{i}| {lst[i]['Имя']} | {lst[i]['Фамилия']} | {lst[i]['Телефон']} |")


file_name = 'phone.csv'
another_file_name = 'phone2.csv'

def main():
    while True:
        command = input("Введите комманду: q - выйти, w - создание и запись файла, r - чтение файла, "
                        "a - перенести запись в другой файл ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            order_print(read_file(file_name))
        #Перенос записи в другой файл
        elif command == 'a':
            if not exists(file_name):
                print("Исходный файл отсутствует. Создайте его")
                continue
            index = int(input("Введите порядковый номер записи, которую хотите перенести: "))
            if not exists(another_file_name):
                create_file(another_file_name)
            phone_list = list(read_file(file_name)[index].values())
            decision = input(f"Вы точно хотите пренести эту запись? y - да, "
                             f"другой символ - нет: {" | ".join(phone_list)} ")
            if decision == 'y':
                write_file(another_file_name, phone_list)
            else:
                continue


main()
