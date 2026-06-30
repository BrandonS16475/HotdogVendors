import os

stop = 2
doEdit = ""
iD = []
name =[]
dates = []

def quickSort(lis):
    if len(lis) <=1:
        return lis
    pivot = lis[0]
    left = []
    right = []

    for i in lis[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return(quickSort(left) + [pivot] + quickSort(right))

def binarySearch(items, searchItem):
    found = False
    first = 0
    last = len(items) - 1
    midpoint = 0
    while first <= last and found == False:
        midpoint = (first + last) // 2
        if items[midpoint] == searchItem:
            print("Found at", midpoint)
            found = True
        elif items[midpoint] < searchItem:
            first = midpoint + 1
        else:
            last = midpoint - 1
    if found is False:
        print("Not found")

def linearSearch(items, target):
    index = 0
    found = False
    while found == False and index < len(items):
        if target == items[index]:
            found = True
            print("Found", index)
        index = index + 1
        if found == False:
            print("not found")


f = open(r"C:\Users\s16475\Documents\GitHub\HotdogVendors\Hotdogs.txt", "r") # opens the file (used the whole directory because was giving an error)
for i in f:
    contents = f.readline()
    sec = contents.split(",")
    iD.append(sec[0])
    name.append(sec[1])
    dates.append(sec[2])

f.close

print("Welcome to the Hotdog Vendors program.")

while stop != 1:
    try:
        do = input("What do you want to do? Edit(e) Search(s) View(v) Stop(stop): \n")
    except TypeError:
        print("Try again")
    except ValueError:
        print("Try again")
    
    if do == "v":
        f = open(r"C:\Users\s16475\Documents\GitHub\HotdogVendors\Hotdogs.txt", "r")

        print("ID: \t\tName: \t\tDate: \t\tVegan Hotdogs: \t\tMeat Hotdogs: \t\tOnions(kg): \t\tKetchup(l)")

        for i in f:
            contents = f.readline() # Reads a singular line from the file. The for loop will allow the whole file to be printed
            sec = contents.split(",")

            print(sec[0], "\t\t", sec[1], "\t", sec[2],"\t",
            sec[3],"\t\t\t", sec[4], "\t\t\t", sec[5], "\t\t\t", sec[6]) #All this for a table
        f.close
    if do == "s":
        f = open(r"C:\Users\s16475\Documents\GitHub\HotdogVendors\Hotdogs.txt", "r")

        quickSort(iD)
        quickSort(name)
        quickSort(dates)

        types = input("Would you rather search normally or search in a sorted way? ")
        stype = input("what would you like to search for? Type name, iD, or dates\n") # Doing search algorithm
        target = input("Enter search target: ")
        if types == "sorted":
            if stype == "name":
                binarySearch(name, target)
            elif stype == "ID":
                binarySearch(iD, target)
            elif stype == "dates":
                binarySearch(dates, target)
        if types == "sorted":
            if stype == "name":
                linearSearch(name, target)
            elif stype == "ID":
                linearSearch(iD, target)
            elif stype == "dates":
                linearSearch(dates, target)
        f.close

    if do == "e":
        i = 0
        n = open("HotdogsNew.txt", "a")

        f = open(r"C:\Users\s16475\Documents\GitHub\HotdogVendors\Hotdogs.txt", "r")

        contents = f.read()
        n.write(contents)

        n.close
        f.close
        while doEdit != "stop":
            doEdit = input("What would you like to do?")
            if doEdit == "clear":
                n = open("HotdogsNew.txt", "w")
                n.write("")
                n.close
            if doEdit == "readline":
                line = int(input("Which line to read? "))
                while i < line:
                    f = open(r"C:\Users\s16475\Documents\GitHub\HotdogVendors\Hotdogs.txt", "r")
                    lines = f.readline()
                    i = i + 1
                print(lines)


    if do == "stop":
        f.close
        print("Stopping")
        stop = 1 # Whatever works I guess?