import random

# word = "secret"
with open("hangwords.txt", "r") as file:
    words = file.readlines()

word = random.choice(words)[:-1]
# print(word)


allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    if allowed_errors == 1:
        guess = input("{} attempt left, Next guess\n>>".format(allowed_errors))
    else:
        guess = input("{} attempts left, Next guess\n>>".format(allowed_errors))
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print("Congratulations!!! :) You has won the game! \nThe word was \"{}\"".format(word.upper()))
else:
    print("Game Over :(  \nThe word was \"{}\"".format(word.upper()))