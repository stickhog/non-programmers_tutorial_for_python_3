# Rewrite the area2.py program from the Examples above to have a separate function for the area of a square, the area
# of a rectangle, and the area of a circle (3.14 * radius**2). This program should include a menu interface.

def hello():
    print("Hello!")

def area(width, height):
    return width*height

def areaSquare(length):
    return length**2

def areaCircle(radius):
    return ((22/7)*radius**2)

def print_welcome(name):
    print('Welcome,', name)

def positive_input(prompt):
    number = float(input(prompt))
    while number <= 0:
        print('Must be positive')
        number = float(input(prompt))
    return number

name = input("Your name: ")
hello()
print_welcome(name)
print()

choice = "m"

while choice != "q":
    if choice == "m":
        print("Select an option:")
        print("'m' - show this menu")
        print("'s' - calculate area of square")
        print("'r' - calculate area of rectangle")
        print("'c' - calculate area of circle")
        print("'q' - quit")
        choice = input("Choice: ")

    elif choice == "s":
        print("Enter length of side below:")
        l = positive_input("Length: ")
        print("Length of side =", l, "Area =", areaSquare(l))
        choice = input("Choice: ")

    elif choice == "r":
        print("Enter width and height below")
        w = positive_input('Width: ')
        h = positive_input('Height: ')
        print("Width =", w, "Height =", h, "Area =", area(w,h))
        choice = input("Choice: ")

    elif choice == "c":
        print("Enter radius below:")
        r = positive_input("Radius: ")
        print("Radius =", r, "Area", areaCircle(r))
        choice = input("Choice: ")

    elif choice == "q":
        print("Quit")

    else:
        print("Invalid selection")
        choice = "m"