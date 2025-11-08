items = {
    'mandazi': 30,
    'chapati': 20,
    'juice': 10,
    'rice': 50
}

record = {}
total = 0

while True:
    print("Available items: mandazi, chapati, juice, rice")
    item = input("Enter the item name (or 'exit' to quit): ").lower()
    if item == 'exit':
        break

    if item not in items:
        print("Item not found. Please enter a valid item.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            continue

        price = items[item]
        total_price = price * quantity
        print(f"Total price for {quantity} {item}: {total_price}")

        amount_paid = int(input("Enter the amount paid: "))
        if amount_paid < total_price:
            print("Amount paid is less than total price. Please pay the full amount.")
            continue

        change = amount_paid - total_price
        print(f"The change is {change}")

        # Update record and total
        record[item] = record.get(item,0) + total_price
        total = total + total_price
        print(f"Record so far: {record}")
        print(f"Total amount for all items: {total}")

    except ValueError:
        print("Invalid input. Please enter positive numbers only.")
