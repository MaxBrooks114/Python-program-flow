answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("higher")
elif guess > answer:
    print("lower")
else:
    print("You got it!")