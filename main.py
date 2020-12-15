import random

dickPic = ['''
+---+
    |
    |
    |
    |
========
''', '''
+---+
 |  |
 0  |
    |
    |
========
''', '''
+---+
 |  |
 0  |
 |  |
    |
========
''', '''
+---+
 |  |
 0  |
/|  |
    |
========
''', '''
+---+
 |  |
 0  |
/|\ |
    |
========
''', '''
+---+
 |  |
 0  |
/|\ |
/   |
======== 
''', '''
+---+
 |  |
 0  |
/|\ |
/ \ |
========
СМЭРТЬ 
''']


def get_secret_word():
    file = open('word_rus.txt', 'r')
    bank = []
    for line in file:
        bank.append(line)
    secretWord = bank[random.randint(0, len(bank) - 1)]
    return secretWord


def game_board(missedLetters, correctLetters, secretWord):
    print("< В_И_С_Е_Л_И_Ц_А >", end='')
    print(dickPic[len(missedLetters)], end='')
    print('Ошибочные буквы: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    hidden = '_' * (len(secretWord) - 1)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            hidden = hidden[:i] + secretWord[i] + hidden[i + 1:]
    for letter in hidden:
        print(letter, end='')
    print()


def get_letter(bannedLetters):
    while True:
        letter = input()
        letter = letter.lower()
        if len(letter) > 1:
            print("Введи только одну букву")
        elif letter in bannedLetters:
            print("Два раза одну и ту же букву? У нас так не принято.")
        elif letter not in "йцукенгшщзхъёфывапролджэячсмитьбю":
            print("Вообще, тут слова состоят из РУССКИХ БУКВ")
        else:
            return letter


missedLetters = ''
correctLetters = ''
secretWord = get_secret_word()
foundAllLetters = False

while True:
    game_board(missedLetters, correctLetters, secretWord)
    enterChar = get_letter(missedLetters + correctLetters)

    if enterChar in secretWord:
        correctLetters += enterChar
        foundAllLetters = True
        for i in range(len(secretWord) - 1):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
    else:
        missedLetters += enterChar
    if foundAllLetters:
        game_board(missedLetters, correctLetters, secretWord)
        print("Winner winner chicken dinner! ")
        print("Твое слово: " + secretWord)
        input("Enter, чтобы выйти")
        break
    if len(missedLetters) == 6:
        game_board(missedLetters, correctLetters, secretWord)
        print()
        print("Ты проиграл! (͡° ͜ʖ ͡°)")
        print("Загаданое слово: " + secretWord)
        input("Enter, чтобы выйти")
        break
