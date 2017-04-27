#Your mission is to create the structure for 2 decorators, one to log the name and arguments of a function and one to log the execution time.
import time

def timer(f):
    def inner(num):
        first = time.time()
        f(num)
        return time.time() - first
    return inner

def name(f):
    def inner(num):
        name = f.func_name
        variables = str(num)
        return "name: " + name + "\nparameters: " + variables + "\n"
    return inner + str(f.func_name)

@name
@timer
def fib(i):
    if i == 1 or i == 2:
        return 1
    return fib(i-1)+fib(i-2)
    
for i in range(1,36):
    print str(i) + ": "+ str(fib(i))

#closure = wrapper(fib)
#closure(3) #will run foo with the arguments -2, 3, 'hello' through wrapper
#time.time()
#if f is a variable that represents a function f.func_name will return the name of the function.
