Here’s a `README.md` description you can use for your project:

---

# 🛒 Flash Sale Management System

This is a simple terminal-based product inventory and shopping cart management system that supports both **Authority** and **Buyer** roles. The program allows an **Authority** to manage products, set flash sales, and apply coupon codes, while **Buyers** can view products, participate in flash sales, apply coupons, and place orders.

---

## 🚀 Features

### 👤 Authority

* Secure login (`username: authority`, `password: authoritypassword`)
* Add and delete products
* View all inventory (regular and flash sale items)
* Set and manage coupon codes (with start and end dates)
* Configure flash sales for specific products (with discount, start, and end dates)

### 🛍️ Buyer

* Login with one of 10 pre-defined buyer accounts
* View available products
* View current flash sales
* Add products to cart (inventory-aware)
* Apply valid coupon codes
* Place an order with optional discount if coupon is active

---

## 🗂️ Structure

* **Product**: Represents an item with code, name, quantity, and price.
* **Authority**: Admin responsible for inventory and sales setup.
* **Buyer**: A customer who can browse and purchase products.
* **Flash Sales**: Time-limited discounts on specific products.
* **Coupon Code**: Discount code valid during a specified date range.

---

## 🧪 Example Buyer Logins

```bash
buyer1 / buyerpassword1
buyer2 / buyerpassword2
...
buyer10 / buyerpassword10
```

---

## 🛠️ How to Use

1. Run the script in a Python environment.
2. Choose between Authority or Buyer from the main menu.
3. As Authority, manage the product catalog and set discounts.
4. As a Buyer, view available items, add to cart, and place orders.

---

## 📅 Date Handling

Flash sales and coupon codes are date-sensitive:

* Format: `YYYY-MM-DD`
* Validity checked against the current system date using `datetime.date.today()`

---

## 📌 Notes

* Cart updates inventory in real-time (quantity deducted on add).
* Discounts from flash sales are shown but not applied in price (demo purpose).
* Coupon discounts are applied on the final amount at checkout.

---

## ✅ Requirements

* Python 3.x
* No external libraries required

---

## 📄 License

This project is open-source and can be used for learning or extension purposes.

---

Let me know if you want this `README.md` in a downloadable file format or need a GUI/web-based version of the system!
