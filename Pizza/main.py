
def display_pizza():
    pizza_size = len(pizza_list)
    if pizza_size == 0:
        print("Pizza is empty! please add")
    else:
        print(f"List of Pizza ({pizza_size})!")
        for pizza in pizza_list:
            print(pizza)
def add_pizza(collection):
    new_pizza = input("What type of pizza would you like?")
    if not check_pizza_already_added(new_pizza, collection):
        pizza_list.sort(reverse=False, key=len)
        collection.insert(2, new_pizza)

    else:
        print(f"Pizza {new_pizza} already added!")

def check_pizza_already_added(new_entry,collection):
    for pizza in collection:
        if pizza.lower() == new_entry.lower():
            return True
    return False


pizza_list = ["FPizza 11","GPizza 2","APizza 355","CPizza 47890"]
add_pizza(pizza_list)
display_pizza()