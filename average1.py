# keeps asking for numbers until 0 is entered.
# Prints the average value.

count = 0
sum = 0
entry = 1

print("Enter numbers to average. Enter 0 to exit.")

while entry != 0:
    entry = float(input("Value? "))
       
    if entry != 0:
        count = count + 1
        sum = sum + entry

    if entry == 0:
        print("Average is: ", sum/count)
