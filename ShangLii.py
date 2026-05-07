# ShangLii Restaurant Ordering System

menu = {
    "Noodles": 5.00,
    "Spring Rolls": 4.00,
    "Dumplings": 4.50,
    "Sticky Rice": 2.50,
    "Curry Soup": 2.00
}

cart = []


def show_menu():
    print("\n--- MENU ---")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")


def show_cart():
    print("\n--- YOUR CART ---")
    if not cart:
        print("Cart is empty.")
        return

    total = 0
    for item in cart:
        print(f"{item} - ${menu[item]:.2f}")
        total += menu[item]

    tax = total * 0.15
    final_total = total + tax

    print(f"\nSubtotal: ${total:.2f}")
    print(f"15% Added: ${tax:.2f}")
    print(f"Total: ${final_total:.2f}")


def add_to_cart():
    item = input("Enter item to add: ").title()
    if item in menu:
        cart.append(item)
        print(f"{item} added to cart.")
    else:
        print("Item not found.")


def remove_from_cart():
    item = input("Enter item to remove: ").title()
    if item in cart:
        cart.remove(item)
        print(f"{item} removed from cart.")
    else:
        print("Item not in cart.")


def main():
    while True:
        print("\n--- RESTAURANT SYSTEM ---")
        print("1. Show Menu")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            show_cart()
        elif choice == "5":
            print("Thank you for your order!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()