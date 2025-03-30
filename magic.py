#learning magic methods

class Book:
    def __init__(self,title,author,pages):
        self.title = title;
        self.author = author;
        self.pages = pages;
    def __str__(self):
        return f"{self.title} by {self.author}";
    def __eq__(self, other):
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False
    def __add__(self,other):
        return self.pages + other.pages;
book1=Book("The caucasian cycle", "A.Smith", 250);
book2=Book("The caucasian cycle", "A.Smith", 250);
book3=Book("Kigogo", "k.Mziza", 150);

print(book1 + book3);


