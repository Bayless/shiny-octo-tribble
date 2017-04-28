#Your mission is to create the structure for 2 decorators, one to log the name and arguments of a function and one to log the execution time.
import time

def timer(f):
    def inner(*num):
        first = time.time()
        f(*num)
        totalTime = time.time() - first
        print totalTime
        return totalTime
    return inner

def name(f):
    def inner2(*num):
        f(*num)
        name = f.func_name
        ret = "name: " + name + "\nparameters: " + str(num) + "\n"
        print ret 
        return ret
    return inner2

@name
#@timer
def fib(i):
    if i == 1 or i == 2:
        return 1
    return fib(i-1)+fib(i-2)

@name
#@timer
def adding(q,w,e,r,t):
    return q+w+e+r+t


#for i in range(1,36):
 #   print str(i) + ": "+ str(fib(i))

print fib(5)
print adding(1,2,3,4,5)
#closure = wrapper(fib)
#closure(3) #will run foo with the arguments -2, 3, 'hello' through wrapper
#time.time()
#if f is a variable that represents a function f.func_name will return the name of the function.
