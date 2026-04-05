menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

#Task 1

# Group menu by category
print("\n===== FULL MENU =====")

categories = set(item["category"] for item in menu.values())

for category in categories:
    print(f"\n===== {category} =====")
    
    for item, details in menu.items():
        if details["category"] == category:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{item} - ₹{details['price']:.2f} [{status}]")

# Dictionary calculations

# Total number of items
total_items = len(menu)

# Total available items
available_items = sum(1 for item in menu.values() if item["available"])

# Most expensive item
most_expensive = max(menu.items(), key=lambda x: x[1]["price"])

# Items under ₹150
under_150 = [(item, details["price"]) for item, details in menu.items() if details["price"] < 150]

# Print results
print("\n--- MENU ANALYSIS ---")
print("Total items:", total_items)
print("Available items:", available_items)

print(f"Most expensive item: {most_expensive[0]} - ₹{most_expensive[1]['price']}")

print("\nItems under ₹150:")
for item, price in under_150:
    print(f"{item} - ₹{price}")

#Task 2

cart = []

# Function to print the cart
def print_cart():
    print("\nCurrent Cart:")
    if not cart:
        print("Cart is empty")
    for item in cart:
        print(f"{item['item']} x{item['quantity']} - ₹{item['price'] * item['quantity']}")


# 1 Add item
def add_to_cart(item_name, quantity):
    if item_name not in menu:
        print(f"{item_name} does not exist in menu")
        return
    
    if not menu[item_name]["available"]:
        print(f"{item_name} is unavailable")
        return

    # Check if already in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"Updated {item_name} quantity to {item['quantity']}")
            return

    # Add new item
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })
    print(f"Added {item_name} x{quantity}")


# 2 Remove item
def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"Removed {item_name}")
            return
    print(f"{item_name} not in cart")


# 3 Update quantity
def update_quantity(item_name, quantity):
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] = quantity
            print(f"Updated {item_name} to {quantity}")
            return
    print(f"{item_name} not in cart")


# Simulation

add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)  # should become 3
print_cart()

add_to_cart("Mystery Burger", 1)
print_cart()

add_to_cart("Chicken Wings", 1)
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()


#Order Summary 

print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    total_price = item["price"] * item["quantity"]
    subtotal += total_price
    print(f"{item['item']} x{item['quantity']} - ₹{total_price:.2f}")

gst = subtotal * 0.05
total = subtotal + gst

print("----------------------------------")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (5%): ₹{gst:.2f}")
print(f"Total Payable: ₹{total:.2f}")
print("==================================")

#Task 3 

import copy

# 1: Deep copy
inventory_backup = copy.deepcopy(inventory)

# Change the original to prove that backup is safe
inventory["Paneer Tikka"]["stock"] = 0

print("\nInventory Changed:")
print("Current:", inventory["Paneer Tikka"])
print("Backup:", inventory_backup["Paneer Tikka"])

# Restore
inventory = copy.deepcopy(inventory_backup)


# 2: Deduct stock based on cart
print("\n--- Deducting Inventory ---")

for cart_item in cart:
    item_name = cart_item["item"]
    qty_needed = cart_item["quantity"]

    stock_available = inventory[item_name]["stock"]

    if stock_available >= qty_needed:
        inventory[item_name]["stock"] -= qty_needed
    else:
        print(f"Warning: Only {stock_available} {item_name} available")
        inventory[item_name]["stock"] = 0


# 3: Reorder alert
print("\n--- Reorder Alerts ---")

for item, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"⚠ {item} low stock: {details['stock']} left (reorder at {details['reorder_level']})")


# 4 :Print both inventories
print("\n--- Final Inventory ---")
print(inventory)

print("\n--- Backup Inventory ---")
print(inventory_backup)


#Task 4

print("\n===== DAILY REVENUE =====")

# 1: Revenue per day
daily_revenue = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(f"{date}: ₹{total:.2f}")

# 2: Best-selling day
best_day = max(daily_revenue, key=daily_revenue.get)
print(f"\nBest Selling Day: {best_day} (₹{daily_revenue[best_day]:.2f})")

# 3: Most ordered item
item_count = {}

for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

most_ordered = max(item_count, key=item_count.get)
print(f"Most Ordered Item: {most_ordered}")


# 4: Add new day
sales_log["2025-01-05":] [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]


print("\n===== UPDATED REVENUE =====")

# Recalculate revenue
daily_revenue = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(f"{date}: ₹{total:.2f}")

best_day = max(daily_revenue, key=daily_revenue.get)
print(f"\nUpdated Best Selling Day: {best_day} (₹{daily_revenue[best_day]:.2f})")


# 5:Numbered list of all orders
print("\n===== ALL ORDERS =====")

order_number = 1

for date, orders in sales_log.items():
    for order in orders:
        items = ", ".join(order["items"])
        print(f"{order_number}. [{date}] Order #{order['order_id']} - ₹{order['total']:.2f} - Items: {items}")
        order_number += 1

