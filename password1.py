# asks for a name and a password
# checks them and determines if user is allowed in

name = input("Name?")
password = input("Password?")
if name == "Howard" and password == "douche123":
    print("Welcome Howard")
elif name == "Spongebob" and password == "patrick":
    print("Welcome Spongebob")
else:
    print("I don't know you.")