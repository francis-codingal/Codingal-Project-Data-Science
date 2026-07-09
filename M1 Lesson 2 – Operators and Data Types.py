#my Coffee Shop
item_name = "Espresso"
price = 3.25
quantity = 15
is_available = True

print("Item:", item_name)
print("Price: $", price)
print("In Stock:", quantity)
print("Available?", is_available)

print(type(item_name))
print(type(price))
print(type(quantity))
print(type(is_available))

total = price * quantity
print("Total value: $", total)
print("Sale price: $", price - 0.50)
print("Double stock:", quantity * 2)

print("Is price under $5?", price < 5)
print("More than 10 in stock?", quantity > 10)
print("Is price exactly $3.25?", price == 3.25)

shop_name = "Java" + " " + "Haven"
print("Shop name:", shop_name)
print("Letters in item name:", len(item_name))
print("First letter:", item_name[0])

price_a = 3.25
price_b = 4.50
print("Before:", price_a, "and", price_b)

temp = price_a
price_a = price_b
price_b = temp

print("After:", price_a, "and", price_b)