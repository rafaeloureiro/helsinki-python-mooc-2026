"""
Improved version of password generator.
"""

from random import choice, randint
from string import ascii_lowercase, digits
 
def generate_strong_password(length: int, numbers: bool, special_characters: bool):
    special_chars = "!?=+-()#"
    # One letter at beginning of the password
    passwd = choice(ascii_lowercase)
    choice_set = ascii_lowercase
 
    if numbers:
        passwd = add_character(passwd, digits)
        choice_set += digits
 
    if special_characters:
        passwd = add_character(passwd, special_chars)
        choice_set += special_chars
 
    while (len(passwd) < length):
        passwd = add_character(passwd, choice_set)
 
    return passwd
 
def add_character(passwd: str, characters):
    character = choice(characters)
    if randint(1,2) == 1:
        return character + passwd
    else:
        return passwd + character
