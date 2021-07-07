'''
After learning about the babylonian way of calculating square roots I
Wanted to implement this into python
'''
import time


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
    prev2 = square_rrot(starting_point[1])
    prev1 = x/prev2
    #up until here this is all recycled from my previous function
    
    for i in range(100):
        prev2 = prev1
        prev1 = x/prev2
        if prev1*prev1 == x:
            return prev1
    return prev1

  
  #the following is just to time it 
mst = time.time()

for i in range(100):
    print(square_root(i))

met = time.time()

tst = time.time()

for i in range(100):
    print(math.sqrt(i))

tet = time.time()

print(f"mine was {met-mst} their's was {tet-tst}")
