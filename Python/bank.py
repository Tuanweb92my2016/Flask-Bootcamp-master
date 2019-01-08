class Book(object):
    """docstring fs Book."""
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):

        # return f"Title: {self.title}, Author: {self.author}"
        return "YEp!"

    def __len__(self):
        return self.pages

    

mybook = Book("Python Rocks!",'Jose',250)
length_book = len(mybook)
print(mybook)
print(length_book)
