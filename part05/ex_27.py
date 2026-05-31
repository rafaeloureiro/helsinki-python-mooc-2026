"""
A program which prints out a square of letters.
"""

layers = int(input("Layers: "))
size = 2 * layers - 1

for row in range(size):
    line = ""
    for col in range(size):
        distance = min(row, col, size - 1 - row, size - 1 - col)
        line += chr(ord("A") + layers - 1 - distance)
    print(line)
