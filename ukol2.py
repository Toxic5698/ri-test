import math

print('Úkol č. 2')
checker = True
while checker:
    input_data = input('Vložte číslo: ')
    if input_data.isnumeric():
        checker = False
    else:
        print('Špatně zadané číslo. Zkuste znovu.')


def find_prime_palindrome(number):
    print('Počítám pro číslo...' + str(number))
    find_next = True
    while find_next:
        is_prime = True

        for x in range(2, int(math.sqrt(number) + 1)):
            if number % x == 0:
                is_prime = False
                break

        if is_prime:
            prime = str(number)
            if prime == prime[::-1]:
                print(f'Zde je nejbližší prvočíslo, co je palindromem: {prime}')
                find_next = False

        number += 1


find_prime_palindrome(int(input_data))
