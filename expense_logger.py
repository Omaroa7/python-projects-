# 
total = 0

while True:
    item = input("Enter item ( or 'q' to quit): ")
    if item.lower() == "q":
        break

    price = float(input("Enter price: "))
    total += price

    with open("expenses.txt", "a") as file:
        file.write(f"{item}: £{price}")

    print(f"\nTotal spent: {total:.2f}")
    print("Your expenses have been saved to expenses.txt")


