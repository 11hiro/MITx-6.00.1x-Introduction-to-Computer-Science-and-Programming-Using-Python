# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:34:09 2018

@author: HIROTO
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE.
    for letter in lettersGuessed :
        if letter in secretWord :
            secretWord = secretWord.replace(letter, "")
    if secretWord == "" :
        return True
    else :
        return False
isWordGuessed( "banana",['z', 'x', 'q', 'b', 'a', 'n', 'a', 'n', 'a'] )