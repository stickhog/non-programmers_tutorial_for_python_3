which_one = int(input("What month (1-12)? "))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

#tweaked this to check whether the entry was in the range of 1-12. if not, then
#continue to prompt for the proper entry until a value 1-12 is given.


if 1 <= which_one <= 12:
    print("The month is", months[which_one - 1])
else:
    while which_one < 1 or which_one > 12:
        print("Must be 1-12")
        which_one = int(input("What month (1-12)? "))

    print("The month is ", months[which_one - 1])
