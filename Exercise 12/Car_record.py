Cars = {}

def add(name, kind, color, price):
    record_name = str(color) + " " + str(name)
    Cars[record_name] = [name, kind, color, price]
    print("\nRecord Added!\n")
    
def select():
    x = 1
    while(1):
        print("RECORD NAMES: ")
        for rec_name in Cars.keys():
            print("%d. %s"%(x, rec_name))
            x += 1
        choice = input("Enter the name of record to be editted: ")
        if (choice not in Cars.keys()):
            print("Record not found! Try again.\n")
        else:
            break
    return choice
    
def delete(record_name):
    print("--------------")
    print("DELETE RECORD")
    print("--------------")
    del Cars[record_name]
    print("\nRecord Deleted!\n")
    
def edit(record_name):
    print("--------------")
    print("EDIT RECORD")
    print("--------------")
    while(1):
        leave = 2
        print("1. Name\n2. Kind\n3. Color\n4. Price")
        choice = int(input("Enter a number to edit the matching value: "))
        if (choice<0 or choice>4):
            print("Invalid choice! Please try again.")
        elif (choice == 1):
            name = input("Enter the new name: ")
            Cars[record_name][0] = name
        elif (choice == 2):
            kind = input("Enter new kind: ")
            Cars[record_name][1] = kind
        elif (choice == 3):
            color = input("Enter new color: ")
            Cars[record_name][2] = color
        elif (choice == 4):
            price = float(input("Enter new price: "))
            Cars[record_name][3] = price
        print("\nRecord Added!")
        print("\nContinue editing record?")
        while (leave<0 or leave>1):
            leave = int(input("Enter 1 for Yes and 0 for No: "))
            if (leave<0 or leave>1):
                print("Invalid choice! Try again.")
            
        if (leave == 0):
            print("Record editing ended\n")
            break
        

def view():
    print("--------------")
    print("VIEW RECORDS")
    print("--------------")
    x = 1
    if (Cars):
        for rec_name, content in Cars.items():
            print("%d. %s"%(x, rec_name))
            x += 1
            #print(content)
            print("Name: %s\nKind: %s\nColor: %s\nPrice: %.2f\n"%(content[0], content[1], content[2], content[3]))
    else:
        print("No records yet\n")
        
        
        
def save():
    file = open ("CarRecord.txt", "w") 
    if(Cars):
        for rec_name, content in Cars.items(): 
            file.write("%s:"%(rec_name))
            file.write("%s:%s:%s:%.2f\n"%(content[0], content[1], content[2], content[3]))
    else:
        file.write("No records yet.")
        
    file.close()
    print("\nRecords Saved!\n")
        
    