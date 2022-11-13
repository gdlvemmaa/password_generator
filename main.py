import random

# constants
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
excluded_symbols = 'il1Lo0O'

q_digits = 'Включать ли цифры "0123456789"?'
q_upper_case = 'Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"?'
q_lower_case = 'Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"?'
q_symbols = 'Включать ли символы "!#$%&*+-=?@^_"?'
q_excluded = 'Исключать ли неоднозначные символы "il1Lo0O"?'


def is_valid(question):
    while True:
        answer = input(question)
        if answer.lower() == 'да':
            return True
        elif answer.lower() == 'нет':
            return False
        else:
            print('Введены неверные данные. Попробуйте ещё раз\n')


def generate_password():
    chars = []
    col, length = int(input('Введите количество генерируемых паролей\n')), \
                  int(input('И длину всех паролей\n'))
    if is_valid(q_digits):
        chars.append(digits)
    if is_valid(q_upper_case):
        chars.append(uppercase_letters)
    if is_valid(q_lower_case):
        chars.append(lowercase_letters)
    if is_valid(q_symbols):
        chars.append(punctuation)
    if not is_valid(q_excluded):
        chars.append(excluded_symbols)
    chars = ''.join(chars)
    for i in range(col):
        print('Пароль ', i + 1, ':  ', *random.choices(chars, k=length),
              sep='')


generate_password()
