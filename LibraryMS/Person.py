
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        print("person name " + self.name + "emailID " + self.email)

