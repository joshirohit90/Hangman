import random
wordList = ["player", "christmas", "boolean", "restaurant", "football"]
index = random.randint(1, 5)
word = wordList[index]
name = input("Enter your name: ")
play = input("Are you ready to play {0}? (Y/N) ".format(name))
incorrectCount = 0
letterCount = 0
letter = ''
openWord = '_' * len(word)
sOpenWord = list(openWord)
won = 0

if play == "Y":
    print("A random word has been selected, guess the letters. You get only 4 incorrect chances")
    print()

    while (incorrectCount < 4) and (won == 0):
        letter = input("Enter a letter: ")
        if letter in word:
            print("You guessed correct")
            for i in range (0, len(word)):
                if letter == word[i]:
                    sOpenWord[i]=letter

            print()
            print(sOpenWord)
            print()
            if '_' not in sOpenWord:
                print("Congratulations, You Won!!")
                won=1
                break
        else:
            print("Sorry, incorrect entry")
            print()
            incorrectCount += 1
    else:
        print("You Failed this test")
else:
    print("Thank You!!")
