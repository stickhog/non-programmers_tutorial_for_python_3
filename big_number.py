__author__ = 'howardau'
#Write a program that asks for two numbers. If the sum of the numbers is greater than 100, print "That is a big number."

print("Input 2 numbers to add together")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
if num1 + num2 > 100:
    print("That's a big number.")
else:
    print("That's a small number.")