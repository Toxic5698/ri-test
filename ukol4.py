import csv
import re


print('Úkol č. 4')


def check_isbn(isbn):
    isbn = isbn.replace("-", "").replace(" ", "").upper()
    match = re.search(r'^(\d{9})(\d|X)$', isbn)
    if not match:
        return False

    digits = match.group(1)
    check_digit = 10 if match.group(2) == 'X' else int(match.group(2))

    result = sum((i + 1) * int(digit) for i, digit in enumerate(digits))
    return (result % 11) == check_digit


def check_price(price):
    price_elements = re.findall(r'-\d+|[.,]|\d+|.+', price)

    # positive number
    if int(price_elements[0]) < 0:
        return False

    # is float
    if price_elements[1] != ('.' or ','):
        return False

    # right format of float
    # if len(price_elements[2]) != 2:
    #     return False

    # contain currency
    try:
        if len(price_elements[3].strip()) < 1 or price_elements[3].isnumeric():
            return False
    except IndexError:
        return False

    # everything alright
    return True


with open('tNmieVFn.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    for index, row in enumerate(csv_reader, 1):
        # elements in row
        if len(row) != 4:
            pass
            print(f'Error! {len(row)} column(s) on line: {str(index)}')
        else:
            for data_index, data in enumerate(row):
                # missing data
                if data_index == (0 or 1) and data is None or data.strip() == '':
                    dict_data = {
                        0: 'title',
                        1: 'author',
                        2: 'ISBN',
                        3: 'price'
                    }
                    print(f'Missing {dict_data[data_index]} on line: {index}')
                # invalid ISBN
                elif data_index == 2 and not check_isbn(row[2]):
                    print(f'Invalid ISBN on line: {str(index)}')
                # invalid price
                elif data_index == 3 and not check_price(row[3]):
                    print(f'Invalid price on line: {index}')
