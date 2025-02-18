# Initialize an empty dictionary to store items and their quantities
cart = {}

# Continuously prompt the user for commands until they decide to quit
while True:
    # Read user input, split it by spaces, and unpack the first element as command and the rest as item details
    command, *item = input().split()

    # Define the commands dictionary, mapping each command string to a lambda function with the desired behavior
    commands = {
        "add": lambda: (
            # Adds an item to the cart or updates its quantity
            cart.update({item[0]: cart.get(item[0], 0) + int(item[1])}),
            print(f"{item[0]}: {cart[item[0]]}"),
        ),
        "remove": lambda: (
            # Removes an item from the cart if it exists, otherwise notifies the user
            print(f"{item[0]}: {cart.pop(item[0])}")
            if item[0] in cart
            else print("Item not found")
        ),
        "show": lambda: (
            # Displays all items in the cart in a sorted manner, or notifies if the cart is empty
            print(", ".join(f"{key}: {value}" for key, value in sorted(cart.items())))
            if cart
            else print("Cart is empty")
        ),
        "quit": lambda: exit(),  # Exits the program
    }

    # Execute the function associated with the provided command
    commands[command]()
