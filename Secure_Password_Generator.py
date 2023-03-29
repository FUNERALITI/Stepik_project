from random import *

# Создание констант
DIGITS = "1234567890"
LOWERCASE_LETTER = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^_"

chars = ''

# Считывание данных юзера

num = int(input("Сколько нужно паролей?"))
length_pass = int(input("Какая длинна одного пароля?"))
digit = input("Включать ли цифры 1234567890? (д==Да, н==Нет)")
A_letter = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д==Да, н==Нет)")
a_letter = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д==Да, н==Нет)")
symbol = input("Включать ли символы !#$%&*+-=?@^_ ? (д==Да, н==Нет)")
ambiguous_symbol = input("Исключать ли неоднозначные символы il1Lo0O? (д==Да, н==Нет)")

# Формирования алфавита для генерации

if digit.lower() == "д":
    chars += DIGITS
if A_letter.lower() == "д":
    chars += UPPERCASE_LETTERS
if a_letter.lower() == "д":
    chars += LOWERCASE_LETTER
if symbol.lower() == "д":
    chars += PUNCTUATION
if ambiguous_symbol.lower() == "д":
    for j in "il1Lo0O":
        chars = chars.replace(j, "")

# Генерация пароля

def password_generation(lenght, chars):
    password = ''
    for i in range(lenght):
        password += choice(chars)
    return password


for a in range(num):
    print(password_generation(length_pass, chars))