class CoffeeMachine:    
    ingridient = ''
    
    def __init__(self, water = 400, milk = 540, coffee_beans = 120, disposable_cups = 9, money = 550):
        self.avail = [water, milk, coffee_beans, disposable_cups, money]
        self.ingr = ['water', 'milk', 'coffee beans', 'disposable cups', 'money']
        
    def __str__(self):
        return '|'.join(map(str, self.avail))
 
    def __repr__(self):
        return 'CoffeeMachine({}, {}, {}, {}, {})'.format(self.avail[0], self.avail[1], self.avail[2], self.avail[3], self.avail[4])
        
    def action(self):
        print('Write action (buy, fill, take, remaining, exit):')
        str_action = input()
        if str_action == 'buy':
            return self.take_coffee()
        elif str_action == 'fill':
            return self.fill_machine()
        elif str_action == 'take':
            return self.take_money()
        elif str_action == 'remaining':
            return self.machine_has()
            
    def take_money(self):
        print(f'I gave you ${self.avail[4]}')
        self.avail[4] = 0
        return self.action()
            
    def compare_amount(self, coffee):
        for index in range(len(self.avail) - 1):
            if self.avail[index] < coffee[index]:
                self.ingridient = self.ingr[index]
                return False
        return True
            
    def take_coffee(self):        
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        type_of_coffee = input()
        espresso = [250, 0, 16, 1, 4]
        latte = [350, 75, 20, 1, 7]
        cappuccino = [200, 100, 12, 1, 6]
        if type_of_coffee == '1':
            #Espresso
            if self.compare_amount(espresso) == True:
                print('I have enough resources, making you a coffee!')
                self.avail[0] -= 250
                self.avail[1] -= 0
                self.avail[2] -= 16
                self.avail[3] -= 1
                self.avail[4] += 4
            else:
                print('Sorry, not enought {}!'.format(self.ingridient))
        elif type_of_coffee == '2':
            #Latte
            if self.compare_amount(latte) == True:
                print('I have enough resources, making you a coffee!')
                self.avail[0] -= 350
                self.avail[1] -= 75
                self.avail[2] -= 20
                self.avail[3] -= 1
                self.avail[4] += 7
            else:
                print('Sorry, not enought {}!'.format(self.ingridient))
        elif type_of_coffee == '3':
            #Cappuccino
            if self.compare_amount(cappuccino) == True:
                print('I have enough resources, making you a coffee!')
                self.avail[0] -= 200
                self.avail[1] -= 100
                self.avail[2] -= 12
                self.avail[3] -= 1
                self.avail[4] += 6
            else:
                print('Sorry, not enought {}!'.format(self.ingridient))
        elif type_of_coffee == 'back':
            None
        return self.action()
            
    def fill_machine(self):
        print('Write how many ml of water do you want to add:')
        self.avail[0] += int(input())
        print('Write how many ml of milk do you want to add:')
        self.avail[1] += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.avail[2] += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.avail[3] += int(input())
        return self.action()
    
    def machine_has(self):
        print('The coffee machine has:')
        print('{} of {}'.format(self.avail[0], self.ingr[0]))
        print('{} of {}'.format(self.avail[1], self.ingr[1]))
        print('{} of {}'.format(self.avail[2], self.ingr[2]))
        print('{} of {}'.format(self.avail[3], self.ingr[3]))
        print('{} of {}'.format(self.avail[4], self.ingr[4]))
        return self.action()

    
coffee_mach = CoffeeMachine()
#print(coffee_mach)
#print(repr(coffee_mach))
coffee_mach.action()