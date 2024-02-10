def read_sprav():
    sprav = []
    path = 'tel_sprav.txt'
    tel_sprav = open(path, 'r', encoding = 'utf-8')

    for line in tel_sprav:
        n = line.split(' ')
        dict_ = {
            "last_name": n[0],
            "first_name": n[1],
            "second_name": n[2],
            "tel": n[3],
        }
        sprav.append(dict_)
    tel_sprav.close()
    return sprav

def print_sprav(tel_sprav):
    for item in tel_sprav:
        print(*(f"{k}: {v}" for k, v in item.items()))
    return None

def add_contact():
    s = input("Введите ФИО, телефон, разделенные пробелами: ")
    tel_sprav = open('tel_sprav.txt', 'a', encoding='utf-8')
    tel_sprav.write(f'{s}\n')
    tel_sprav.close()

def find_last_name(last_name, tel_sprav):
    for item in tel_sprav:
        if item["last_name"] == last_name:
            print(item)


def copy_contact():
    source_file = 'tel_sprav_copy.txt' #откуда будем копировать данные
    destination_file = 'tel_sprav.txt' #куда будем копировать

    line_number_input = input("Введите номер строки для копирования: ")
    if line_number_input.isdigit(): #состоит ли введенная строка только из цифр
        line_number = int(line_number_input)
        with open(source_file, 'r', encoding='utf-8') as source:
            lines = source.readlines() #читает все строки из файла и возвращает их в виде списка строк
            if 0 < line_number <= len(lines): #проверяем, что введенный номер строки находится в допустимом диапазоне
                with open(destination_file, 'a', encoding='utf-8') as destination:
                    destination.write(lines[line_number - 1]) #копируем эту строку в файл назначения
                print("Контакт скопирован успешно.")
            else:
                print("Номер строки вне диапазона.")
    else:
        print("Некорректный номер строки.")


def main():
    while True:
        print("Что хотите сделать?")
        print("1: Вывести данные")
        print("2: Записать новый контакт")
        print("3: Найти контакт")
        print("4: Скопировать данные из другого файла")
        print("0: Выйти")

        x = input()
        tel_sprav = read_sprav()
        if x == "1":
            print_sprav(tel_sprav)
        elif x == "2":
            add_contact()
        elif x == "3":
            find_last_name(input("Введите фамилию: "), tel_sprav=tel_sprav)
        elif x == "4":
            copy_contact()
        elif x == "0":
            break
        else:
            print("Неверная команда")


if __name__ == "__main__":
    main()