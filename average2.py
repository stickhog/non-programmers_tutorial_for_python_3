# keeps asking for numbers until count numbers have been entered.
# Prints the average value.

count = 0
sum = 0

countRequested = int(input("How many numbers to average? "))
print("Enter numbers to average.")

while count < countRequested:
    entry = float(input("Number? "))
    count = count + 1
    sum = sum + entry

print("Average is: ", sum/count)
