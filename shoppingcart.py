def get_order():
    print("[command] [item] (commands are: a to add, d to delete, q to quit) ")
    line = input()

    command = line[:1]
    item = line[2:]

    return command, item

def add_to_cart(item, cart):
    if not item in cart:
        cart[item] = 0
    cart[item] += 1

def delete_from_cart(item, cart):
    if item in cart:
        cart[item] -= 1


def process_order(order, cart):
    command, item = order

    if command == "a":
        add_to_cart(item, cart)
        print("You've added "+(item)+ " to your cart!")
    elif command == "d" and item in cart:
        delete_from_cart(item, cart)
        print("You've taken "+(item)+ " out of your cart!")
    elif command == "d" and item not in cart:
        print("That's not in your cart!")
    elif command == "q":
        return False

    return True

def go_shopping():
    cart = dict()

    while True:
        order = get_order()
        if not process_order(order, cart):
            break
        
    

    print ("You bought:")
    print (cart)



go_shopping()
