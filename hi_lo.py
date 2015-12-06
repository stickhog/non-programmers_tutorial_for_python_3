__author__ = 'howardau'
# Plays the guessing game higher or lower

# This should actually be something that is semi random like the
# last digits of the time or something else, but that will have to
# wait till a later chapter.  (Extra Credit, modify it to be random
# after the Modules chapter)

number = 37
#guess = -1

#print("Guess the number between 0 and 100.")

guess = float(input("Guess the number between 0 and 100. Guess? "))
while guess != number:
    if guess < number:
        print("Higher")
        guess = float(input("Guess? "))
    elif guess > number:
        print("Lower")
        guess = float(input("Guess? "))
print("Correct")