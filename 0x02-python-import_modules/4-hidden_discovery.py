#!/usr/bin/python3

if __name__ == "__main__":
    """Print all the names defined by the compiled module."""
    import hidden_4

    hidden = dir(hidden_4)
    for i in hidden:
        if i[:2] != "__":
            print(i)

