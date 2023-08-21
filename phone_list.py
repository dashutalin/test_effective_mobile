import csv
import os
from typing import Callable

INFO: list[str] = ['id', 'Name', 'Surname', 'Last name',
                   'Company', 'Work phone', 'Home phone']

with open('phone_list.csv', 'r') as file:
    COUNTER: int = int(file.readlines()[-1].split(',')[0])
    print(COUNTER)


def write_row() -> None:
    '''
    Function to write a new line to a file.
    No parametrs.
    '''
    with open('phone_list.csv', 'a') as file:
        global COUNTER
        name: str = input('Input name: ')
        surname: str = input('Input surname: ')
        last_name: str = input('Input last name: ')
        company: str = input('Input company: ')
        work_phone: str = input('Input work phone: ')
        home_phone: str = input('Input home phone: ')
        csv_writer = csv.writer(file, lineterminator="\r")
        COUNTER += 1
        csv_writer.writerow([COUNTER, name, surname, last_name,
                             company, work_phone, home_phone])


def read_row() -> None:
    '''
    Function for reading records in a file with a
    specified number of lines.
    No parametrs.
    '''
    with open('phone_list.csv', 'r') as file:
        csv_reader = csv.reader(file)
        state = True
        while state:
            amount: int = int(input('Enter the number of lines'
                                    'you want to read: '))
            for _ in range(amount):
                try:
                    print(next(csv_reader))
                except Exception:
                    print('It was the last row.')
                    state = False
            ans: str = input('If you want to finish, write "stop": ')
            if ans == 'stop':
                state = False


def search() -> None:
    '''
    Function for searching for strings that contain one
    or more input values.
    No parametrs.
    '''
    with open('phone_list.csv', 'r') as file:
        values: set[str] = set()
        value: str = input('Input value for search.'
                           'If you want to stop, enter - "stop". ')
        while value != 'stop':
            values.add(value)
            value = input('Input value for search: ')
        print(values)
        for line in csv.reader(file):
            if set(line) >= values:
                print(','.join(line))


def edit() -> None:
    '''
    Function for editing one specified value in a line with
    the specified id in the file.
    No parametrs.
    '''
    with open('phone_list.csv', 'r') as file:
        num_of_row: int = int(input('Enter id of line: '))
        csv_reader = file.readlines()
        edit_row = csv_reader[num_of_row].split(',')
        key = input('What do you want to change: 1 - name, '
                    '2 - surname, 3 - last name, '
                    '4 - company, 5 - work number, 6 - home number: ')
        value = input('Input value for change: ')
        edit_row[int(key)] = value
        csv_reader[num_of_row] = ','.join(edit_row)
        with open('phone_list.csv', 'w') as f:
            f.writelines(csv_reader)


def main() -> None:
    actions: dict[str, Callable[[], None]] = {
        'r': read_row,
        'a': write_row,
        's': search,
        'e': edit
    }
    while True:
        choose: str = input('Choose what you want to do and click the button:'
                            'read - "r", edit - "e", search - "s", '
                            'add new - "a". If you want to finish,'
                            'write the "stop".\n')
        if choose == "stop":
            break
        actions[choose]()


if __name__ == '__main__':
    if not os.path.exists('phone_list.csv'):
        with open('phone_list.csv', 'w+') as file:
            csv_writer = csv.DictWriter(file, fieldnames=INFO,
                                        lineterminator="\r")
            csv_writer.writeheader()
    main()
