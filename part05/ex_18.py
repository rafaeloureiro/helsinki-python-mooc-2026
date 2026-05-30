"""
The phone book application from the exercise prior improved that a name (key) can handle multiple phone numbers.
"""

phone_book = {}
while True:
    code = input("command (1 search, 2 add, 3 quit): ")
    if code.lower() == "3":
        print("quitting...")
        break
    elif code.lower() == "2":
        name = input("name: ")
        number = input("number: ")
        if name in phone_book:
            phone_book[name].append(number)
        else:
            phone_book[name] = [number]
        print("ok!")
    elif code.lower() == "1":
        name = input("name: ")
        if name in phone_book:
            for number in phone_book[name]:
                print(number)
        else:
            print("no number")
