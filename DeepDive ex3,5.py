#Exercise 3
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
calc = input("Please enter the operator(+, -, x, /) for the calculation desired: ")
if calc == "+":
    result = num1 + num2
elif calc == "-": 
    result = num1 - num2
elif calc.lower() == "x":
    result = num1 * num2
elif calc == "/":
    result = num1/num2
#print(num1, calc, num2, "=", result)
print("%d %s %d = %d" %(num1, calc, num2, result))
#2nd print is better since it specifies the data type of the value to be outputted
