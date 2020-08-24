import calculations as cal
import random
import os
# os.getcwd() returns the current directory where the program is executed
print("Current dir before: ",os.getcwd())

print("Files present: ")
# returns all the files present in the current directory as a list
print(os.listdir())

for files in os.listdir():
    print(files)
# os.mkdir(foldername) it creates a folder in the current directory
os.mkdir("demo_folder")

os.chdir("demo_folder")
print("Current dir after: ",os.getcwd())

# ############################################################################
# password generator

lowercase=[chr(x) for x in range(97,123)]
numbers=[str(x) for x in range(0,10)]
uppercase=[x.upper() for x in lowercase]

total = lowercase + uppercase +numbers

password=''
# random.choice(list) returns a random picked value from passes list
password = password + random.choice(lowercase)
password = password + random.choice(uppercase)

# str(number) returns the string representation of the passed variable
password = password + str(random.choice(numbers))



# i default value 0
for i in range(5):   # 0 ,1 ,2, 3, 4
    charac= random.choice(total)
    password = password + charac
    print(i ," : ",charac )

print("password: ",password)

