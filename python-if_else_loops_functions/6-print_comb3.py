#!/usr/bin/python3

for i in range(10):
    for j in range(i + 1, 10):
        print("{:02d}".format(i * 10 + j), end="")
        if (not (i == 8 and j == 9)):
            print(", ", end="")
print("")
