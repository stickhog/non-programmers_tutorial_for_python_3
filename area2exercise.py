# calculate area of rectangle, square, circle with menu interface

def hello():
    print("Hello!")

def menu():
    print("This calculates the area of a rectangle, square, or circle.")
    print("Press 'm' to show this menu again")
    print("Press 'r' for rectangle")
    print("Press 's' for square")
    print("Press 'c' for circle")
    print("Press 'q' to quit")

def print_welcome(name):
    print('Welcome,', name)

def positive_input(prompt):
    number = float(input(prompt))
    while number <= 0:
        print('Must be positive')
        number = float(input(prompt))
    return number

def area_rectangle(width, height):
    return width*height

def area_square(length):
    return length**2

def area_circle(radius):
    return (22/7)*radius**2

name = input('Your name: ')
hello()
print_welcome(name)
print()

choice = "m"
while choice != "q":
    if choice == "r":
        print('Enter width and height below')
        print()
        w = positive_input('Width: ')
        h = positive_input('Height: ')
        print()
        print('Width =', w, 'Height =', h, 'Area =', area_rectangle(w, h))
        print()
        choice = "m"
        
    elif choice == "s":
        print('Enter length of one side')
        print()
        l = positive_input('Side: ')
        print()
        print('Side =', l, 'Area =', area_square(l))
        print()
        choice = "m"

    elif choice == "c":
        print('Enter radius of circle')
        print()
        r = positive_input('Radius: ')
        print()
        print('Radius =', r, 'Area =', area_circle(r))
        print()
        choice = "m"

    elif choice == "m":
        menu()
        choice = input("Option: ")

    elif choice != "q":
        print('That is not a valid option.')
        print()
        menu()
        choice = input("Option: ")
