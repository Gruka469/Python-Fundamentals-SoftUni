products_info = {}

while True:
    product_data = input()
    if product_data == "buy":
        break
    
    name, price, quantity = product_data.split()
    price = float(price)
    quantity = int(quantity)

    if name in products_info:
        # Product already exists, update its price and quantity
        products_info[name]['price'] = price
        products_info[name]['quantity'] += quantity
    else:
        # Product doesn't exist yet, add it with its price and quantity
        products_info[name] = {'price': price, 'quantity': quantity}

for name, info in products_info.items():
    total_price = info['price'] * info['quantity']
    print(f"{name} -> {total_price:.2f}")