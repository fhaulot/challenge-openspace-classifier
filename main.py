

# Connect main with the others modules
from utils.openspace import Openspace

# Import library to make calculation
import math
from utils.table import Table

# Request the user to indicate the path to the file with the attendants list
#path = input("Please specify the file patch with the list of attendants:")
path = "C:/Users/bljor/OneDrive/Documents/GitHub/colleagues.csv"

# Initiate a list to include all attendants in the file
names = []

# Read the file and save the attendants
with open(path, "r") as my_file:
    n = my_file.read().split("\n")
    names.extend(n)

# Check the number of attendants input
seats = len(names)

# Check the quantity of tables needed based on 4 people per table
qty = math.ceil(seats/4)

# Create the tables in main
tables = [Table(4) for t in range(qty)]

print(tables)
# Summarise the input
# print(f"\nThank you! Your file includes {seats} attendants.\n\nHere is the list:")
# print(*names, sep ='\n')

# Call the different methods that will set the class organisation
# Create an Openspace object
#space = Openspace(tables)

# Set all attendants to their seats
#Openspace.organize(names)

# Show the seating layout
#Openspace.display()

# Save the layout to Excel in active directory
#Openspace.store("seating_arrangement.xlsx")

