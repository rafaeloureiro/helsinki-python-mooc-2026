"""
A function named most_common_words(filename: str, lower_limit: int) that takes a filename and an integer value for a lower limit as its arguments. 
The function should return a dictionary containing the occurrences of the words which appear at least the number of times specified in the lower_limit parameter.
"""

def most_common_words(filename: str, lower_limit: int) -> dict:
    with open(filename) as file:
        text = file.read()

    punctuation = ".,;:!?\"'()[]{}—-–…"
    for char in punctuation:
        text = text.replace(char, "")

    words = text.split()

    counts = {word: words.count(word) for word in set(words)}
    return {word: count for word, count in counts.items() if count >= lower_limit}
