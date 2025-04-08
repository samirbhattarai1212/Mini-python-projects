from data import resources, MENU

def check_resources(order_resources):
    for iteam in order_resources:
        if order_resources[iteam]> resources[iteam]:
            print(f"we do not have enough {iteam}")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transcation(drinks_price,total_price):
    if drinks_price>= total_price:
        print("sorry, you do not have enough money. money refunded.")
        return False
    else:
        change = round(total_price - drinks_price, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drinks_price
        return True

def make_coffee(drink_name, ingredients):
    for iteams in ingredients:
        resources[iteams] -= ingredients[iteams]
    print(f"Here's you {drink_name}☕")



turn_on=True
money=0
while turn_on:
    user_order=input("What would you like? (espresso/latte/cappuccino):")
    if user_order=="report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}gm")
        print(f"money: {money}")
    elif user_order=="off":
        turn_on=False
    else:
        drink=MENU[user_order]
        if check_resources(drink["ingredients"]):
            payment= process_coins()
            if transcation(drink["cost"],payment):
                make_coffee(user_order,drink["ingredients"])
            



