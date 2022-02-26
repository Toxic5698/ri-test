import math

print('Úkol č. 2')
checker = True
while checker:
    input_data = input('Vložte číslo: ')
    if input_data.isnumeric() and int(input_data) > 10:
        checker = False
    else:
        print('Špatně zadané číslo. Zadané číslo musí být větší než 10. Zkuste znovu.')


def find_prime_palindrome(number):
    print('Počítám pro číslo...' + str(number))
    find_next = True
    while find_next:
        is_prime = True
        if number % 2 == 0:
            number += 1

        if str(number) == str(number)[::-1]:
            for x in range(3, int(math.sqrt(number) + 1), 2):
                if number % x == 0:
                    is_prime = False
                    break

            if is_prime:
                print(f'Zde je nejbližší prvočíslo, co je palindromem: {number}')
                find_next = False

        number += 2


find_prime_palindrome(int(input_data))
