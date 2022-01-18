class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
car1 = Vehicle()
car2 = Vehicle()

car1.color = "red"
car1.kind = "Convertible"
car1.value = float(60000)
car1.name = "Fer"
print(car1.description())

car2.color = "blue"
car2.kind = "Van"
car2.value = float(10000)
car2.name = "Jump"
print(car2.description())
