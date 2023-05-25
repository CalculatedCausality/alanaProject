import json
import os
import unittest

from store import Store


class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store('inventory.json')

    def test_initialize_inventory(self):
        with open('inventory.json', 'r') as f:
            inventory = json.load(f)
        self.assertEqual(inventory, self.store.inventory)

    def test_add_item_to_cart(self):
        self.store.add_item_to_cart('apple', 5)
        self.assertEqual(self.store.cart['apple'], 5)

    def test_checkout(self):
        self.store.add_item_to_cart('apple', 5)
        self.store.checkout()
        self.assertEqual(self.store.cart, {})

    def test_update_inventory_file(self):
        self.store.add_item_to_cart('apple', 5)
        self.store.update_inventory_file('inventory.json')
        with open('inventory.json', 'r') as f:
            updated_inventory = json.load(f)
        self.assertEqual(updated_inventory, self.store.inventory)


if __name__ == "__main__":
    unittest.main(exit=False)
