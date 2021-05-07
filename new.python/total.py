'''''''''
def x(n):
    if n==1 or n==2:
        return 1
    else:
        return(x(n-1)+x(n-2))
print(x(10))

def summiation(number):
    if number==1:
        return 1
    summiation(number-1)
    return"lanka"
summiation(10)

def factorial(n):
    if n==0: return 1
    return n* factorial(n-1)
print(factorial(6))

def x(n):
    if n==0:
        return 0
    else:
        print (n)
        return x(n-1)
print(x(4)) 

def listsum(x):
    if len(x) == 1 : return x[0]
    return x[0]+listsum(x[1:])
print(listsum([1,2,3,]))
'''''''''''
def harmonic_sum(n):
    if n<2:
        return 1
    else:
        return 1/n+(harmonic_sum(n-1))
print(harmonic_sum(5))
#print()










