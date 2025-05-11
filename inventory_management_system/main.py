from inventory import Inventory
from product import Electronics, Grocery, Clothing
from exceptions import *

def main():
    inventory = Inventory()

    while True:
        print("\n=== Inventory Menu ===")
        print("1. Add Product")
        print("2. Sell Product")
        print("3. View Products")
        print("4. Save to File")
        print("5. Total Inventory Value")
        print("6. Remove Expired Groceries")
        print("7. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                type_ = input("Enter product type (electronics/grocery/clothing): ").lower()
                pid = input("ID: ")
                name = input("Name: ")
                price = float(input("Price: "))
                qty = int(input("Quantity: "))

                if type_ == "electronics":
                    brand = input("Brand: ")
                    warranty = int(input("Warranty (years): "))
                    p = Electronics(pid, name, price, qty, brand, warranty)

                elif type_ == "grocery":
                    expiry = input("Expiry Date (YYYY-MM-DD): ")
                    p = Grocery(pid, name, price, qty, expiry)

                elif type_ == "clothing":
                    size = input("Size: ")
                    material = input("Material: ")
                    p = Clothing(pid, name, price, qty, size, material)

                else:
                    print("Unknown type.")
                    continue

                inventory.add_product(p)
                print("Product added.")

            elif choice == "2":
                pid = input("Enter product ID to sell: ")
                qty = int(input("Quantity: "))
                inventory.sell_product(pid, qty)
                print("Product sold.")

            elif choice == "3":
                for p in inventory.list_all_products():
                    print(p)

            elif choice == "4":
                inventory.save_to_file("data.json")
                print("Inventory saved.")

            elif choice == "5":
                print(f"Total Inventory Value: {inventory.total_inventory_value()}")

            elif choice == "6":
                inventory.remove_expired_products()
                print("Expired products removed.")

            elif choice == "7":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
