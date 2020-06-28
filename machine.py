# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:34:34 2020

@author: lotus
"""
print('Write how many cups of coffee you will need:')
num_of_cups = int(input())
print('For ' + str(num_of_cups) + ' cups of coffee you will need:')
req_water = num_of_cups * 200
req_milk = num_of_cups * 50
req_coffee_beans = num_of_cups *15
print(str(req_water) + ' ml of water')
print(str(req_milk) + ' ml of milk')
print(str(req_coffee_beans) + ' g of coffee beans')
print('Starting to make a coffee')
print('Grinding coffee beans')
print('Boiling water')
print('Mixing boiled water with crushed coffee beans')
print('Pouring coffee into the cup')
print('Pouring some milk into the cup')
print('Coffee is ready!')