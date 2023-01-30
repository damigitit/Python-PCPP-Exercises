"""
Author: Damian Archer
Date: 12/23
File: class_and_instance_data.py
Purpose: PCPP Exercises - Class and Instance Data
"""

import random

class Apple:
    def __init__(self, unit_weight):
        self.unit_weight = unit_weight
    
    def get_unit_weight(self):
        return self.unit_weight
        

class ApplePackage:
    count = 0
    package_weight = 0
    apples = []
    
    def __init__(self):
        
        while ((ApplePackage.count < 1000) \
               and (ApplePackage.package_weight < 300)):

            apple = Apple(random.uniform(0.2, 0.5)) # instantiate apple with
                                                    # random weight

            # if constraints can be met, add the apple to the package
            # otherwise, stop adding apples.
            if ((apple.get_unit_weight() + ApplePackage.package_weight) < 300):
                ApplePackage.apples.append(apple)
                ApplePackage.package_weight += apple.get_unit_weight()
                ApplePackage.count += 1
            else:
                break

    def get_package_details(self):
        print(f"There are {len(ApplePackage.apples)} apples in this package, weighing {ApplePackage.package_weight} units")
   
     
package = ApplePackage()
package.get_package_details()
                
        
