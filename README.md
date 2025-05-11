# 🧾 Inventory Management System (Python OOP + CLI)

A fully interactive and extensible Inventory Management System built using Python’s Object-Oriented Programming principles. It features product categorization, real-time stock operations, JSON persistence, custom exceptions, and a user-friendly CLI interface.

---

## 🗂 Project File Descriptions

### 📁 `product.py`
Defines the core structure of all products using OOP principles.

#### 🧱 Product (Abstract Base Class)
- Common attributes: `id`, `name`, `price`, `stock`
- Shared methods: 
  - `restock()`
  - `sell()`
  - `get_total_value()`
  - `__str__()`

#### 📺 Electronics (Subclass)
- Additional attributes: `brand`, `warranty_years`

#### 🥫 Grocery (Subclass)
- Additional attributes: `expiry_date`
- Method: `is_expired()` to check if the product is past its expiration

#### 👗 Clothing (Subclass)
- Additional attributes: `size`, `material`

Each subclass:
- Overrides `__str__()` for detailed display
- Supports JSON serialization via `to_dict()`

---

### 📁 `inventory.py`
Handles the inventory logic and product management.

#### Core Functions:
- ➕ `add_product()` — Adds new products, prevents duplicate IDs
- 📦 `list_all_products()` — Displays all inventory items
- 💰 `sell_product()` — Reduces stock and handles OutOfStockError
- 💵 `total_inventory_value()` — Calculates total inventory worth
- 🗑 `remove_expired_products()` — Removes only expired Grocery items
- 💾 `save_to_file()` — Persists inventory as JSON

✅ Internally uses a dictionary for fast ID-based access.

---

### 📁 `exceptions.py`
Defines custom exception classes for clearer error reporting.

- 🚫 `DuplicateProductIDError` — Raised when product ID already exists
- 📉 `OutOfStockError` — Raised when selling more items than available

---

### 📁 `main.py`
Entry point for the application — Command Line Interface.

#### 👨‍💻 Features:
- Menu-driven user interaction using `while` loop
- Add new products (`Electronics`, `Grocery`, `Clothing`)
- Sell existing products
- View full product list
- Total inventory value
- Remove expired groceries
- Save current inventory to JSON file
- Exit program

🎯 Designed for interactive use, simulating a real-world store workflow.

---

## ✅ Tech Stack
- Python 
- OOP principles
- `abc` module for abstraction
- JSON for persistence
- Custom exception handling

---

## ▶️ How to Run

```bash
python main.py

## ✉️ Feedback

We’d love to hear your thoughts!

If you find this project helpful or have any suggestions for improvement:

- ⭐ **Give it a star**
- 💡 **Suggest features or enhancements**

Your feedback keeps this project alive and evolving 🚀

