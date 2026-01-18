# lists exercises
scores =  [9,3,5,2,5]

primes = [2,3,5,7,9,11]

vehicles = [
    ["bmw","mercedes","honda","tesla"],
    ["suzuki","yamaha","triumph"]
]
my_faves = [2,"seeds",34]

#first prime
primes[0]
print(primes[0])
#first 5 elements of prime
print(primes[:5])
#4th and 5th elements of prime
print(primes[3:5])
#print from 4th element to the end
print(primes[3:])
#last prime
print(primes[-1])
#last 3 elements
print(primes[:-3])
# primes[5] = 13
# print(primes)
# primes = [-2,-3,-5] + primes
#
# print(len(primes))
#
# print(primes)
# primes=primes[-5:-1]+primes

# print(primes)
# print(sorted(primes))

x = 9.0 +3j
print(x.imag)
y = 4
# print(y.bit_length())
primes.append(31)
# print(primes)
# help(primes.append)
primes.pop()

planets = ['Mercury','Venus','Earth','Jupiter','Mars','Jupiter','Saturn','Uranus','Neptune','Sun']
planets.append('Malacandra')
print((planets))
# print(planets.pop())

if "Sun" in planets:
    print("Sun is part of planets")
else:
    print("Sun is NOT part of the planets")

help(planets)
ext_plan=['SQ100','XQ120','ZQ300']
print(planets.count('Jupiter'))
planets.extend(ext_plan)
# print(primes.count(1))
print(planets)

t_prime = (2,3,5,7,11,13,17,19)

x = 0.25
print(x.as_integer_ratio())
s = 4
t = 8
print("s:",s,"t:",t)
s,t = t,s
print("s:",s,"t:",t)


prty = ["adele","Shimma","Seun","Shamrock","Stardust"]
print( (len(prty)//2)+1)

print(prty.index("Shamrock"))