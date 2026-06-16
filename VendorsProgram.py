f = open(r"C:\Users\s16475\Documents\GitHub\HotdogVendors\Hotdogs.txt", "r") # opens the file (used the whole directory because was giving an error)
print("Welcome to the Hotdog Vendors program.")
do = input("What do you want to do? Edit(e) Search(s) View(v)")
if do is "v":
    for i in f:
        contents = f.readline() # Reads a singular line from the file. The for loop will allow the whole file to be printed
        sec = contents.split(",")
        print("Name:\n" sec[1],"\n")
        print(sec)
f.close()