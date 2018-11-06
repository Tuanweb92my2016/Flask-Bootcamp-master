
def hello(name='Jose'):
    print('the hello() func has been run')

    def greet():

        return "            This is inside the greet()"

    def welcome():

        return "            This is inside welcome()"

    # print(greet())
    # print(welcome())

    if name == "Jose":
        return greet
    else:
        return welcome


x = hello("Tuan")
print(x())
