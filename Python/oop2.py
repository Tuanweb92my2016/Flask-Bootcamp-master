def hello():
    return "Hi Jose"

def other(func):
    print("Some other code")

    print(func())

other(hello)
