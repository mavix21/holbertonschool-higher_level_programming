#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hiddenNames = dir(hidden_4)
    for name in hiddenNames:
        if name.startswith("__"):
            continue
        print(name)
