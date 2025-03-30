import json
import csv


#We are gonna work with Writing files using python

# a txt file(plain text)

txt_file_path = "./input.txt";
text = "Python is a good language to start with";

with open (txt_file_path, "w") as file:
    file.write(text);
    print(f"Your file {txt_file_path} has been created");



# a json file

json_file_path = "./input.json"

employees = {
    "Manager": "Mr.Krabs",
    "Cook": "Spongebob Squarepants",
    "Accountant": "Squidward"
}

with open(json_file_path, "w") as file:
    json.dump(employees, file, indent = 4);
    print(f"The file {json_file_path} has been created");

# A csv file

csv_file_path = "./input.csv"

students = [["Name", "Age", "Course"],
            ["Zayd", 22, "BDS"],
            ["Zamzam", 22, "BSD"]]

with open(csv_file_path, "w") as file:
    writer = csv.writer(file);

    for row in students:
        writer.writerow(row)
    print(f"The file {csv_file_path} has been created")

