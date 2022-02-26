import sys
from sys import setrecursionlimit

print('Úkol č. 1')
# input and check data
checker = True
while checker:
    input_data = input('Vložte slova oddělená čárkou: ')
    if len(input_data) < 3:
        print('Málo znaků, zkuste znovu.')
    else:
        words_set = set(word.strip() for word in input_data.split(','))
        print(len(words_set))
        if len(words_set) < 2:
            print('Zadáno pouze jedno použitelné slovo, zkuste znovu.')
        else:
            checker = False

words_to_process = list(words_set)
print('Slova ke zpracování: ' + str(words_to_process))
# words_to_process = ['egg', 'gasolin', 'academy', 'neural', 'lobotomy', 'ypsilon']
# words_to_process = ['ant', 'tiger', 'racoon', 'ning', 'giraffe', 'elephant']
words_to_process = ['AB', 'BA', 'BC', 'CD']
counter = len(words_to_process)
if counter > 500:
    setrecursionlimit(counter * 5)


# proces data
def word_chain(words):
    global counter
    if counter == 0:
        if len(words) == 1:
            print(f'Vytvořený řetězec: {words[0]}')
        else:
            longest = max(words, key=len)
            print(f'Nejdelší řetězec: {longest}')
            words.remove(longest)
            print(f'Ostatní slova {words}')
    else:
        #word1 = max(words, key=len)
        for word1 in words:
            for word2 in words:
                if word1 != word2 and word1[-1] == word2[0]:
                    new_word = ' - '.join((word1, word2))
                    words.append(new_word)
                    words.remove(word1)
                    words.remove(word2)
                    break
                elif word1 != word2 and word2[-1] == word1[0]:
                    new_word = ' - '.join((word2, word1))
                    words.append(new_word)
                    words.remove(word1)
                    words.remove(word2)
                    break

            counter -= 1
            word_chain(words)


# output result
word_chain(words_to_process)
