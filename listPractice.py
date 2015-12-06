# Provide a menu with the following options:
# 1) print the list
# 2) add a name to the list
# 3) remove a name from the list
# 4) change an item in the list
# 9) quit

menu_item = 0
namelist = []
while menu_item != 9:
    print("-------------")
    print("1. Show the list")
    print("2. Add a name to the list")
    print("3. Remove a name from the list")
    print("4. Change a name in the list")
    print("9. Quit")

    menu_item = int(input("Select an option: "))

    if menu_item == 1:
        print("-------------")
        print(namelist)

    elif menu_item == 2:
        namelist.append(input("Name to add: "))
        print("-------------")
        print(namelist)

    elif menu_item == 3:
        nameRemove = input("Name to remove: ")
        if nameRemove not in namelist:
            print("-------------")
            print("Not in list.")
        else:
            namelist.remove(nameRemove)
            print("-------------")
            print(namelist)

    elif menu_item == 4:
        nameChange = input("Name to change: ")
        if nameChange not in namelist:
            print("-------------")
            print("Not in list.")
        elif nameChange in namelist:
            nameChangeTo = input("Name to change to: ")
            namelist[namelist.index(nameChange)] = nameChangeTo
            print("-------------")
            print(namelist)

print("Quit")