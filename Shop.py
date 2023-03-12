class Shop:
    name = "Catcatan Mart"
    description = "[shop description]"
    list_of_categories = ['Item', 'DVD', 'MP3', 'Book']
    list_of_items = ['Pen', 'Avatar DVD', 'Freebird.mp3', 'Harry Potter Book']
    URL = "https://catcatan-mart.com/shop"

    def viewCategory(self):
        print("Categories:")
        for category in self.list_of_categories:
            print(category)

    def searchItems(self):
        print("Searching for item...")

    def viewItems(self):
        print("Items:")
        for item in self.list_of_items:
            print(item)

    def viewShoppingCart(self):
        print("Viewing shopping cart.")


Sp = Shop()

print()
Sp.viewCategory()
print()
Sp.searchItems()
print()
Sp.viewItems()
print()
Sp.viewShoppingCart()
