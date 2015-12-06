demolist = ["life", 42, "the universe", 6, "and", 9]
print("demolist = ", demolist)

# append an item
demolist.append("everything")
print("After 'everything' was appended demolist is now: ", demolist)

# length of a list
print("len(demolist) =", len(demolist))

# first position of a list item
print("demolist.index(42) =", demolist.index(42))

# item stored in position []
print("demolist[1] =", demolist[1])

# print each item in list sequentially
# create a variable c, starting at 0, and is incremented until it reaches the
# last index of the list
for c in range(len(demolist)):
    print("demolist[", c, "] =", demolist[c])

# a better way of doing the above
for c, x in enumerate(demolist):
    print("demolist[", c, "] = ", x)

# delete an item
del demolist[2]
print("After item 2 was removed, demolist is now:", demolist)

# is an item in a list?
if "life" in demolist:
    print("'life' was found in demolist using an if statement")
else:
    print("'life' was not found in demolist")

if "amoeba" in demolist:
    print("'amoeba' was found in demolist")
if "amoeba" not in demolist:
    print("'amoeba' was not found in demolist")

# sort
another_list = [42, 7, 0, 123]
another_list.sort()
print("The sorted another_list [42,7,0,123] is ", another_list)

# type 'help(list)' for all the functions in a list
