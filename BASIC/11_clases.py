class EmptyPerson:
    pass
class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.name = name
        self.surname = surname
        self.alias = alias
    def walk(self):
        print(f" {self.name} {self.surname} alias {self.alias} esta caminando")

my_person = Person("Juan","OsoC")
print(my_person)
print(my_person.name)
print(my_person.surname)
print(f"{my_person.name} {my_person.surname}")

my_person.walk()

my_person.alias = 1212312312312
print(my_person)