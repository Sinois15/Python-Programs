#vehicle class definition
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
#menu function
def menu():
    print("----------")
    print("MENU")
    print("----------")
    print("1. Add record\n2. Delete record\n3. Edit record\n4. Display records\n5. Save records\n6. Exit program\n")

#exit program function

def leave():
    global ext
    ext = 2
    print("--------------")
    print("EXITING")
    print("--------------")
    while(ext < 0 or ext > 1):
        print("Quit program?")
        ext = int(input("Enter 1 for Yes and 0 for No: "))
        if (ext < 0 or ext >1):
            print("Invalid choice. Try again.\n")
    

#main
import Car_record

print(result)
while(1):
    menu()
    choice = int(input("Enter a number to perform the matching process: "))
    if (choice<1 or choice>6):
        print("Invalid choice! Try again.")
    elif (choice == 1):
        print("--------------")
        print("ADD RECORD")
        print("--------------")
        car = Vehicle()
        car.name = input("Enter name: ")
        car.kind = input("Enter kind: ")
        car.color = input("Enter color: ")
        car.value = float(input("Enter value: "))
        Car_record.add(car.name, car.kind, car.color, car.value)
    
    elif (choice == 2):
        rec_name = Car_record.select()
        Car_record.delete(rec_name)
    
    elif (choice == 3):
        rec_name = Car_record.select()
        Car_record.edit(rec_name)
        
    elif (choice == 4):
        Car_record.view()
    
    elif (choice == 5):
        Car_record.save()
    
    elif (choice == 6):
        leave()
        if (ext == 1):
            print("Bye Bye\nExiting program.")
            break
        else:
            continue

