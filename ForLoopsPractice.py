__author__ = 'howardau'

#onetoten = range(1,11)
#for count in onetoten:
#    print(count)

#list = [2,4,6,8]
#sum = 0
#for num in list:
#    sum = sum + num
#print("The sum is:", sum)

list = [4,5,7,8,9,1,0,7,10]
list.sort()
prev = None
for item in list:
    if prev == item:
        print("Duplicate of", prev, "found")
    prev = item

#a = 1
#b = 1
#for c in range(1,10):
#    print(a, end=" ")
#    n = a + b
#    a = b
#    b = n