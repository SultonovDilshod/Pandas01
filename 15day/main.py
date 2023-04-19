import json

with open('database.json', 'r') as file:
    data = json.loads(file.read())
    print(data)
for question in data:
    print(question["Quession text"])
    for index, alternative in enumerate(question["Alternatives"]):
        print(index + 1, '-', alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question['user_choice'] == question["correct_answer"]:
        score += 1
        result = "Correct answer"
    else:
        result = "Wrong answer"
    message = f"{result} {index + 1} - Your answer: {question['user_choice']}, " \
              f"{index + 1} - Correct answer is {question['correct_answer']}"
    print(message)
print(score, "/", len(data))

print("Git uchun birinchi praktika")
print("Git ucdddddddddddddddddddd")
print("Git uchun birinchi praktika")
