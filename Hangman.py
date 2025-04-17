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
