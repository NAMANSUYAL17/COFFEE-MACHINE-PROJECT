Menu={
    'latte':{
        'ingredients':{
            'water':200,
            'milk':150,
            'coffee':24
        },
        'cost':150
    },
    'espresso':{
        'ingredients':{
            'water':50,
            'coffee':18
        },
        'cost':100
    },
    'cuppoccino':{
        'ingredients':{
            'water':250,
            'milk':100,
            'coffee':24
        },
        'cost':200
    }
}
resources ={
    'water':500,
    'milk':200,
    'coffee':100
}
def process_coins():
    print('Please, insert coins')
    coins_five=int(input('How many five rupees coins:'))
    coins_ten=int(input('How many ten rupees coins:'))
    coins_twenty=int(input('How many twenty rupees coins:'))
    total=coins_five*5+coins_ten*10+coins_twenty*20
    return total
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True
def is_payment_successful(coffee_cost,money_recieved):
    if money_recieved>=coffee_cost:
        global profit
        profit+=coffee_cost
        change=money_recieved-coffee_cost
        print(f"Here is your {change}rs change")
        return True
    else:
        print("Sorry, thats not enough money.Money refunded")
def make_coffee(coffee_name,ingredients_coffee):
    for item in ingredients_coffee:
        resources[item]-=ingredients_coffee[item]
    print(f'Here is your {coffee_name}...Enjoy.')
profit=0
is_on=True
while is_on:
    choice=input('What would you like to have?(latte/espresso/cuppoccino)')
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}ml")
        print(f"money={profit}rs")
    else:
        coffee_type=Menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment=process_coins()
            if is_payment_successful(coffee_type['cost'],payment):
                make_coffee(choice,coffee_type['ingredients'])


        