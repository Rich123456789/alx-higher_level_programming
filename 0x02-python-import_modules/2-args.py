#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    from sys import argv

    num = len(argv) - 1
    if num == 0:
        print("0 arguments.")
    elif num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num))
    for i in range(num):
        print("{}: {}".format(i + 1, argv[i + 1]))
