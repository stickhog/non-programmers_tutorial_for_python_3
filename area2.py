# calculate area of rectangle

def hello():
    print("Hello!")

def area(width, height):
    return width*height

def print_welcome(name):
    print('Welcome,', name)

def positive_input(prompt):
    number = float(input(prompt))
    while number <= 0:
        print('Must be positive')
        number = float(input(prompt))
    return number

name = input('Your name: ')
hello()
print_welcome(name)
print()
print('Enter width and height below')
print()
w = positive_input('Width: ')
h = positive_input('Height: ')

print('Width =', w, 'Height =', h, 'Area =', area(w, h))
