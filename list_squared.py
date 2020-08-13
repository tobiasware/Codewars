import math

def list_squared(m, n):
    l = []
    
    for x in range(m, n + 1):
        divisors = set()
        for y in range(1, int(math.sqrt(x)+1)):
            if x % y == 0:
                divisors.add(y**2)
                divisors.add(int(x/y)**2)
        total = sum(divisors)
        if math.sqrt(total) == int(math.sqrt(total)):
            l.append([x, total])
    return l


print(list_squared(1,250))
