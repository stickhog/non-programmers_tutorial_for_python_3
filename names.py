__author__ = 'howardau'
#Write a program that asks the user their name, if they enter your name say "That is a nice name", if they enter
# "John Cleese" or "Michael Palin", tell them how you feel about them ;), otherwise tell them "You have a nice name."
name = input("What's your name?")
if name == 'Howard':
    print("Great name.")
elif name == 'John Cleese':
    print("Funny")
elif name == 'Michael Palin':
    print("Not as funny")
else:
    print("Nice name")
