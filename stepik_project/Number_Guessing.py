from random import *

random_num = randint(1, 100)
print('Добро пожаловать в числовую угадайку', random_num)
count = 0


def is_valid(n):
    return int(n) in range(1, 101)


def check_number(entered_num):
    if entered_num < random_num:
        print("Ваше число меньше загаданного, попробуйте еще разок")
    elif entered_num > random_num:
        print("Ваше число больше загаданного, попробуйте еще разок")
    elif entered_num == random_num:
        print("Вы угадали, поздравляем!")
        return True


while True:
    question = int(input("Введите число от 1 до 100"))
    result = is_valid(question)
    count += 1
    if not result:
        print("А может быть все таки введем целое число от 1 до 100?")
        continue
    else:
        print(int(question))

    if check_number(question):
        print("Число попыток:", count)
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
        break
