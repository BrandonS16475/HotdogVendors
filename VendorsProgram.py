stop = 2#
name = []
iD = []
dates =[]

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

        for i in f:
            contents = f.readline()
            sec = contents.split(",")

            iD.append(sec[0])
            name.append(sec[1])
            dates.append(sec[2])
        stype = input("what would you like to search for? Type name, iD, or dates")
        target = input("Enter search target: ")
        linearSearch(stype, target)

    if do == "stop":
        f.close
        print("Stopping")
        stop = 1 # Whatever works I guess?