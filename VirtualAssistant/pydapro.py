import wikipedia
import wolframalpha

while True:

    input1 = input("Question: ")

    try:

        #wolframalpha
        app_id = "3R5TUE-VX6GG8Y3JX"

        client = wolframalpha.Client(app_id)

        res = client.query(input1)

        answer = next(res.results).text

        print(answer)

    except:
        #wikipedia

        wikipedia.set_lang("en")
        print(wikipedia.summary(input1, sentences=2))
        
