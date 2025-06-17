cafe_menu = ["Mini Pizza", "Mini Burger", "Mini Sandwich", "Muffin", "Hot Chocolate", "Coffee", "Tea"]
stock = {
    "Mini Pizza": 10,
    "Mini Burger": 10,
    "Mini Sandwich": 10,
    "Muffin": 10,
    "Hot Chocolate": 10,
    "Coffee": 10,
    "Tea": 10
}

price = {
    "Mini Pizza": 30,
    "Mini Burger": 30,
    "Mini Sandwich": 30,
    "Muffin": 10,
    "Hot Chocolate": 15,
    "Coffee": 7,
    "Tea": 5
}

total_stock = 0

for item in cafe_menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

print(f"The total stock worth in the café is: R{total_stock:.2f}")
