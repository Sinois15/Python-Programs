#Functions, classes and objects

#Functions
def my_function():
    print("Hello From My Function!")
    
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
          
def sum_two_numbers(a, b):
    return a + b

my_function()
my_function_with_args("John Doe", "a great year!")
x = sum_two_numbers(1,2)
print(sum_two_numbers(2, 2))

#Classes

#class definition:
class MyClass:
    topic = "blah"
    
    def review(self):
        print("the class was meh")
#the "self" keyword only lets the compiler that there's a function in this class
#its not counted when inputing parameters
#when using its variables within the class itself, use self.<variable>

#creating and accessing an object
testObject = MyClass()
print(testObject.topic)
testObject.review()

#Dictionaries
#like arrays but the indexes are customizable values named "keywords"
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

#initializing a dictionary
phonebook = {
 "John" : 938477566,
 "Jack" : 938377264,
 "Jill" : 947662781
}
print(phonebook)      

#values are not ordered in a dictionary and are thus iterated as following
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
    
#adding a value
phone_num = 1116365238 #can input also
phonebook["me"] = phone_num 

#removing a value
phonebook = {
 "John" : 938477566,
 "Jack" : 938377264,
 "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)
#OR 
phonebook = {
 "John" : 938477566,
 "Jack" : 938377264,
 "Jill" : 947662781
}
phonebook.pop("Jill")
print(phonebook)