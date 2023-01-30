"""
Author: Damian Archer
Date: 1/12/2023
File: xml_forecast_lab.py
Purpose: PCPP Exercises - XML Parsing
"""

import xml.etree.ElementTree as ET

class TemperatureConverter:

    def convert_celsius_to_fahrenheit(self, celsius):
        assert isinstance(celsius, int) or isinstance(celsius, float)
        return 9/5 * celsius + 32


    def convert_fahrenheit_to_celsius(self, fahrenheit):
        assert isinstance(fahrenheit, int) or isinstance(fahrenheit, float)
        return (fahrenheit - 32) * 5/9
    

class ForecastXmlParser:

    def __init__(self):
        self.converter = TemperatureConverter()
        
    def parse(self):
        tree = ET.parse('forecast.xml')
        
        root = tree.getroot()
        
        for child in root:
            day = child.find('day').text
            c = child.find('temperature_in_celsius').text
            f = self.converter.convert_celsius_to_fahrenheit(int(c))
            print(f"{day}: {c:.3} celsius, {f:.3} fahrenheit")


app = ForecastXmlParser()
app.parse()
