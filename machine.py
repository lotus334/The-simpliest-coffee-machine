avail_water = 400
avail_milk = 540
avail_coffee_beans = 120
avail_disposable = 9
avail_money = 550

def machine_has():
    print('The coffee machine has:')
    print(str(avail_water) + ' of water')
    print(str(avail_milk) + ' of milk')
    print(str(avail_coffee_beans) + ' of coffee beans')
    print(str(avail_disposable) + ' of disposable cups')
    print(str(avail_money) + ' of money')

def take_coffee():
    global avail_water
    global avail_milk
    global avail_coffee_beans
    global avail_disposable
    global avail_money
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    type_of_coffee = int(input())
    if type_of_coffee == 1:
        #Espresso
        avail_water -= 250
        avail_coffee_beans -= 16
        avail_disposable -= 1
        avail_money += 4
    elif type_of_coffee == 2:
        #Latte
        avail_water -= 350
        avail_milk -= 75
        avail_coffee_beans -= 20
        avail_disposable -= 1
        avail_money += 7
    elif type_of_coffee == 3:
        #Cappuccino
        avail_water -= 200
        avail_milk -= 100
        avail_coffee_beans -= 12
        avail_disposable -= 1
        avail_money += 6
        
def fill_machine():
    global avail_water
    global avail_milk
    global avail_coffee_beans
    global avail_disposable
    print('Write how many ml of water do you want to add:')
    avail_water += int(input())
    print('Write how many ml of milk do you want to add:')
    avail_milk += int(input())
    print('Write how many grams of coffee beans do you want to add:')
    avail_coffee_beans += int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    avail_disposable += int(input())

def action():
    machine_has()
    print()
    print('Write action (buy, fill, take):')
    action = input()
    if action == 'buy':
        take_coffee()
    elif action == 'fill':
        fill_machine()
    elif action == 'take':
        global avail_money
        print('I gave you $' + str(avail_money))
        avail_money = 0
    print()
    machine_has()

action()

'''
print('Write how many ml of water the coffee machine has:')
avail_water = int(input())
print('Write how many ml of milk the coffee machine has:')
avail_milk = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
avail_coffee_beans = int(input())
print('Write how many cups of coffee you will need:')
num_of_cups = int(input())
#print('For ' + str(num_of_cups) + ' cups of coffee you will need:')
req_water = num_of_cups * 200
req_milk = num_of_cups * 50
req_coffee_beans = num_of_cups * 15
#print(str(req_water) + ' ml of water')
#print(str(req_milk) + ' ml of milk')
#print(str(req_coffee_beans) + ' g of coffee beans')
avail_cups = 0
if avail_water / 200 > 0:
    avail_cups = int(avail_water / 200)
if avail_milk / 50 < avail_cups:
    avail_cups = int(avail_milk / 50)
if avail_coffee_beans / 15 < avail_cups:
    avail_cups = int(avail_coffee_beans / 15)
if avail_cups >= num_of_cups:
    print('Yes, I can make that amount of coffee', end = '')
    left_cups = avail_cups - num_of_cups
    if left_cups > 0:
        print(' (and even ' + str(int(left_cups)) + ' more than that)')
else:
    print('No, I can make only ' + str(avail_cups) + ' cups of coffee')
'''