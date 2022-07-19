import random
def hungman():
    word=random.choice(["hello","superman","ironman","thor","avengers","earth","savewater","anshul","batman","internet"])
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ''
    while len(word) > 0 :
        main = ""
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "*"
        if main == word :
            print(main)
            print("You Win!...")
            print("     \ O /     ")
            print("       |       ")
            print("      / \    \n")
            print("   THANK YOU   ")
            print("     HAPPY     ")
            break
        guess = input("\nGuess the Word : "+  main + "\n")
        if guess in validLetters :
            guessmade = guessmade + guess
        else:
            print("Enter a Valid Character : ")
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9 :
                print("9 Turns Left...")
                print("---------------")
            if turns == 8:
                print("8 Turns Left...")
                print("---------------")
                print("       O       ")
            if turns == 7:
                print("7 Turns Left...")
                print("---------------")
                print("       O       ")
                print("       |       ")
            if turns == 6:
                print("6 Turns Left...")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      /        ")
            if turns == 5:
                print("5 Turns Left...")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      / \      ")
            if turns == 4:
                print("4 Turns Left...")
                print("---------------")
                print("     \ O       ")
                print("       |       ")
                print("      / \      ")
            if turns == 3:
                print("3 Turns Left...")
                print("---------------")
                print("     \ O /     ")
                print("       |       ")
                print("      / \      ")
            if turns == 2:
                print("2 Turns Left...")
                print("---------------")
                print("     \ O /|    ")
                print("       |       ")
                print("      / \      ")
            if turns == 1:
                print("1 Turns Left...")
                print("Last Breaths Counting, Take Care!...")
                print("---------------")
                print("     \ O_|/    ")
                print("       |       ")
                print("      / \      ")
            if turns == 0:
                print("You Lose!...")
                print("You Let a Kind Man Die...")
                print("---------------")
                print("       O_|     ")
                print("      /|\      ")
                print("      / \      ")
                print("\n GAME OVER!...")
                break
name = input("Enter your Name :  ")
print("\n")
print(" \t ================")
print("\t|| HUNGMAN GAME ||")
print("\t ================")
print("\nWelcome",name)
print("---------------------------------")
ch = 'y'
while ch == 'y' :
    print("Try to Guess the Word in Less than 10 Attempts...")
    hungman()
    print()
    ch = input("Want to Play Again...[Y/N]...")
