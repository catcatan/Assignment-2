class Order:
    date = "March 12, 2023"
    status = "In transit"
    shopping_cart = "3 items in cart"
    delivery_address = "123 nowhere street"
    payment_method = "Credit Card"


    def validatePayment(self):
        print(f"Validating {self.payment_method} payment...")

    def cancel(self):
        print("Action canceled.")

    def dispatch(self):
        print(f"Parcel has been dispatched {self.date} to {self.delivery_address} and is now {self.status}.")

    def confirmDelivery(self):
        print("Delivery confirmed.")

    def refund(self):
        print("Purchase refunded.")

    def archive(self):
        print("Transaction has been archived.")


Odr = Order()

print()
Odr.validatePayment()
print()
Odr.cancel()
print()
Odr.dispatch()
print()
Odr.confirmDelivery()
print()
Odr.refund()
print()
Odr.archive()
