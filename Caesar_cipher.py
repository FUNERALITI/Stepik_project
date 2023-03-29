# # Данные юзера
#
# direction = input("Укажите направление: (шифрование, дешифрование) ")
# lang = input("Какой язык использовать? (ру==Русский, англ == Английский) ")
# step = int(input("Укажите шаг сдвига: "))
# text = input("Введите текст: ")
#
# # Алфавит
# # low_letter = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й",
# #               "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю",
# #               "я"]
# alph = ['АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
#
# # Шифрование на русском с известным нам шагом
# # Пироги
#
# for i in text:
#     if i.isalpha():
#         char = alph[lang][(alph[lang].index(i.upper()) + step) % len(alph[lang])]
#         print(char if i.isupper() else char.lower(), end='')
#     else:
#         print(i, end='')
#
# # def cesar_ru(dir, lang, stp, txt):
# #     result = []
# #     lst = ""
# #     if dir == "шифрование":
# #         if lang == "ру":
# #             for i in txt:
# #                 result.append(low_letter.index(i) + stp)
# #             for i in result:
# #                 lst += low_letter[i]
# #     return lst
# #
# #
# # print(cesar_ru(direction, language, step, text))

alph = ['АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
direction = input('Выбери направление: \n(+) - Шифрование \n(-) - Дешифрование:\n ')
lang = int(input('Выбери язык алфавита: \n0 - Русский \n1 - Английский: \n'))
step = int(direction + input('Веди число, шаг сдвига (со сдвигом вправо): '))
text = input('Введите текст для обработки:\n')

for i in text:
    if i.isalpha():
        char = alph[lang][(alph[lang].index(i.upper()) + step) % len(alph[lang])]
        print(char if i.isupper() else char.lower(), end='')
    else:
        print(i, end='')