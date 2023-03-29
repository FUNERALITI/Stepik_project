from random import choice


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        ''' 
                   -------- 
                   |      | 
                   |      O 
                   |     \\|/ 
                   |      | 
                   |     / \\
                   - 
                ''',
        # голова, торс, обе руки, одна нога
        ''' 
                   -------- 
                   |      | 
                   |      O 
                   |     \\|/ 
                   |      | 
                   |     /  
                   - 
                ''',
        # голова, торс, обе руки
        ''' 
                   -------- 
                   |      | 
                   |      O 
                   |     \\|/ 
                   |      | 
                   |       
                   - 
                ''',
        # голова, торс и одна рука
        ''' 
                   -------- 
                   |      | 
                   |      O 
                   |     \\| 
                   |      | 
                   |      
                   - 
                ''',
        # голова и торс
        ''' 
                   -------- 
                   |      | 
                   |      O 
                   |      | 
                   |      | 
                   |      
                   - 
                ''',
        # голова
        ''' 
                   -------- 
                   |      | 
                   |      O 
                   |     
                   |       
                   |      
                   - 
                ''',
        # начальное состояние
        ''' 
                   -------- 
                   |      | 
                   |       
                   |     
                   |       
                   |      
                   - 
                '''
    ]
    return stages[tries]


ru_alphabet = 'АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'  # русский алфавит
word_list = ['тысяча', 'книга', 'возможность', 'результат', 'ночь', 'стол', 'имя', 'область', 'статья', 'число',
             'компания', 'народ', 'жена', 'группа', 'развитие', 'процесс', 'суд', 'условие', 'средство', 'начало',
             'свет', 'пора', 'путь', 'душа', 'уровень', 'форма', 'связь', 'минута', 'улица', 'вечер', 'качество',
             'мысль', 'дорога', 'мать', 'действие', 'месяц', 'государство', 'кровь', 'район', 'небо', 'армия', 'класс',
             'представитель', 'участие', 'девочка', 'политика', 'герой', 'картина', 'доллар', 'спина', 'территория',
             'пол', 'поле', 'изменение', 'направление', 'рисунок', 'течение', 'церковь', 'банк', 'сцена', 'население',
             'большинство', 'музыка', 'правда', 'свобода', 'память', 'команда', 'союз', 'врач', 'договор', 'дерево',
             'факт', 'хозяин', 'природа', 'угол', 'телефон', 'позиция', 'двор', 'писатель', 'самолет', 'объем', 'род',
             'солнце', 'вера', 'берег', 'спектакль', 'фирма', 'способ', 'завод', 'цвет', 'журнал', 'руководитель',
             'специалист', 'оценка', 'регион', 'песня', 'процент', 'родитель', 'море', 'требование', 'основание',
             'половина', 'роман', 'круг', 'анализ', 'стихи', 'автомобиль', 'экономика', 'литература', 'бумага', 'поэт']


def is_valid(w_l):  # защита от дурака
    if w_l.isalpha():
        for i in w_l:
            if i in ru_alphabet:
                return True


def get_word():
    word = choice(word_list).upper()
    return word


def play(word):
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    print("Давайте играть в угадайку слов!")
    print(display_hangman(tries))
    print(f'Загадано слово из {len(word)} букв', word_completion)
    print(word)  # после теста удалить!
    while tries != 0:
        word_or_letter = input('Введи слово или букву\n').upper()
        while not is_valid(word_or_letter):
            print('Похоже ты ввел не верный символ')
            print(word_completion)
            word_or_letter = input('Введи снова слово или букву\n').upper()
        if word_or_letter in guessed_letters:
            print('Вы уже называли эту букву')
            print('Названные буквы', *guessed_letters)
            print(word_completion)
            continue
        if word_or_letter in guessed_words:
            print('Вы уже называли это слово')
            print('Названные слова', *guessed_words)
            print(word_completion)
            continue
        if word_or_letter == guessed_words:
            print('Вы уже называли это слово')
            continue
        if len(word_or_letter) > 1:
            guessed_words.append(word_or_letter)
            print('Названные слова', *guessed_words)
        if len(word_or_letter) == 1:
            guessed_letters.append(word_or_letter)
            print('Названные буквы', *guessed_letters)
        if word_or_letter == word:
            return 'Поздравляем, вы угадали слово! Вы победили!'
        if word_or_letter in word:
            print('Вы угадали букву')
            for i in range(len(word)):
                if word[i] == word_or_letter:
                    word_completion = word_completion[:i] + word_or_letter + word_completion[i + 1:]
            print(word_completion)
            if word_completion == word:
                return 'Поздравляем, вы угадали слово! Вы победили!'
        if word_or_letter not in word:
            print('Такой буквы нет в этом слове')
            tries -= 1
            print(display_hangman(tries))
            print(word_completion)
    if tries == 0:
        print('GAME OVER')
        return f'Было загадано слово "{word.capitalize()}"'


def play_again():
    while True:
        answer = input('Хотите сыграть снова? Введите да или нет')
        if answer == 'да':
            print(play(get_word()))
        if answer == 'нет':
            print('Возвращайся')
            break
        else:
            print('Не понял Вас')
            continue


print(play(get_word()))
play_again()