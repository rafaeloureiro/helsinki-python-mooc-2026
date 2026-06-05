"""
A function which creates passwords of a desired length, consisting of lowercase characters a to z.
"""

from random import sample
from string import ascii_lowercase

def generate_password(n: int):
    return "".join(sorted(sample(ascii_lowercase, n)))
  
