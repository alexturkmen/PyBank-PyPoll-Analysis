import os
import csv

# Defining the path for input file
inputpath = os.path.join("Resources", "budget_data.csv")

# Printing the header of the analysis
print("Financial Analysis")
print("----------------------------------")


# Calculating and printing total months
with open(inputpath) as inputfile:
    reader = csv.reader(inputfile, delimiter = ",")
    next(reader)
    row_count = sum(1 for row in reader)
    print(f"Total Months: {row_count}")
    

# Calculating and printing total
with open(inputpath) as inputfile:
    reader = csv.reader(inputfile, delimiter = ",")
    next(reader)
    totalpl = 0
    for row in reader:
        totalpl = totalpl + int(row[1])
    print(f"Total: ${totalpl}")


# Calculating average change
with open(inputpath) as inputfile:
    reader = csv.reader(inputfile, delimiter = ",")
    next(reader)

    # Creating empty lists to create lists for months and profit/losses
    list_pl = []
    list_months = []

    # Creating new lists for months and profits/losses
    for row in reader:
        list_pl.append(row[1])
        list_months.append(row[0])

    # Calculating average of changes, and at the same time creating a list for the changes
    total = 0
    length = len(list_pl)
    list_ch = []
    for item in range(1, length):
        x = int(list_pl[item]) - int(list_pl[item-1])
        total = total + x
        list_ch.append(x)
    average = total / (length - 1)
    average = round(average, 2)

    # Printing average of changes
    print(f"Average Change: ${average}")
    # Deleting the first month of the list to match the number of items in the list with the number of items in the list of changes
    # I can delete the first month because there is no change in first month anyway
    del list_months[0]
    
# Creating a dictionary to calculate Greatest Increase and Decrease in profits
zip_iterator = zip(list_months, list_ch)
dictionary = dict(zip_iterator)

# Calculating Greatest Increase in Profits and corresponding month
max_key = max(dictionary, key=dictionary.get)
all_values = dictionary.values()
max_value = max(all_values)

# Calculating Greatest Decrease in Profits and corresponding month
min_key = min(dictionary, key=dictionary.get)
all_values = dictionary.values()
min_value = min(all_values)

# Printing Greatest Increase and Decrease in Profits with corresponding months
print(f"Greatest Increase in Profits: {max_key} (${max_value})")
print(f"Greatest Decrease in Profits: {min_key} (${min_value})")


# Creating an Analysis.txt file using the data I generated
f = open("Analysis.txt", "w")
f.write(f"Financial Analysis \n-------------------------------------- \nTotal Months: {row_count} \nTotal: ${totalpl} \nAverage Change: ${average} \nGreatest Increase in Profits: {max_key} (${max_value}) \nGreatest Decrease in Profits: {min_key} (${min_value})")
f.close()

# Moving the Analysis.txt file into Analysis folder
import shutil

source = "Analysis.txt"
destination = "Analysis"

new_path = shutil.move(source, destination)

