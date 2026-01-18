#planets list
planets=["mercury","jupiter","venus","mars","neptune","earth","saturn","uranus","moon"]
#loop through the list
for planet in planets:
    print(planet)

pl_tup=(1,2,3,4,5)
for ind in pl_tup:
    print(pl_tup)

def recursive_factorial(num):
    if(num > 1):
        return num * recursive_factorial(num-1)
    else:
        return num

print(recursive_factorial(6))

myname="Jaggel Haggar"
for c in myname:
    print('C:=',c)


print(range(4))

#gennerate even nummbers
even_n = [n for n in range(20) if n % 2 ==0]
print(even_n)

short_planets = [planet
                 for planet in planets
                 if len(planet) < 7]

box = [32 for n in range(9)]
print(box)
print(short_planets)