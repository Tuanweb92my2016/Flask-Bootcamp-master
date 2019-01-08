import wolframalpha

input1 = input("Question: ")

app_id = "3R5TUE-VX6GG8Y3JX"

client = wolframalpha.Client(app_id)

res = client.query(input1)

answer = next(res.results).text

print(answer)
