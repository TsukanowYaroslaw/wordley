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


