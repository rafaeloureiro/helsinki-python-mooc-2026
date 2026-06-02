"""
A program which works as a simply diary. The diary entries should be saved in the file diary.txt. 
When the program is executed, it should first read any entries already in the file.
"""

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    option = input("Function: ")

    if option == "0":   
        print("Bye now!")
        break

    elif option == "1":
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as my_file:
            my_file.write(f"{entry}\n")
            print("Diary saved")

    elif option == "2":
        with open("diary.txt") as my_file:
            print("Entries:")
            for line in my_file:
                print(line, end="")
