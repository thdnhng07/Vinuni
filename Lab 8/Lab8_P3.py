cart = {}

while True:
    command, *item = input().split()

    commands = {
        "add": lambda: (
            cart.update({item[0]: cart.get(item[0], 0) + int(item[1])}),
            print(f'{item[0]}: {cart[item[0]]}')),
        "remove": lambda: (
            print(f"{item[0]}: {cart.pop(item[0])}")
            if item[0] in cart
            else print("Item not found")
        ),
        "show": lambda: (
            print(", ".join(f"{key}: {value}" for key, value in sorted(cart.items())))
            if cart
            else print("Cart is empty")
        ),
        "quit": lambda: exit(),
    }

    commands[command]()


