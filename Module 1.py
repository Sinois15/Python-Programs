#Print
x = 1
if (x == 1):
    print("x is 1 u twat")
#print without newline
a = [1, 2, 3, 4]
for i in range(4):
    print(a[i], end =" ")
print()

#Exercise 1    
print("Welcome to brainded class :)")

#Basic variables: numbers and strings
myint = 7
print(myint)

myfloat = 7.0 #flaot data type detected, variable set to it automatically
print(myfloat)
myfloat = float(7)# manually set it to float, just for the sake of it
print(myfloat)

mystring = "hewo"
print(mystring)
mystring = 'hello'
print(mystring)
#can use both single and double quotes but double is encouraged, cuz problems with things like 'don't'
mystring = "Don't worry about apostrophes"
print(mystring)

#Operators
one = 1
two = 2
three = one + two
print("three is ", three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

#Assignment of variables
one = 1
two = 2
hello = "hello"
#print (one + two + hello) cannot be done

#Exercise 2
mystring = "hello"
myfloat = 10.0
myint = 20

#Arithmetic operators
number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#Operations with strings
helloworld = "hello" + " " + "world"
print(helloworld)


lotsofhellos = "hello" * 10
print(lotsofhellos)

#Operations with lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

#String formatting
name = "John"
print("Hello, %s!" % name)

name = "John"
age = 23
print("%s is %d years old." % (name, age))

mylist = [1,2,3]
print("A list: %s" % mylist)
# %s is for strings
# %d is for integers
# %f is for float
# %.<number>f sets the number of decimal points
# %x/%X - Integers in hex representation (lowercase/uppercase)

astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))
#prints the number of characters in the string

astring = "Hello world!"
print(astring.index("o"))
#outputs the index of the first o

astring = "Hello world!"
print(astring.count("l"))
#outputs the number of l's

astring = "Hello world!"
print(astring[3:7])
#outputs from index 3 to 6, range is upper limit exclusive

astring = "Hello world!"
print(astring[-7:-3])
#starts from 7th index from the back, goes backwards and stops at 3rd character from the end

astring = "Hello world!"
print(astring[3:7:2])
#starts from index 3, stops at 6 and moves by 2 indexes each time
#step 0f 1 is default if not specified

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

astring = "Hello world!"
print(astring[::-1])
#reverse step, so it reverses the string

astring = "Hello world!"
print(astring.upper()) #changes to upper case
print(astring.lower()) #lower case

astring = "Hello world!"
print(astring.startswith("Hello"))
#checking if the string does start with "Hello"
print(astring.endswith("asdfasdfasdf"))
#checking if the string does end with "asdfasdfasdf"

astring = "Hello world!"
afewwords = astring.split(" ")
#splits the string at the space and stores the splited in variable afterwords as a list
print(afewwords)

year = 2021
string = "it is going to be amazing in the year {}"
print(string.format (year))
#.format replaces all {} in the string with the specified variable/value
# follows the order in which the variable/values are written as shown below

qty = 15
item = 16
fees = 50.50
quotation = "the total fee for {} pieces of {} cost {}."
print(quotation.format(qty, item, fees) )

#If, else, controls and loops
#conditions
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

#boolean operator
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# "in" operator
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
#"in" allows to find a specific value in data structures without iterative means e.g. loop


#else if/elif
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")
    
# "is" operator
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False
#"is" compares the instances instead of the values 
# "is" may be used to check if some data is stored in the same memory location

# "not" operator
print(not False) # Prints out True
print((not False) == (False)) # Prints out False

#Loops
#for loop
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)
# Prints out 3,4,5
for x in range(3, 6):
    print(x)
# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
#"range" returns a list of numbers in the specified range
#"xrange" returns an iterator, more efficient

#while loop
i = 1
while i < 6:
    print(i)
    i += 1

#break and continue
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
        print(x)

#else clause in loops
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
        print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

#list
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print (mylist[0]) # prints 1
print (mylist[1]) # prints 2
print (mylist[2]) # prints 3
# prints out 1,2,3
for x in mylist:
    print(x)



