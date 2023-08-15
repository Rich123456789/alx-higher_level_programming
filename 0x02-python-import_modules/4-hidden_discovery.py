#!/usr/bin/python3

if __name__ == "__main__":
    """Print all the names defined by the compiled module."""
    import hidden_4

    names = dir(hidden_4)
    for i in names:
        if i[0:2] != "__":
            print(i)
