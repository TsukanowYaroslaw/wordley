#Импортируем random
import random

#Виселица
HANGMAN_PICS = ['''
                   === ''','''
                    |
                    
                    |
                    
                    |
                   === ''','''
                +---+
                    |
                    
                    |
                    
                    |
                   === ''','''
                +---+
                |   |
                
                    |
                    
                    |                  
                   === ''', '''
                +---+
                |   |
                0
                    |
                    
                    |                  
                   === ''','''
                +---+
                |   |
                0
                |   |
                    
                    |                  
                   === ''','''
                +---+
                |   |
                0
               /|   |
                    
                    |                  
                   === ''','''
                +---+
                |   |
                0
               /|\  |
                    
                    |                  
                   === ''','''
                +---+
                |   |
                0
               /|\  |
                
               /    |                  
                   === ''','''
                +---+
                |   |
                0
               /|\  |
                
               / \  |                  
                   === ''','''
                +---+
                |   |
                0
               /|\  |
                |
               / \  |                  
                   === ''']
print(' В И С Е Л И Ц А')

#Слова
words = ['бобер', 'собака', 'кошка', 'зубр', 'олень', 'заяц', 'медведь', 'корова', 'коза', 'лиса', 'волк', 'поросенок', 'дельфин', 'кит', 'акула']

#Играть снова
def play_again():
    answer = input("Хотите сыграть ещё раз?")
    correctLetters = ""
    missedLetters = ""
    secretWord = getRandomWord(words)
    return answer, correctLetters, missedLetters, secretWord

#Нужные буквы
missedLetters = ''
correctLetters = ''

#Случайное слово
def getRandomWord(wordlist):
    return random.choice(wordlist)

secretWord = getRandomWord(words)

#Дисплей
def  displayBoard(missedLetters, secretWord, correctLetters):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print("Неверная буква:", end=" ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    blanks = "_"*len(secretWord)


    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=" ")
    print()

#Ввод и исравнение
def getGuess(alreadyGuessed):
    while True:
        print("Тема животные")
        guess = input("Угадайте букву:")
        guess = guess.lower()
        if len(guess)!= 1:
            print("Пожалуйста, введите ОДНУ РУССКУЮ БУКВУ")
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя':
            print("Пожалуйста, введите БУКВУ")
        elif guess in alreadyGuessed:
            print("Буква введена. Напишите снова.")
        else:
            return guess
        

#Хотите сыграть ещё?
while True:
    displayBoard(missedLetters, secretWord, correctLetters)
    guess = getGuess(missedLetters + correctLetters)   
    if guess in secretWord:
        correctLetters = correctLetters + guess
        if len(correctLetters) == len(secretWord):
            print("Вы выиграли")
            displayBoard(missedLetters, secretWord, correctLetters)
            answer, correctLetters, missedLetters, secretWord = play_again()
            if answer != "да":
                break
    else:
        missedLetters += guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, secretWord, correctLetters)
            print("Вы проиграли")
            answer, correctLetters, missedLetters, secretWord = play_again()
            if answer != "да":
                break
