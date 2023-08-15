#!/usr/bin/python3

if __name__ == "__main__":
    """Print all the names defined by the compiled module."""
    import hidden_4

    name = dir(hidden_4)
    for i in name:
        if i[0:2] != "__":
            print(name)
