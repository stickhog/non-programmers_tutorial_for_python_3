# Write a program that has a user guess your name, but they only get 3 chances to do so until the program quits.

count = 1
myName = 'howard' # use lower case so that the .lower string method can be used
guessName = input('guess my name:')

while count < 3 and guessName.lower() != myName: # .lower returns a copy of the string with all the cased characters...
    # converted to lowercase.
    print("Wrong, try again.")
    guessName = input('guess my name:')
    count += 1 # same as count = count + 1

if guessName.lower() == myName:
    print("Correct.")
#elif count == 3 and guessName != myName:
else:
    print("Wrong. Out of guesses.")
