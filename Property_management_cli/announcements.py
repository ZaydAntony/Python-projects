import json
import os

file_path = "./Property_management_cli/announcements.json"

print("-------------------🏡 Welcome to your property manager 🏡------------------")


class Announcements:
    def get_announcement(self):
        self.title = str(input("Enter announcement title: "))
        while True:
            if self.title == "":
                print("Title cannot be blank")
                self.title = input("Enter announcement title: ")
            else:
                break
            
        self.description = input("Enter a short description: ")
        while True:
            if self.description == "":
                print("Description cannot be blank")
                self.description = input("Enter a short description: ")
            else:
                break
        self.date = input("Enter date in the form of (DD:MM:YY): ")
        while True:
            if self.date == "":
                print("Date cannot be blank")
                self.date = input("Enter date in the form of (DD:MM:YY): ")
            else:
                break

        
        return {
            "title": self.title,
            "description": self.description,
            "date": self.date
        }
        

def store_announcements(data):

    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            try:
                announcements = json.load(file)
            except:
                announcements = []
        announcements.append(data)
        with open(file_path, 'w') as file:
            json.dump(announcements,file, indent =4)
            print("Announcement added successfully 😀✅")
    else:
        print("File does not exist.")

anouncement = Announcements()
new_data = anouncement.get_announcement()
store_announcements(new_data)





