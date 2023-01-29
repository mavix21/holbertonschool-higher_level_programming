#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv)
    i = 1
    sum = 0

    while i < argc:
        sum += int(argv[i])
        i += 1

    print("{}".format(sum))
