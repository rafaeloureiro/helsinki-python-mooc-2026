"""
A function named dict_of_numbers(), which returns a new dictionary. The dictionary should have the numbers from 0 to 99 as its keys. 
The value attached to each key should be the number spelled out in words.
"""

def dict_of_numbers():
    ones = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen"
    }
    tens = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
    }

    result = {}
    for i in range(100):
        if i in ones:
            result[i] = ones[i]
        else:
            ten = i // 10
            one = i % 10
            if one == 0:
                result[i] = tens[ten]
            else:
                result[i] = tens[ten] + "-" + ones[one]
    return result
