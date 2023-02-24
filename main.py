import pizza


FinalPizzaChoice = {}


def module_chooser(y):
    while True:
        try:
            prompt = ''
            i = 1
            for z in y:
                prompt += z + ' : ' + str(i)
                if i == len(y):
                    prompt += '   |   '
                    return int(input(prompt))
                i += 1
                prompt += ' | '

        except ValueError:
            print('Invalid Input')
            print('\n')


def input_string(x):
    while True:
        y = input(x).strip()
        if len(str(y)) != 0:
            return str(y)
        print('Invalid Input')
        print('\n')


def print_details(x, y):
    print('Customer :', x)
    print('Pizza Preference :', y)


def pizza_addon(x, y):
    addon = x
    print('\n')
    FinalPizzaChoice[customer_name] = y
    print_details(customer_name, y)
    print('Bill :', addon + base)


base = 450
customer_name = input_string('Name : ')
pizza_toppings = module_chooser(['Deluxe', 'Special', 'Primo'])

print('\n')
print('--Details--')
print('Base :', base)

if pizza_toppings == 1:
    pizza_addon(pizza.deluxe_addon(), 'Deluxe')

elif pizza_toppings == 2:
    pizza_addon(pizza.special_addon(), 'Special')

elif pizza_toppings == 3:
    pizza_addon(pizza.primo_addon(), 'Primo')

print('\n')
