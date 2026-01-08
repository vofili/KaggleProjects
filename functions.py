
#help(print)

help(print)


def least_difference(x,y,z):
    """
    Returns the least difference between any 2 numbers in a 3 integer arguement

    >>> least_difference(1,5,-5)
    4
    """
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    mindiff = min(diff1,diff2,diff3)
    return mindiff

print(least_difference(1,5,-5))

def least_diff_none(a,b,c):
    dff1 = abs(a - b)
    dff2 = abs(a - c)
    dff3 = abs(b - c)
    print(min(dff1,dff2,dff3))

#help(least_difference)

print(least_diff_none(3,6,9))

def sayHello(who="Valentine"):
    print("Hello",who)


sayHello("Timi")
sayHello()
sayHello(who="Nancy")
#higher order functions example

def mod_5(a):
    return a % 5

#return the value that maximizes mod 5
maxmod5 = max(100,50,41,28,13,key=mod_5)
print(maxmod5)


