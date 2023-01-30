"""
Author: Damian Archer
Date: 1/12/23
File: xml_three_vegan_products_lab.py
Purpose: PCPP Exercises - XML File Writing/Creation
"""

import xml.etree.ElementTree as ET

TYPE, PRODUCER, PRICE, CURRENCY = 0,1,2,3

products = {'Good Morning Sunshine':
           ('cereals', 'OpenEDG Testing Service', '9.90', 'USD'),
           'Spaghetti Veganietto':
           ('pasta', 'Programmers Eat Pasta', '15.49', 'EUR'),
           'Fantastic Almond Milk':
           ('beverages', 'Drinks4Coders Inc.', '19.75', 'USD')
            }

root = ET.Element('shop')
category = ET.SubElement(root, 'category', {'name' : 'vegan products'})

for k,v in products.items():
    product = ET.SubElement(category, 'product', {'name': k})
    product_type = ET.SubElement(product, 'type')
    product_producer = ET.SubElement(product,'producer')
    product_price = ET.SubElement(product, 'price')
    product_currency = ET.SubElement(product, 'currency')
    
    product_type.text = v[TYPE]
    product_producer.text = v[PRODUCER]
    product_price.text = v[PRICE]
    product_currency.text = v[CURRENCY]


tree = ET.ElementTree(root)
ET.indent(tree, space="\t", level=0)
tree.write('shop.xml', 'UTF-8', True)


