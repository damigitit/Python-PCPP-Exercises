"""
Author: Damian Archer
File: deep_copy_2.py
Date: 1/16/2023
Purpose: PCPP Exercises
"""

import copy

class Delicacy(dict):
    def __init__(self):
        pass

    def add(self, name, price, weight):
        self[name] = {"price": price, "weight": weight}

    def __str__(self):
        string = ''
        for key, value in self.items():
            string += f"{key} " f"{value}"
            string += '\n'
        return string

delicacy = Delicacy()

delicacy.add('candy', 2.50, 3.22)
delicacy.add('chocolate', 5.00, 6.34)
delicacy.add('soda', 1.23, 1.22)


print(delicacy)
print('making copy of delicacy...')
delicacy_copy = copy.copy(delicacy)

delicacy['candy']['price'] *= 2
print("The price of candy has been doubled")
print("in both delicacy...")
print(delicacy)
print("and delicacy_copy...")
print(delicacy_copy)

print('making deep copy of delicacy...')
delicacy_deep_copy = copy.deepcopy(delicacy)
print("doubling price of soda in delicacy...")
delicacy['soda']['price'] *= 2

print("\nSoda price change is reflected in delicacy...")
print(delicacy)
print("but not in delicacy_deep_copy...")
print(delicacy_deep_copy)

