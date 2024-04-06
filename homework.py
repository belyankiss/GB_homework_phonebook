from csv import DictReader, DictWriter
from os.path import exists
file_name = 'phone.csv'

def get_info():
    first_name = 'Sergei'
    last_name = 'Kudri'
    flag = False
    while not flag:
        try:
            phone_number = int(input('Write the phone number: '))
            if len(str(phone_number)) != 11:
                print('Incorrect phone number. Try again...')
            else:
                flag = True
        except ValueError:
            print('Not valid number')
    return [first_name, last_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['name', 'surname', 'phone'])
        f_w.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)

def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'name': lst[0],
           'surname': lst[1],
           'phone': lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['name', 'surname', 'phone'])
        f_w.writeheader()
        f_w.writerows(res)


def copy_row_from_old_file(row, old_file):
    with open(old_file, 'r', encoding='utf-8') as old_data:
        f_r = DictReader(old_data)
        if row <= len(list(f_r.reader)) - 1:
            return list(f_r.reader)[row]
        else:
            print('You write a integer which not exists in the phonebook. Try again...')
            return False


def main() -> None:
    while True:
        command = input('Write the command: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name=file_name, lst=get_info())
        elif command == 'r':
            if not exists(file_name):
                print('File not exists you should create file')
                continue
            for row in read_file(file_name):
                print(row)
        elif command == 'c':
            new_file_name = input("Create a new file and it's name like 'new_phone.csv'... ")
            if '.csv' in new_file_name:
                if not exists(new_file_name):
                    create_file(new_file_name)
                flag = False
                while not flag:
                    try:
                        row_number = int(input("Choose a row which you want to copy..."))
                        row_str = copy_row_from_old_file(row_number, old_file=file_name)
                        if row_str is list:
                            write_file(new_file_name, row_str)
                    except ValueError:
                        print("The value should be an integer. Try again!")
                    else:
                        flag = True
            else:
                print("The file must have an extension '.csv'")


            # print(*read_file(file_name=file_name))


main()



