# Fahrenheit / Celcius converter

def print_options():
    print("Options:")
    print("'man' show manual")
    print("'c' convert from Celcius to Fahrenheit")
    print("'f' conert from Fahrenheit to Celcius")
    print("'q' quit")

def celcius_to_fahrenheit(c_temp):
    return 9.0/5.0 * c_temp +32

def fahrenheit_to_celcius(f_temp):
    return (f_temp - 32.0)*5.0/9.0

choice = "man"
while choice != "q":
    if choice == "c":
        c_temp = float(input("Celcius: "))
        print("Fahrenheit: ", celcius_to_fahrenheit(c_temp))
        choice = input("Option: ")
    elif choice == "f":
        f_temp = float(input("Fahrenheit: "))
        print("Celcius: ", fahrenheit_to_celcius(f_temp))
        choice = input("Option: ")
    elif choice != "q":
        print_options()
        choice = input("Option: ")
