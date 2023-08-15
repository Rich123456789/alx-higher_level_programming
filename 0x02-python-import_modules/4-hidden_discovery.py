#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by the compiled module."""
    import hidden_4

    hidden_name = dir(hidden_4)
    for i in hidden_name:
        if i[:2] != "__":
            print(hidden_name)
