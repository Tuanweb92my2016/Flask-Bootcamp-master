import wikipedia

while True:

    input1 = input("# QUESTION: ")
    wikipedia.set_lang("en")
    print(wikipedia.summary(input1, sentences=2))
