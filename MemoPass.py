import string
import secrets
import random

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

if __name__ == '__main__':
    words = list(load_words())
    characters = '/@!$%*&()_-=[]{},.<>;:?'
    count_words = 2
    count_simbols = 4
    password_length = 18
    random_words = list()
    random_chars = list()
    continueLoop = True
    password = ''
    while continueLoop:
        for z in range(count_words):
            random_words.append(str(secrets.choice(words)))
        if len(''.join(random_words)) < password_length - count_simbols:
            continueLoop = False
        else:
            random_words.clear()
    
    for x in range(16 - len(''.join(random_words))):
        random_chars.append(secrets.choice(characters))

    final_list = random_chars + random_words

    n = len(final_list)

    while n > 1:
        n -= 1
        sel = random.randint(0, n)
        value = final_list[sel]
        final_list[sel] = final_list[n]
        final_list[n] = value
    else:
        password = password.join(final_list)


    print(password)