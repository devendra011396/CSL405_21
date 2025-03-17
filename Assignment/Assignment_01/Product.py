class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock}"


def add_product(products):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter initial stock quantity: "))
    products[name] = Product(name, price, stock)
    print("Product added successfully!\n")


def update_stock(products):
    name = input("Enter product name: ")
    if name in products:
        quantity = int(input("Enter quantity to add/remove (negative to remove): "))
        products[name].update_stock(quantity)
        print("Stock updated successfully!\n")
    else:
        print("Product not found!\n")


def display_product(products):
    name = input("Enter product name: ")
    if name in products:
        print(products[name])
    else:
        print("Product not found!\n")


def main():
    products = {}
    while True:
        print("\nStore Product Manager")
        print("1. Add a new product")
        print("2. Update stock of an existing product")
        print("3. Display product details")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_product(products)
        elif choice == "2":
            update_stock(products)
        elif choice == "3":
            display_product(products)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
