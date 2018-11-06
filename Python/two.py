import one

print("TOP LEVEL in TWO.PY")

one.func()

if __name__ == '__main__':
    print("Two.py is being run directly!")
else:
    print("Two.py has been imported!")
