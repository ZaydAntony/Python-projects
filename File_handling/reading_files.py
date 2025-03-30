import json
import csv


# In this section we will get to take a look at reading files using python

#A txt file
path = "./input.txt";

with open(path, "r") as file:
    content = file.read()
    print(content)
# prints out whatever we wrote in our input.txt file


#A Json file

file_path = "./input.json"

with open(file_path, "r") as file:
    output = json.load(file)
    print(output)

    # prints out a dictionary of the content in input.json

# A csv file

csv_path = "./input.csv"

with open(csv_path, "r") as file:
    content = csv.reader(file)

    for line in content:
        print(line);