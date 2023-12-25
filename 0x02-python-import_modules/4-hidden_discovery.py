#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hd
    all_names = dir(hd)
    for name in all_names:
        if not name.startswith("__"):
            print(name)
