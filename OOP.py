# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def details(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

# Subclass inheriting from Book
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)  # Call parent constructor
        self.file_size = file_size  # New attribute for EBook

    # Overriding details() method to include file size
    def details(self):
        return super().details() + f", file size: {self.file_size}MB"

# Instantiate objects
book1 = Book("Learn Java programming", "Emilly Morrison", 281)
ebook1 = EBook("Think Python", "Allen Downey", 328, 1.5)

# Print details
print(book1.details())  # Output: 'Learn Java programming' by Emilly Morrison, 281 pages
print(ebook1.details())  # Output: 'Think Python' by Allen Downey, 328 pages, file size: 1.5MB



#ACTIVITY 2: POLYMORPHISM CHALLENGE

# Base class
class Animal:
    def move(self):
        pass  # Placeholder method (abstract behavior)

# Subclass for Birds
class Bird(Animal):
    def move(self):
        return "Flying in the sky "

# Subclass for Fish
class Fish(Animal):
    def move(self):
        return "Swimming in the water "

# Subclass for Mammals
class Mammal(Animal):
    def move(self):
        return "Walking or running on land "

# Instantiate objects
bird = Bird()
fish = Fish()
mammal = Mammal()

# Call move() for each object
print(bird.move())  # Output: Flying in the sky 
print(fish.move())  # Output: Swimming in the water 
print(mammal.move())  # Output: Walking or running on land 
