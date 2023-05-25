import json


class Store:
    def __init__(self, inventory_file):
        self.inventory = self.initialize_inventory(inventory_file)
        self.cart = {}

    def initialize_inventory(self, inventory_file):
        with open(inventory_file, 'r') as f:
            return json.load(f)

    def display_stock_in_aisle(self, aisle):
        for item, details in self.inventory.items():
            if details['aisle'] == aisle:
                print(
                    f"{item}: {details['price']}, {details['inventory']} in stock")

    def add_item_to_cart(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name]['inventory'] >= quantity:
                self.inventory[item_name]['inventory'] -= quantity
                if item_name in self.cart:
                    self.cart[item_name] += quantity
                else:
                    self.cart[item_name] = quantity
            else:
                print(f"Sorry, {item_name} is out of stock.")
        else:
            print(f"Sorry, {item_name} is not in the inventory.")

    def checkout(self):
        total_amount = 0
        print("Checkout Summary:")
        for item, quantity in self.cart.items():
            item_price = self.inventory[item]['price'] * quantity
            total_amount += item_price
            print(
                f"{item}: {quantity} x {self.inventory[item]['price']} = {item_price}")
        print(f"Total amount: {total_amount}")
        self.cart = {}

    def update_inventory_file(self, inventory_file):
        with open(inventory_file, 'w') as f:
            json.dump(self.inventory, f)
