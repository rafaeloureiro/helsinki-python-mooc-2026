"""
A function named find_words(search_term: str). It should return a list containing all the words in the file which match the search term.
The search term may include lowercase letters and the following wildcard characters:
- A dot . means that any single character is acceptable in its place. For example, ca. would yield words like cat and car, p.ng would yield words like ping and pong, and .a.e would yield words like sane, care and late.
- An asterisk * at the end of the search term means that any word which begins with the search term is acceptable. An asterisk at the beginning of the search term means that any word which ends with the search term is acceptable. For example, ca* would yield words like california, cat, caring and catapult, while *ane would yield words like crane, insane and aeroplane.
There can only ever be a single asterisk in the search term.
- If there are no wildcard characters in the search term, only words which match the search term exactly are returned.
"""

def find_words(term: str) -> list:
    with open("words.txt") as f:
        words = [word.strip() for word in f]

    result = []

    for word in words:
        # Asterisk at the beginning: word must end with the suffix
        if term[0] == "*":
            suffix = term[1:]
            if len(word) >= len(suffix) and word[len(word)-len(suffix):] == suffix:
                result.append(word)

        # Asterisk at the end: word must begin with the prefix
        elif term[-1] == "*":
            prefix = term[:-1]
            if len(word) >= len(prefix) and word[:len(prefix)] == prefix:
                result.append(word)

        # Dot wildcard: word must have same length, matching char by char
        elif "." in term:
            if len(word) == len(term):
                match = True
                for i in range(len(term)):
                    if term[i] != "." and term[i] != word[i]:
                        match = False
                        break
                if match:
                    result.append(word)

        # Exact match
        else:
            if word == term:
                result.append(word)

    return result
