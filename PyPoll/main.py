import os
import csv

# Defining the path for input file
inputpath = os.path.join("Resources", "election_data.csv")

# Printing the header of the analysis
print("Election Results")
print('---------------------------------')


# Calculating total votes
with open(inputpath, "r") as inputfile:
    reader = csv.reader(inputfile, delimiter =",")
    header = next(reader)
    row_count = sum(1 for row in reader)
    print(f"Total Votes: {row_count}")
    print('---------------------------------')


# Generating a list of all candidates in the election
with open(inputpath, "r") as inputfile:
    reader = csv.reader(inputfile, delimiter =",")
    header = next(reader)
    cand_list = []
    for row in reader:
        cand = row[2]
        cand_list.append(cand)

# Counting the number of votes for each candidate
# Converting the counter into a dictionary
import collections
counter=collections.Counter(cand_list)
dictionary = dict(counter)


# Defining the keys and values to be pulled from the dictionary
first_key = list(dictionary)[0]
first_value = list(dictionary.values())[0]

second_key = list(dictionary)[1]
second_value = list(dictionary.values())[1]

third_key = list(dictionary)[2]
third_value = list(dictionary.values())[2]

fourth_key = list(dictionary)[3]
fourth_value = list(dictionary.values())[3]

# Calculating percentage for Khan
# Even though I rounded the number for 3 decimals, for some reason it was rounded to 1 decimal
first_perc = first_value / row_count * 100
first_perc = round(first_perc, 3)


# Calculating percentage for Correy
# Even though I rounded the number for 3 decimals, for some reason it was rounded to 1 decimal
second_perc = second_value / row_count * 100
second_perc = round(second_perc, 3)


# Calculating percentage for Li
# Even though I rounded the number for 3 decimals, for some reason it was rounded to 1 decimal
third_perc = third_value / row_count * 100
third_perc = round(third_perc, 3)


# Calculating percentage for O'Tooley
# Even though I rounded the number for 3 decimals, for some reason it was rounded to 1 decimal
fourth_perc = fourth_value / row_count * 100
fourth_perc = round(fourth_perc, 3)


# Printing percentage of votes and total number of votes for each candidate
print(f"{first_key}: {first_perc}% ({first_value})")
print(f"{second_key}: {second_perc}% ({second_value})")
print(f"{third_key}: {third_perc}% ({third_value})")
print(f"{fourth_key}: {fourth_perc}% ({fourth_value})")
print('---------------------------------')

# Pulling the winner's name from the dictionary
max_key = max(dictionary, key=dictionary.get)

# Printing the winner
print(f"Winner: {max_key}")
print('---------------------------------')


# Creating an Analysis.txt file using the data I generated
f = open("Analysis.txt", "w")
f.write(f"Election Results \n--------------------------------- \nTotal Votes: {row_count} \n--------------------------------- \n{first_key}: {first_perc}% ({first_value}) \n{second_key}: {second_perc}% ({second_value}) \n{third_key}: {third_perc}% ({third_value}) \n{fourth_key}: {fourth_perc}% ({fourth_value}) \n--------------------------------- \nWinner: {max_key} \n---------------------------------")
f.close()

# Moving the Analysis.txt file into Analysis folder
import shutil

source = "Analysis.txt"
destination = "Analysis"

new_path = shutil.move(source, destination)


