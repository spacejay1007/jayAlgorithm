N = input()

# 1단계
lower = N.lower()
answer = ""
# print(lower)

# 2단계
for i in lower:
    if i.isalnum() or i in "-_.":
        answer += i

# if '..' in answer:
#     answer.replace("..", ".")
# 3단계
while ".." in answer:
    answer = answer.replace("..", ".")

# 4단계
answer = answer.strip(".")

# 5단계
if answer == "":
    answer += 'a'

# 6단계
if len(answer) >= 16:
    answer = answer[0:15]
    answer = answer.rstrip(".")

# 7단계
if len(answer) <= 2:
    # answer += answer[1]
    # print(answer[:1])
    # answer += answer[1:]
    answer_id = len(answer)
    add_word = answer[len(answer)-1:]
    while len(answer) < 3:
        answer += add_word

print(answer)
