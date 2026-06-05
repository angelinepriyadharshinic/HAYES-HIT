menu = {
    "Zinger Burger": 200,
    "Pizza": 150,
    "Loaded Fries": 120,
    "French Fries": 90,
    "Coke": 40,
    "Sprite": 40,
    "Extra Dip": 3
}

cart = []
total = 0

while True:
    print("\n===== HAYES HIT =====")
    print("1. View Menu")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n----- MENU -----")
        for item, price in menu.items():
            print(f"{item} - ₹{price}")

    elif choice == "2":
        print("\n----- MENU -----")
        for item, price in menu.items():
            print(f"{item} - ₹{price}")

        food = input("\nEnter food name exactly as shown: ")

        if food in menu:
            cart.append(food)
            total += menu[food]
            print(food, "added to cart!")
        else:
            print("Item not found.")

    elif choice == "3":
        if len(cart) == 0:
            print("\nYour cart is empty.")
        else:
            print("\n----- YOUR CART -----")
            for item in cart:
                print(item, "- ₹", menu[item])

            print("Total: ₹", total)

    elif choice == "4":
        if len(cart) == 0:
            print("\nYour cart is empty.")
        else:
            print("\n----- BILL -----")
            for item in cart:
                print(item, "- ₹", menu[item])

            print("Total Amount: ₹", total)

            confirm = input("Confirm Order (yes/no): ")

            if confirm.lower() == "yes":
                print("\n✅ Order Placed Successfully!")
                print("Thank you for ordering from HAYES HIT!")

                cart.clear()
                total = 0
            else:
                print("Order Cancelled.")

    elif choice == "5":
        print("Thank you for visiting HAYES HIT!")
        break

    else:
        print("Invalid choice. Please try again.")
