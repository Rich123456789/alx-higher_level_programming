#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    no_of_arg = len(sys.argv) - 1
    if no_of arg == 0:
        print("0 arguments.")
    elif no_of_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(no_of_arg))
    for i in range(no_of_arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
