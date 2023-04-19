#! python3
# -*- coding: utf-8 -*-
# cheater.py - Cheat in games - Scrabble and Slowoku. Polish words.
import collections, os, sys
import pyinputplus as pyip
from pathlib import Path
import numpy as np

def find_anagram(myletters): # Find words built on given letters.
    global your_words
    your_words = []
    for word in words: # Search in dictionary
        if len(word) == wordLength: # Quantity of letters condition.
            wordx = word # Word as 'global variable'.
            word_as_list = [*word] # Split the dictionary word.
            x = 0
            for letter in myletters: # Search for letters in given letters.
                if letter in word_as_list: # Checks if letter is in the dictionary word.
                    x += 1
                    word_as_list.remove(letter) # If letter match, erase it to avoid duplicates.
                    if x == len(myletters): # Adds 'global variable' to results if every letter is in word.
                        your_words.append(wordx)
                    else:
                        continue
                else:
                    x *= 0 # If letter does not match, skip and jump to the next dictionary word.
                    break
        else:
            continue

def chooseGame():
    global lenLetters, lettersWithout_, wordLength, spellingL, no_letters_as_list
    print('\nEnter '66' to exit: ')
    letters = input('\nEnter letters to cheat in Scrabble: \nEnter letters to cheat in Słowoku (symbol "_" for missing letter):\n ').lower().replace(" ", "")
    [(print("Thanks for game."), sys.exit()) if letters == "66" else True] # Exit program.
    spellingL = [*letters] # Split given letters and/or "_" symbols to a list of single characters.
    lettersWithout_ = letters.replace("_","")
    letters_as_list = [*lettersWithout_] # Split given letters to a list with single letters (without "_").
    lenLetters = len(letters) # 'Global variable' that counts quantity of letters and/or "_" symbols.
    print(letters_as_list) # Print letters as list.
    if "_" in letters: # Checks which game is chosen. Here 'SŁOWOKU'.
        print('Enter free letters (ENTER for none): ')
        free_letters = input().lower().replace(" ", "") # Omit spacebars.
        free_lettersWithout_ = free_letters.replace("_", "")
        free_letters_as_list = [*free_lettersWithout_] # Split given free letters to a list with single letters (without "_").
        wordLength = lenLetters # Another 'global variable'. Both needed to play 'SLOWOKU'.
        print(free_letters_as_list)
        print('Enter letters that are excluded (ENTER for none): ') # Asks for forbidden letters.
        no_letters = input().lower().replace(" ", "") # Omit spacebars.
        no_letters_as_list = [*no_letters] # Split given forbidden letters to a list with single letters.
        if any(char in (letters_as_list + free_letters_as_list) for char in no_letters_as_list): # Checks if letters provided by player don't duplicate.
            print("Some letters may be duplicated.")
            chooseGame() # Back to beginning of loop.
        else:
            print('SLOWOKU. Searching for words ...')
            find_anagram(letters_as_list + free_letters_as_list) # Finds words built on given letters.
            oszustSlowoku(your_words) # Adds word to results.
    else: # Checks which game is chosen. Here 'SCRABBLE'.
        wordLength = int(input('\nHow many letters are in desired word?\n '))
        print('SCRABBLE. Searching for words ...')
        find_anagram(letters_as_list) # Finds words built on given letters.
        oszustScrabble(wordPoints, your_words) # Adds word to results. Loads dictionary with letters points ('wordPoints').

def oszustSlowoku(list_of_words): # SLOWOKU game.
    SlowokuSet = set() # List without duplicates.
    for i in range(len(list_of_words)): # "i" equal to number of results from 'find_anagram' loop results.
        spellingW = [*list_of_words[i]] # Split result's word to a list with single letters.
        x = 0
        if any(char in spellingW for char in no_letters_as_list): # Checks if forbidden letter is in word.
            continue
        else:
            for j in range(lenLetters):
                if (spellingL[j] == spellingW[j]): # Checks sequence of the same letters.
                    x += 1 # "x" increased for correct match.
                    if x == wordLength: # Checks all of the criteria.
                        SlowokuSet.add(list_of_words[i]) # And then add word to 'SLOWOKU' results.
                        break
                    else: # Criteria not yet finalized, so check next position.
                        continue
                elif spellingL[j] == "_": # Position as any not forbidden letter.
                    x += 1 # "x" increased for correct match.
                    if x == wordLength:
                        SlowokuSet.add(list_of_words[i])
                        break
                    else:
                        continue
                else:
                    x *= 0 # Criteria incorrect. Reset "x".
                    break # skip and jump to the next result word.
    SlowokuWords = sorted(list(SlowokuSet)) # Alphabetical order.
    results(SlowokuWords) # Print results.

def oszustScrabble(wordPoints, list_of_words):
    global dict_of_words_with_points
    dict_of_words_with_points = {}
    for word in list_of_words: # Checks every word of 'find-anagram' loop results.
        points_sum = 0 # Word points.
        spellingW_as_dict = dict.fromkeys(word.upper(), 0) # Creates dictionary for word.
        for k, v in spellingW_as_dict.items():
            points_sum = points_sum + wordPoints.get(k) # Summarize points of letters.
        dict_of_words_with_points[word.upper()] = points_sum # Adds word with its points.
    sorted_dict = {k: v for k, v in sorted(dict_of_words_with_points.items(), key=lambda item: item[1], reverse = True)} # Sort dictionary by number of points. Descending.
    results(sorted_dict) # Print results.

def results(result): # Print results of games.
    print('\nYour words are (total ' + str(len(result)) + '):')
    l = 1 # Ordinal number.
    if "_" in spellingL: # 'SLOWOKU' results.
        for word in result:
            print(str(l) + ". " + word)
            l += 1
    else:
        for k, v in result.items(): # 'SCRABBLE' results.
            print(str(l) + ". " + k + "  [" + str(v) + "]")
            l += 1

os.getcwd()
os.chdir(r'F:\Dokumenty\Pyton\automate_online-materials') # Set working folder.
fileName = 'slowaPL.txt' # Name of file with words. You can download it from https://sjp.pl/sl/growy/sjp-20230402.zip

# SCRABBLE dictionary of letters points.
wordPoints = {"A" : 1, "E" : 1, "I" : 1, "N" : 1, "O" : 1, "R" : 1, "S" : 1, "W" : 1, "Z" : 1,
                  "C" : 2, "D" : 2, "K" : 2, "L" : 2, "M" : 2, "P" : 2, "T" : 2, "Y" : 2,
                  "B" : 3, "G" : 3, "H" : 3, "J" : 3, "Ł" : 3, "U" : 3,
                  "Ą" : 5, "Ę" : 5, "F" : 5, "Ó" : 5, "Ś" : 5, "Ż" : 5,
                  "Ć" : 6,
                  "Ń" : 7,
                  "Ź" : 9}

print('Loading dictionary ...')
words = sorted({line.strip().lower() for line in open(fileName, 'r', encoding = 'utf-8').readlines()}) # Loads every word from polish dictionary.
letters = []
letters_as_list = []
free_lettersWithout_ = []
no_letters_as_list = []

while True:
    chooseGame()
