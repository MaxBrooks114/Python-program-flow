options = ["exit", "sleep", "play", "eat", "learn", "work"]
choice = None
option = ''

while choice != 0:
    for option in options:
        print(str(options.index(option)) + ". " + option)
    choice = int(input("Please choose an option: "))
    if choice < len(options):
        print("you have chosen {}. Enjoy!".format(options[choice]))
    else:
        print("That is not an option")
else:
    print("Goodbye")
