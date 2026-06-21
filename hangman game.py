import random

players = ["dhoni", "virat", "sachin", "jadeja", "raina","bravo"]
word = random.choice(players)

guessed = ""
limit = 6

while limit > 0:
    display = ""

    for i in word:
        if i in guessed:
            display += i
        else:
            display += "_ "

    print("Word:", display)

    if "_" not in display:
        print("You Win!")
        break

    guess = input("Enter a letter: ")
    guessed += guess

    if guess not in word:
        limit -= 1
        print("Wrong guess! Chances left:", limit)

if limit == 0:
    print("Game Over! The word was", word)
