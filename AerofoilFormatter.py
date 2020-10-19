# Program to convert coordinates from airfoiltools.com to an acceptable format for ANSYS DesignModeller.

# Required library.
import os

# Clear the screen.
os.system('cls')

# Help section.
print("v1.5.1.0")
print("\nThis is a tool for converting 4-digit NACA aerofoil coordinates from airfoiltools.com.\n\
Make sure that the shape has a closed trailing edge.\n\
Copy everything from the text box on that website (including the information on the first line)\n\
and paste into a plain-text file before using this program.\n\n\
Drag and drop that file here. Alternatively, enter the file path manually.\n\
The output will not be a closed shape. You must do that yourself in ANSYS.\n")

# Define path to coordinates file.
path = input("> Enter file path: ")

# Read file
while True:
    try: 
        if path[0] == ("\""):
            path = path.strip("\"")
        elif path[0] == ("\'"):
            path = path.strip("\'")

        with open(path, 'r') as f:
            content = [row.replace("\n","") for row in f]
            content.pop(0)
        break
    except:
        print("Invalid entry.\n")
        path = input("> Enter file path: ")
        continue

print("\nProcess complete.\n")

# Split the coordinates into x and y lists.
x_coords = [x.replace(" ","")[:8] for x in content]
y_coords = [y.split(" ")[-1] for y in content]

# Remove final coordinates as it is a duplicate of the first element.
del x_coords[-1]
del y_coords[-1]

# Write to file.
name = input("> Save as: ")
name = name + ".txt"
with open(name, 'w') as f:
    if name[0] == ("\""):
        name = name.strip("\"")
    elif name[0] == ("\'"):
        name = name.strip("\'")
    f.write("#Group" + " "*3 + "Point" + " "*8 + "X" + " "*15 + "Y" + " "*15 + "Z\n")
    for i in range(len(x_coords)):
        f.write("1        " + str(i+1) + " "*8 + x_coords[i] + " "*8 + y_coords[i] + "        0.000000\n")
print("Done.\n")

close = input("Press \"enter\" to close the program.")
