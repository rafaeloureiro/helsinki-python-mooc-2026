"""
A phone book application to search numbers, add numbers or quit functions included.
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
        phone_book[name] = number
        print("ok!")
    elif code.lower() == "1":
        name = input("name: ")
        if name in phone_book:
            print(f"{phone_book[name]}")
        else:
            print(f"no number")
