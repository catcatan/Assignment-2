class ShoppingCart:
    list_of_items = ['i9 Intel CPU', '8GB RAM', 'SSD']
    deliveryFees = 120
    discount = 200
    total_amount = 10000.00


    def addItem(self):
        item = input("What item name to add to shopping cart?: ")
        self.list_of_items.append(item)
        for item in self.list_of_items:
            print(item)

    def removeItem(self):
        index = int(input("What item number to remove from cart?: "))
        self.list_of_items.pop(index - 1)
        for item in self.list_of_items:
            print(item)

    def selectDeliveryOption(self):
        print("Delivery Options:")
        delv_opt = input("1. Door-to-Door or 2. Pick up from location?: ")
        print()
        if delv_opt == "1":
            print(f"You have chosen Door-to-Door delivery.")
        elif delv_opt == "2":
            print("You have chosen Pick up from location delivery")
        else:
            print("Not an option.")
            self.selectDeliveryOption()

    def applyDiscount(self):
        print(f"{self.discount} peso discount was applied.")


    def calculateTotal(self):
        print(f"Your total amount is {self.total_amount} pesos.")


    def checkout(self):
        print("Shopping cart checked out.")


SH = ShoppingCart()

print()
SH.addItem()
print()
SH.removeItem()
print()
SH.selectDeliveryOption()
print()
SH.applyDiscount()
SH.calculateTotal()
SH.checkout()
