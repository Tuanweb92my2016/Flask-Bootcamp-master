def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main__':
    print("One.py is being run directly!")
else:
    print("One.py has been imported!")
