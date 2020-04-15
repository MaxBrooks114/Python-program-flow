import random
highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = None

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("game over")
        break
    if guess == answer:
        print("correct")
        break
    else:
        if guess < answer:
            print("Higher")
        else:
             print("Lower")







# if guess < answer:
#     print("higher")
#     guess = int(input())
#     if guess == answer:
#         print("You got it!")
#     else:
#         print("wrong!")
# elif guess > answer:
#     print("lower")
#     guess = int(input())
#     if guess == answer:
#         print("You got it!")
#     else:
#         print("wrong!")
# else:
#     print("You got it!")