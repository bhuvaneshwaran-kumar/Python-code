x=5

print("before calling function1 in global scope: ",x)

def function1():
    global x  # this has to be done when you want to modify/write global variables inside function
    x=10
    print("inside function: ",x)

function1()
print("after calling function in global scope: ",x)

print("---------------------------------------------------")

# function can return multiple values
def calculation(x,y):
    sums=x+y
    subb=x-y
    return sums,subb


sums,subb=calculation(10,5)

print("Sum: ",sums)
print("Sub: ",subb)