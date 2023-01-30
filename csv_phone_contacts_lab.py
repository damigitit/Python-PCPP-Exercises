import csv

class PhoneContact:

    def __init__(self, name, phone):
        self._name = name
        self._phone = phone

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


class Phone:

    def __init__(self):
        self.contacts = []

    def load_contacts_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            fieldnames = ['Name', 'Phone']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in reader:
                self.contacts.append(PhoneContact(row['Name'], row['Phone']))

    def show_contacts(self):
        for contact in self.contacts:
            print(contact.name,":", contact.phone)

    def search_contacts(self):
        search_criteria = input("Search contacts: ")
        for contact in self.contacts:
            if search_criteria in contact.name or search_criteria in contact.phone:
                print(contact.name, ":", contact.phone)

phone = Phone()
phone.load_contacts_from_csv('contacts.csv')
phone.show_contacts()
phone.search_contacts()

