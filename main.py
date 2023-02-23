import Pizza


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


def print_details(x, y):
    print('Customer :', x)
    print('Pizza Preference :', y)


def pizza_addon(x, y):
    addon = x
    print('\n')
    FinalPizzaChoice[customer_name] = y
    print_details(customer_name, y)
    print('Total :', addon + base)


base = 450
customer_name = input('Name : ')
pizza = module_chooser(['Deluxe', 'Special', 'Primo'])

print('\n')
print('--Details--')
print('Base :', base)

if pizza == 1:
    pizza_addon(Pizza.deluxe_addon(), 'Deluxe')

elif pizza == 2:
    pizza_addon(Pizza.special_addon(), 'Special')

elif pizza == 3:
    pizza_addon(Pizza.primo_addon(), 'Primo')

print('\n')
print(FinalPizzaChoice)
