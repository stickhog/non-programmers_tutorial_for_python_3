list = ["Life", "The Universe", "Everything", "Jack", "Jill", "Life", "Jill"]

# make a copy of the list. See the More On Lists chapter for what [:] means.
copy = list[:]
# sort the copy
copy.sort()
prev = copy[0]
del copy[0]

count = 0

# go through the list searching for a match
while count < len(copy) and copy[count] != prev:
    prev = copy[count]
    count = count + 1

# if a match was not found, then count can't be < len
# since the while loop continues while count is < len
# and no match is found

if count < len(copy):
    print("First match:", prev)
