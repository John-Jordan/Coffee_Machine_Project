MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 50,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}


def check_resources(order):
    if MENU[order]["ingredients"]['water'] > resources['water']:
        print('I am sorry, there is not enough water.')
    elif 'milk' in MENU[order]["ingredients"] and MENU[order]["ingredients"]['milk'] > resources['milk']:
        print('I am sorry, there is not enough milk.')
    elif MENU[order]["ingredients"]['coffee'] > resources['coffee']:
        print('I am sorry, there is not enough coffee.')
    else:
        check_money(order)




def update_resources(order):
    if 'water' in MENU[order]['ingredients']:
        resources['water'] -= MENU[order]['ingredients']['water']
    if 'milk' in MENU[order]['ingredients']:
        resources['milk'] -= MENU[order]['ingredients']['milk']
    if 'coffee' in MENU[order]['ingredients']:
        resources['coffee'] -= MENU[order]['ingredients']['coffee']
    resources['money'] += MENU[order]['cost']



def check_money(order):
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))
    total = (quarters * .25 + dimes *.1 +nickels * .05 + pennies * .01)
    if MENU[order]['cost'] > total:
        print('Sorry, you don\'t have enough change. Money refunded')
    else:
        change = total - MENU[order]['cost']
        print(f'Here is ${change} in change.')
        update_resources(order)


run_program = True
while run_program:
    order = input('What would you like? espresso/latte/cappuccino: ')

    if order == 'report':
        print(resources)
        continue

    if order == 'off':
        run_program = False
        continue

    check_resources(order)






