#Module 3: File handling

#Write to File
file = open ("testfile.txt", "w") 
file.write("Hello World\n") 
file.write("This is our new text file\n")
file.write("and this is another line.\n")
file.write("Why? Because we can.\n") 
file.close()

#Reading File in Python
file = open ("testfile.txt", "r")
print(file.read())

#Reading First 5 Characters in File
file = open ("testfile.txt", "r")
print(file.read (5))

#Reading First Line Characters in File
file = open ("testfile.txt", "r")
print(file.readline())

#Reading Lines Characters in File
file = open ("testfile.txt", "r")
print(file.readline())

#Looping over a file object
file = open("testfile.txt", "r") 
for line in file: 
    print(line)

