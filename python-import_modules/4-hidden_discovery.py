#!/usr/bin/python3
import marshal

def load_pyc_names(filename):
    with open(filename, "rb") as f:
        f.read(16)
        code_obj = marshal.load(f)
        return code_obj.co_names

if __name__ == "__main__":
    names = load_pyc_names("hidden_4.pyc")
    filtered_names = sorted(name for name in names if not name.startswith("__"))
    for name in filtered_names:
        print(name)
