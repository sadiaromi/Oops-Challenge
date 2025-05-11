import json
from product import  Grocery
from exceptions import DuplicateProductIDError, OutOfStockError

class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product._product_id in self._products:
            raise DuplicateProductIDError("Product ID already exists.")
        self._products[product._product_id] = product

    def remove_product(self, product_id):
        if product_id in self._products:
            del self._products[product_id]

    def search_by_name(self, name):
        return [p for p in self._products.values() if name.lower() in p._name.lower()]

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if p.__class__.__name__.lower() == product_type.lower()]

    def list_all_products(self):
        return list(self._products.values())

    def sell_product(self, product_id, quantity):
        if product_id not in self._products:
            raise KeyError("Product ID not found.")
        try:
            self._products[product_id].sell(quantity)
        except ValueError:
            raise OutOfStockError("Insufficient stock.")

    def restock_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].restock(quantity)

    def total_inventory_value(self):
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        to_remove = [pid for pid, p in self._products.items() if isinstance(p, Grocery) and p.is_expired()]
        for pid in to_remove:
            del self._products[pid]

    def save_to_file(self, filename):
        data = [product.to_dict() for product in self._products.values()]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
