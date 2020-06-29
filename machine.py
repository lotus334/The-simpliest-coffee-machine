avail_water = 400
avail_milk = 540
avail_coffee_beans = 120
avail_disposable = 9
avail_money = 550
avail = [400, 540, 120, 9, 550]
ingr = ['water', 'milk', 'coffee beans', 'disposable cups', 'money']

def machine_has():
    print('The coffee machine has:')
    print(str(avail[0]) + ' of water')
    print(str(avail[1]) + ' of milk')
    print(str(avail[2]) + ' of coffee beans')
    print(str(avail[3]) + ' of disposable cups')
    print(str(avail[4]) + ' of money')

def compare_amount(coffee):
    for index in range(len(avail) - 1):
        if avail[index] < coffee[index]:
            global ingridient
            ingridient = ingr[index]
            return False
    return True

def take_coffee():
    global avail
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    type_of_coffee = input()
    espresso = [250, 0, 16, 1, 4]
    latte = [350, 75, 20, 1, 7]
    cappuccino = [200, 100, 12, 1, 6]
    if type_of_coffee == '1':
        #Espresso
        if compare_amount(espresso) == True:
            print('I have enough resources, making you a coffee!')
            avail[0] -= 250
            avail[1] -= 0
            avail[2] -= 16
            avail[3] -= 1
            avail[4] += 4
        else:
            print('Sorry, not enought ' + ingridient + '!')
    elif type_of_coffee == '2':
        #Latte
        if compare_amount(latte) == True:
            print('I have enough resources, making you a coffee!')
            avail[0] -= 350
            avail[1] -= 75
            avail[2] -= 20
            avail[3] -= 1
            avail[4] += 7
        else:
            print('Sorry, not enought ' + ingridient + '!')
    elif type_of_coffee == '3':
        #Cappuccino
        if compare_amount(cappuccino) == True:
            print('I have enough resources, making you a coffee!')
            avail[0] -= 200
            avail[1] -= 100
            avail[2] -= 12
            avail[3] -= 1
            avail[4] += 6
        else:
            print('Sorry, not enought ' + ingridient + '!')
    elif type_of_coffee == 'back':
        None
        
def fill_machine():
    global avail
    print('Write how many ml of water do you want to add:')
    avail[0] += int(input())
    print('Write how many ml of milk do you want to add:')
    avail[1] += int(input())
    print('Write how many grams of coffee beans do you want to add:')
    avail[2] += int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    avail[3] += int(input())

def action():
    action = ''
    while action != 'exit':
        print('Write action (buy, fill, take, remaining, exit):')
        action = input()
        if action == 'buy':
            take_coffee()
        elif action == 'fill':
            fill_machine()
        elif action == 'take':
            global avail
            print('I gave you $' + str(avail_money))
            avail[4] = 0
        elif action == 'remaining':
            machine_has()
        print()

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