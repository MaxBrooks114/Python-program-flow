answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("Got it on the first try!")
else:
    if guess < answer:
        print("Higher")
    else:
        print("Lower")
    guess = int(input())
    if guess == answer:
        print("You got it!")
    else:
        print("wrong!")

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