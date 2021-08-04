from main import MENU
profit =0
resource ={ "water" : 300,
    "milk":200,
    "coffee": 100,
    "money" : 0
    }
# for key in resource:
#     print(key)
#     print(resource[key])



water = resource["water"]
milk = resource["milk"]
coffee = resource["coffee"]
money = resource["money"]

# current_milk = 0
# current_coffee = 0 
# current_water = 0
# current_money = 0

# calculating resource used
def make_coffee(order_ingredients,user):
    ''''deduct ingrdients from the coffee'''
    for items in order_ingredients:
        resource[items] -= order_ingredients[items]
        

    
def is_resource_sufficient(order_ingredients,resource):
    for items in order_ingredients:
        if order_ingredients[items]>= resource[items]:
            print("sorry there is no sufficient resouces")
            return False
    return True

def money_requirement(MENU,money):
    quater = float(input("how many quarters?:"))
    quater = quater * 0.25

    dimies = float(input("how many dimes?:"))
    dimies = dimies * 0.10

    nickles = float(input("how many nickles?:"))
    nickles = nickles * 0.05

    pennies = float(input("how many pennies?:"))
    pennies = pennies * 0.01
    # print(MENU["espresso"]["cost"])

    # total money calculated
    total_money = quater + dimies + nickles + pennies 
    total_money =round(total_money,2)
    print(f" your total money inserted is ${total_money}")

    # checking money is sufficient or not if not then money refunded
    if MENU["espresso"]["cost"] < total_money :
        print(f"here is your order of {user} ☕")
        cost_of_coffee= MENU["espresso"]["cost"]
        money = money + cost_of_coffee
        change = total_money - cost_of_coffee
        change = round(change , 2)
        print(f"your change is ${change}")
        global profit
        profit +=cost_of_coffee
        return True
    else:
        print("sorry money is insuffient. MONEY REFUNDED!!")
        return False

# asking input form the user of coffee

to_be_continue = True
while to_be_continue:
    user = input ("“What would you like? (espresso/latte/cappuccino) : ")


    if user == "espresso":
        drink = MENU[user]
        if is_resource_sufficient(drink["ingredients"],resource):
            print("Please insert coins")
            money_requirement(MENU,money)
            make_coffee(drink["ingredients"],user)
            
            
    elif user == "latte":
        drink = MENU[user]
        if is_resource_sufficient(drink["ingredients"],resource):
            print("Please insert coins")
            money_requirement(MENU,money)
            make_coffee(drink["ingredients"],user)
    elif user == "cappuccino":
        drink = MENU[user]
        if is_resource_sufficient(drink["ingredients"],resource):
            print("Please insert coins")
            money_requirement(MENU,money)
            make_coffee(drink["ingredients"],user)
    elif user == "report":
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Money: ${profit}")
    elif user == "off":
        to_be_continue = False

