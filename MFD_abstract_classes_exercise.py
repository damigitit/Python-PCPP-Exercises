"""
Author: Damian Archer
Date: 1/2/2023
File: MFD_abstract_classes_exercise.py
Purpose: PCPP Exercises - Abstract Classes, Inheritance, and Composition
"""

import abc

class Scanner(abc.ABC):

    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass

class Printer(abc.ABC):

    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MFD1(Scanner,Printer):

    def __init__(self):
        self.price = "$200.33"
        self.resolution = "300 DPI"
        self.serial = 203494857

    def scan_document(self):
        return "Document has been scanned"

    def get_scanner_status(self):
        return "scanner resolution is {} and serial number is {}".format(self.resolution, self.serial)

    def print_document(self):
        return "Document has been printed"

    def get_printer_status(self):
        return "Printer resolution is {} and serial number is {}".format(self.resolution, self.serial)

class MFD2(MFD1):
    def __init__(self):
        self.price = "300.22"
        self.resolution = "800 DPI"
        self.serial = 432394837
        self.prints = 0
        self.scans = 0

    def scan_document(self):
        self.scans += 1
        return "Document has been scanned"

    def print_document(self):
        self.prints += 1
        return "Document has been printed"

    def get_printer_history(self):
        print("\nShowing Printer History:")
        return str(self.scans) + " Scans and " + str(self.prints) + " Prints"


class MFD3(MFD2):

    def __init__(self):
        self.price = "$500.11"
        self.resolution = "1200 DPI"
        self.serial = 987232343
        self.prints = 0
        self.scans = 0
        self.faxcount = 0
        self.faxes = {}
        

    def fax_document(self, message, addr):
        self.faxes[self.faxcount] = (message, addr)
        self.faxcount += 1
        return "Faxing \"{}\" to address {}\n".format(message, addr)

    def get_fax_history(self):
        output = ""
        print("Showing Fax History:")
        for key, value in self.faxes.items():
            output += "{} --> {}\n".format(key, value)

        return output
    
mfd1 = MFD1()
print("The MFD1 costs " + mfd1.price)
print(mfd1.scan_document())
print(mfd1.get_scanner_status())
print(mfd1.print_document())
print(mfd1.get_printer_status())
print()

mfd2 = MFD2()
print("The MFD2 costs " + mfd2.price)
print(mfd2.scan_document())
print(mfd2.get_scanner_status())
print(mfd2.print_document())
print(mfd2.get_printer_status())
print(mfd2.get_printer_history())
print()

mfd3 = MFD3()
print("The MFD3 costs " + mfd3.price)
print(mfd3.fax_document("test fax 1", "2073335555"))
print(mfd3.fax_document("yeahhh, uhh, did you get that memo?", "1235555555"))
print(mfd3.get_fax_history())




