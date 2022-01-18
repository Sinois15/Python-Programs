class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

#main    

Cars = {}

car = Vehicle()
car.name = input("Enter name: ")
car.kind = input("Enter kind: ")
car.color = input("Enter color: ")
car.value = float(input("Enter value: "))

Cars["Car"] = {car.name, car.kind, car.color, car.value}





