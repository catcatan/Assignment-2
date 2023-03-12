class Item:
    def __init__(self, code, title, description, category, picture, quantity_in_stock, price):
        self.code = code
        self.title = title
        self.description = description
        self.category = category
        self.picture = picture
        self.quantity_in_stock = quantity_in_stock
        self.price = price

    def __repr__(self):
        return f'Code: {self.code}, Title: {self.title}, Description: {self.description}, ' \
               f'Category: {self.category}, Picture: {self.picture}, Stock: {self.quantity_in_stock},' \
               f' Price: {self.price}'

    def viewFullDescription(self, obj):
        print(obj)

    def addToCart(self, obj):
        print(f"{obj} added to cart.")

    def updateStockLevel(self):
        print('Stock Updated.')


print()

# Item Object
my_item = Item(1101, 'Ink Pen', 'Used for writing', 'Item', 'pen.png', 378, 15.00)

my_item.viewFullDescription(my_item)
my_item.addToCart("Item")
my_item.updateStockLevel()

print()
print()


class DVD(Item):
    def __init__(self, code, title, description, category, picture, quantity_in_stock, price, director, certificate, list_of_actors):
        super().__init__(code, title, description, category, picture, quantity_in_stock, price)
        self.director = director
        self.certificate = certificate
        self.list_of_actors = list_of_actors

    def __repr__(self):
        return f'{super().__repr__()}, Director: {self.director}, Certificate: {self.certificate}, List of Actors: {self.list_of_actors}'


# DVD Object
my_dvd = DVD(1234, 'Avatar', '[movie description]', 'DVD', 'dvdcover.jpeg', 50, 2000.00, 'James Cameron', 'certificate.pdf', ['Zoë Saldana', 'Sam Worthington', 'Sigourney Weaver'])

my_item.viewFullDescription(my_dvd)
my_item.addToCart("DVD")
my_item.updateStockLevel()

print()
print()


class MP3(Item):
    def __init__(self, code, title, description, category, picture, quantity_in_stock, price, duration, artist):
        super().__init__(code, title, description, category, picture, quantity_in_stock, price)
        self.duration = duration
        self.artist = artist

    def __repr__(self):
        return f'{super().__repr__()}, Duration: {self.duration}, Artist: {self.artist}'

    def playExtract(self):
        print("MP3 is playing")

    def download(self):
        print("MP3 is downloading")


# MP3 Object
my_mp3 = MP3(7854, 'Free Bird', '[song description]', 'MP3', 'freebird.png', 456, 500.00, '9 minutes and 7 seconds', 'Lynyrd Skynyrd')

my_item.viewFullDescription(my_mp3)
my_mp3.playExtract()
my_mp3.download()

my_item.addToCart("MP3")
my_item.updateStockLevel()

print()
print()


class Book(Item):
    def __init__(self, code, title, description, category, picture, quantity_in_stock, price, isbn, author, synopsis):
        super().__init__(code, title, description, category, picture, quantity_in_stock, price)
        self.isbn = isbn
        self.author = author
        self.synopsis = synopsis

    def __repr__(self):
        return f'{super().__repr__()}, ISBN: {self.isbn}, Author: {self.author}, Synopsis: {self.synopsis}'

    def preview(self):
        print("Previewing...")


# Book Object
my_book = Book(546495, 'Harry Potter', '[book description]', 'Book', 'harry_potter.png', 90, 10000.00, '978-0439708180', 'J.K. Rowling', '[book synopsis]')

my_item.viewFullDescription(my_book)
my_book.preview()

my_item.addToCart("Book")
my_item.updateStockLevel()
