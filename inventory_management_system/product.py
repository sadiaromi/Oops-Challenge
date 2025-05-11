from abc import ABC, abstractmethod
from datetime import date

class Product(ABC):
    def __init__(self, product_id, name, price, quantity_in_stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    def restock(self, amount):
        self._quantity_in_stock += amount

    def sell(self, quantity):
        if quantity > self._quantity_in_stock:
            raise ValueError("Not enough stock to sell.")
        self._quantity_in_stock -= quantity

    def get_total_value(self):
        return self._price * self._quantity_in_stock

    @abstractmethod
    def __str__(self):
        pass

    def to_dict(self):
        return {
            "product_id": self._product_id,
            "name": self._name,
            "price": self._price,
            "quantity_in_stock": self._quantity_in_stock,
            "type": self.__class__.__name__
        }

class Electronics(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, brand, warranty_years):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._brand = brand
        self._warranty_years = warranty_years

    def __str__(self):
        return f"[Electronics] {self._name} by {self._brand}, Warranty: {self._warranty_years} yrs, Stock: {self._quantity_in_stock}"

    def to_dict(self):
        data = super().to_dict()
        data.update({"brand": self._brand, "warranty_years": self._warranty_years})
        return data

class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._expiry_date = expiry_date  # YYYY-MM-DD format

    def is_expired(self):
        return date.today() > date.fromisoformat(self._expiry_date)

    def __str__(self):
        status = "EXPIRED" if self.is_expired() else "Valid"
        return f"[Grocery] {self._name}, Expiry: {self._expiry_date} ({status}), Stock: {self._quantity_in_stock}"

    def to_dict(self):
        data = super().to_dict()
        data.update({"expiry_date": self._expiry_date})
        return data

class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._size = size
        self._material = material

    def __str__(self):
        return f"[Clothing] {self._name}, Size: {self._size}, Material: {self._material}, Stock: {self._quantity_in_stock}"

    def to_dict(self):
        data = super().to_dict()
        data.update({"size": self._size, "material": self._material})
        return data
