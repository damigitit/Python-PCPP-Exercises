"""
Author: Damian Archer
Date: 1/2/2023
File: static_and_class_methods_exercise.py
Purpose: PCPP Exercises - Static and Class Methods
"""

class LuxuryWatch:
    watches_created = 0
    
    def __init__(self):
        LuxuryWatch.watches_created += 1
        self.engraving = ''
        
    @classmethod
    def get_number_of_watches_created(cls):
        return "# of watches created: {}".format(cls.watches_created)
        
    @classmethod
    def engraved_watch(cls, text):
        try:
            if cls.validate(text):
                _watch = cls()
                _watch.engraving = text
                return _watch
            else: raise Exception
        except:
            print("Invalid text engraving... engraving", text, "not applied")

    @staticmethod
    def validate(text):      
        if len(text) < 40 and text.isalnum():
            return True
        else:
            return False

    def get_engraving(cls):
        return cls.engraving

    


watch = LuxuryWatch()
print(LuxuryWatch.get_number_of_watches_created())

valid_engraved_watch = LuxuryWatch.engraved_watch("Damian")
print("Created watch with engraving {}".format(valid_engraved_watch.engraving))
print(LuxuryWatch.get_number_of_watches_created())

invalid_engraved_watch = LuxuryWatch.engraved_watch("foo@baz.com")
print(LuxuryWatch.get_number_of_watches_created())
