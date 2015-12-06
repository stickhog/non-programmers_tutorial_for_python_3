#Write a program that asks the user for a Login Name and password. Then
#when they type "lock", they need to type in their name and password to
#unlock the program.

login = input("Login name? ")
password = input("Password? ")
print ("Login and password stored. Logged in.")

command = input("Type 'lock' to logout.")
while command != "lock":
    command = input("Type 'lock' to logout.")
print ("Program locked.")

loginAttempt = input("Login name? ")
while loginAttempt != login:
    loginAttempt = input("Invalid login. Try again: ")
passwordAttempt = input("Password? ")
while passwordAttempt != password:
    passwordAttempt = input("Invalid password. Try again: ")
    
print ("Logged in.")
