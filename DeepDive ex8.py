def menu():
    print("---------")
    print("MENU")
    print("---------")
    print("1. Addition")
    print("2. Substration")
    print("3. Multiplication")
    print("4. Division")
    print("5. View Past results")
    print("6. Exit")
    print()
    global choice
    choice = int(input("Enter a number from the list above to perform the corresponding action: "))
    #return choice

def input_num():
    global num1
    global num2
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

def add(a, b):
    return a + b

def subs(a, b):
    return (a - b)

def mult(a, b):
    return (a*b)

def div(a, b):
    return (a/b)

def save(answers, a, b, calc, result):
    record = str(a) + " " + str(calc) + " " + str(b) + " = " 
    answers.append(result)
    components.append(record)
    
def view_results(l_answers):
    print("-------------")
    print("PAST RESULTS")
    print("-------------")
    print()
    if len(l_answers) == 0:
        print("No results recorded yet")
    else:
        for x in range(len(l_answers)):
            print(components[x], "%.3f"%answers[x])
        print()
            
def process(calc):
    global num1
    global num2
    input_num()
    if calc == "+":
        result = add(num1, num2)
      
    elif calc == "-":
        result = subs(num1, num2)
        
    elif calc == "x":
        result = mult(num1, num2)
        
    elif calc == "/":
        result = div(num1, num2)
    print("---------")
    print("ANSWERS")
    print("---------")
    print(num1, calc, num2, "=", "%.3f"%result)
    save(answers, num1, num2, calc, result)
    print()
    
#main
choice = 0
num1 = -1
num2 = -1
components = []
answers = []
leave = -1
while True:
    menu()
    if choice<1 or choice>6:
        print("Invalid choice")
    elif choice == 1:
        process("+")
        
    elif choice == 2:
        process("-")
        
    elif choice == 3:
        process("x")
        
    elif choice == 4:
        process("/")
        
    elif choice == 5:
        view_results(answers)
        
    elif choice == 6:
        while (leave<0 or leave>1):
            print("Exit the program?")
            leave = int(input("Enter 1 for Yes or 0 for No: "))
            if (leave<0 or leave >1):
                print("invalid choice")
            elif (leave == 1 or leave == 0):
                break
        if (leave == 1):
            print("---------")
            print("Bye Bye")
            print("---------")
            break
        elif(leave == 0):
            continue
                
       
        
    