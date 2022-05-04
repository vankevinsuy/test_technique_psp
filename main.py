import string
from collections import deque

def alphabetCenterOn(l):
    alphabet = deque([letter for letter in string.ascii_uppercase])

    if l.upper() not in alphabet:
        raise Exception("l not in alphabet") 

    while alphabet[0] != l:
        alphabet.rotate(1)

    return alphabet

def getTime(s):
    result = 0
    init_letter = "A"
    inputs = [letter.upper() for letter in s]

    for letter in inputs:

        reordered_alapbet = list(alphabetCenterOn(letter))
        
        if reordered_alapbet.index(init_letter) > 13:
            result += reordered_alapbet.index(init_letter) - 13
        else:
            result += reordered_alapbet.index(init_letter)

        init_letter = letter


    return result