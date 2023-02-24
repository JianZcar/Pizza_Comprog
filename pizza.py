AddOns_Dictionary = {'Cheese': 100, 'Mozzarella Cheese': 150, 'Pepper': 80, 'Bacon Ham': 120, 'Mushroom': 130,
                     'Onions Chili': 110, 'Tomato': 90, 'Pineapple': 100, 'Salami': 120}


def total(x):
    a = [0]
    y = 0
    for price in [AddOns_Dictionary[key] for key in x]:
        y += price
        a[0] = y
    return a[0]


def display_list(y):
    for x in y:
        print(x, ' : ', AddOns_Dictionary[x])


def deluxe_addon():
    deluxe_pizza = ['Cheese', 'Bacon Ham', 'Onions Chili']
    display_list(deluxe_pizza)
    return total(deluxe_pizza)


def special_addon():
    special_pizza = ['Cheese', 'Pepper', 'Bacon Ham', 'Mushroom', 'Onions Chili']
    display_list(special_pizza)
    return total(special_pizza)


def primo_addon():
    primo_pizza = ['Mozzarella Cheese', 'Pepper', 'Bacon Ham', 'Mushroom', 'Onions Chili', 'Tomato', 'Pineapple',
                   'Salami']
    display_list(primo_pizza)
    return total(primo_pizza)
