# Write your code here
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