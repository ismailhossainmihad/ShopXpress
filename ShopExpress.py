import datetime

class Product:
    def __init__(self, code, name, quantity, price):
        self.code = code
        self.name = name
        self.quantity = quantity
        self.price = price
        self.is_flash_sale = False


class Authority:
    def __init__(self):
        self.products = []
        self.coupon_code = ""
        self.coupon_discount = 0
        self.flash_sales = []

    def login(self):
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username == "authority" and password == "authoritypassword":
                print("Authority login successful.")
                break
            else:
                print("Invalid credentials. Please try again.")

    def show_inventory(self):
        print("-- Inventory --")
        print("Regular Products:")
        for product in self.products:
            if not product.is_flash_sale:
                print(f"Code: {product.code}, Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}")

        print("\nFlash Sale Products:")
        for flash_sale in self.flash_sales:
            product = flash_sale["product"]
            print(f"Code: {product.code}, Name: {product.name}, Quantity: {product.quantity}, "
                  f"Price: {product.price}, Discount: {flash_sale['discount']}%, "
                  f"Start Date: {flash_sale['start_date'].strftime('%Y-%m-%d')}, "
                  f"End Date: {flash_sale['end_date'].strftime('%Y-%m-%d')}")

        print("\n")

    def add_product(self, code, name, quantity, price):
        product = Product(code, name, quantity, price)
        self.products.append(product)
        print(f"Product {code} added successfully.")

    def delete_product(self, code):
        for product in self.products:
            if product.code == code:
                self.products.remove(product)
                print(f"Product {code} deleted successfully.")
                break
        else:
            print(f"Product {code} not found.")

    def set_coupon_code(self, coupon_code, discount, start_date, end_date):
        self.coupon_code = coupon_code
        self.coupon_discount = discount
        self.coupon_start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        self.coupon_end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        print(f"Coupon code '{coupon_code}' set successfully with {discount}% discount.")

    def set_flash_sale(self, code, discount, start_date, end_date):
        for product in self.products:
            if product.code == code:
                product.is_flash_sale = True
                flash_sale = {
                    "product": product,
                    "discount": discount,
                    "start_date": datetime.datetime.strptime(start_date, "%Y-%m-%d").date(),
                    "end_date": datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
                }
                self.flash_sales.append(flash_sale)
                print(f"Flash sale set for product {code} with {discount}% discount.")
                break
        else:
            print(f"Product {code} not found.")


class Buyer:
    def __init__(self):
        self.cart = []

    def login(self):
        username_passwords = {
            "buyer1": "buyerpassword1",
            "buyer2": "buyerpassword2",
            "buyer3": "buyerpassword3",
            "buyer4": "buyerpassword4",
            "buyer5": "buyerpassword5",
            "buyer6": "buyerpassword6",
            "buyer7": "buyerpassword7",
            "buyer8": "buyerpassword8",
            "buyer9": "buyerpassword9",
            "buyer10": "buyerpassword10"
        }

        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in username_passwords and username_passwords[username] == password:
                print("Buyer login successful.")
                break
            else:
                print("Invalid credentials. Please try again.")

    # Rest of the Buyer class code...


    def add_to_cart(self, code):
        for product in authority.products:
            if product.code == code:
                if product.quantity > 0:
                    self.cart.append(product)
                    product.quantity -= 1
                    print(f"Product {code} added to cart.")
                else:
                    print(f"No {product.name} available in the inventory.")
                break
        else:
            print(f"Product {code} not found.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Products in your cart:")
            for product in self.cart:
                print(f"Code: {product.code}, Name: {product.name}, Price: {product.price}")

    def show_product_list(self):
        print("-- Product List --")
        print("Available Products:")
        available_products = [product for product in authority.products if product.quantity > 0]
        if not available_products:
            print("No products available.")
        else:
            for product in available_products:
                print(f"Code: {product.code}, Name: {product.name}, Price: {product.price}")

    def show_flash_sale(self):
        print("-- Flash Sale --")
        for flash_sale in authority.flash_sales:
            product = flash_sale["product"]
            print(f"Code: {product.code}, Name: {product.name}, Price: {product.price}, "
                  f"Discount: {flash_sale['discount']}%, "
                  f"Start Date: {flash_sale['start_date'].strftime('%Y-%m-%d')}, "
                  f"End Date: {flash_sale['end_date'].strftime('%Y-%m-%d')}")

    def apply_coupon(self, coupon_code):
        if coupon_code == authority.coupon_code:
            current_date = datetime.date.today()
            if authority.coupon_start_date <= current_date <= authority.coupon_end_date:
                # Apply coupon code logic here
                print("Coupon applied successfully.")
            else:
                print("Coupon is not valid at the moment.")
        else:
            print("Invalid coupon code.")

    def place_order(self):
        if not self.cart:
            print("Your cart is empty. Please add products to the cart.")
        else:
            total_amount = sum(product.price for product in self.cart)
            if authority.coupon_code and authority.coupon_discount > 0:
                current_date = datetime.date.today()
                if authority.coupon_start_date <= current_date <= authority.coupon_end_date:
                    discount = total_amount * (authority.coupon_discount / 100)
                    total_amount -= discount
                    print("Coupon discount applied.")
                else:
                    print("Coupon is not valid at the moment. Full price will be charged.")

            print(f"Order placed successfully. Total amount: {total_amount}.")


authority = Authority()
buyer = Buyer()

while True:
    print("-- Menu --")
    print("1. Authority Login")
    print("2. Buyer Login")
    print("0. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        authority.login()
        while True:
            print("-- Authority Menu --")
            print("1. Show Inventory")
            print("2. Add Product")
            print("3. Delete Product")
            print("4. Set Coupon Code")
            print("5. Set Flash Sale")
            print("0. Logout")

            authority_choice = input("Enter the number of your choice: ")

            if authority_choice == "1":
                authority.show_inventory()
            elif authority_choice == "2":
                code = input("Enter the product code: ")
                name = input("Enter the product name: ")
                quantity = int(input("Enter the product quantity: "))
                price = float(input("Enter the product price: "))
                authority.add_product(code, name, quantity, price)
            elif authority_choice == "3":
                code = input("Enter the product code: ")
                authority.delete_product(code)
            elif authority_choice == "4":
                coupon_code = input("Enter the coupon code: ")
                discount = int(input("Enter the discount percentage: "))
                start_date = input("Enter the start date (YYYY-MM-DD): ")
                end_date = input("Enter the end date (YYYY-MM-DD): ")
                authority.set_coupon_code(coupon_code, discount, start_date, end_date)
            elif authority_choice == "5":
                code = input("Enter the product code: ")
                discount = int(input("Enter the discount percentage: "))
                start_date = input("Enter the start date (YYYY-MM-DD): ")
                end_date = input("Enter the end date (YYYY-MM-DD): ")
                authority.set_flash_sale(code, discount, start_date, end_date)
            elif authority_choice == "0":
                print("Logged out of the authority account.")
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        buyer.login()
        while True:
            print("-- Buyer Menu --")
            print("1. View Cart")
            print("2. Show Product List")
            print("3. Show Flash Sale")
            print("4. Apply Coupon")
            print("5. Add to Cart")
            print("6. Place Order")
            print("0. Logout")

            buyer_choice = input("Enter the number of your choice: ")

            if buyer_choice == "1":
                buyer.view_cart()
            elif buyer_choice == "2":
                buyer.show_product_list()
            elif buyer_choice == "3":
                buyer.show_flash_sale()
            elif buyer_choice == "4":
                coupon_code = input("Enter the coupon code: ")
                buyer.apply_coupon(coupon_code)
            elif buyer_choice == "5":
                code = input("Enter the product code: ")
                buyer.add_to_cart(code)
            elif buyer_choice == "6":
                buyer.place_order()
                break
            elif buyer_choice == "0":
                print("Logged out of the buyer account.")
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice == "0":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")