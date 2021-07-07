import math
import time

def absolute(x):
    if x < 0:
        return x*-1
    return x

def square_root(x):
    perfect_squares = []
    for i in range(100):
        perfect_squares.append(i*i)
    for e in range(len(perfect_squares)):
        if x == perfect_squares[e]:
            return e
    starting_point = [10000, -1]
    for i in perfect_squares:
        if abs(x-i) < starting_point[0]:
            starting_point = [abs(x-i), i]
    prev1 = square_root(starting_point[1])
    prev2 = prev1 - starting_point[0]
    depth = 0
    for i in range(100):
        if prev2**2 < x:
            prev2 += 1*10**depth
        if prev2**2 > x:
            prev2 -= 1*10**depth
            depth-=1
        if prev2**2 == x:
            return prev2
    return prev2


mst = time.time()

for i in range(100):
    print(square_root(i))

met = time.time()

tst = time.time()

for i in range(100):
    print(math.sqrt(i))

tet = time.time()

print(f"mine was {met-mst} their's was {tet-tst}")

