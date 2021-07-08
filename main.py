import math
import time



def square_root(x):
    perfect_squares = []
    for i in range(100):
        perfect_squares.append(i*i)
       
    for e in range(len(perfect_squares)):
        #this is just to quickly return a perfect cube should it be so
        if x == perfect_squares[e]:
            return e
        
    starting_point = [10000, -1]
    for i in perfect_squares:
        if abs(x-i) < starting_point[0]:
            starting_point = [abs(x-i), i]
    prev = square_root(starting_point[1]) - starting_point[0]
    depth = 0
    '''
    prev will be updated many times
    i.e 
    for sqrt(2)
    starts with 1
    it will add 0.1 until it gets to 1.5 then it knows
    it has gone to far
    it will back track and set depth to 0.01
    it will then begin with 1.41 and so forth until it reaches the correct value
    '''
    
    for i in range(100):
        if prev**2 < x:
            prev += 1*10**depth
        if prev**2 > x:
            prev -= 1*10**depth
            depth-=1
        if prev**2 == x:
            return prev
    return prev


results_file = open("sqrt_results.txt", "a")


#the next two arrays are for recording the results within the program so 
#that the averages can be calculated in the end
my_times  = []

their_times = []



# the following is just to time it
def take_time():
	global my_times, their_times
	print("#", end = "")
	mst = time.time()

	for i in range(100):
	    square_root(i)

	met = time.time()

	tst = time.time()

	for i in range(100):
	    math.sqrt(i)

	tet = time.time()

	results_file.write(f"Mine was {met - mst} Their's was {tet - tst}\n")
	my_times.append(met-mst)
	their_times.append(tet- tst)
	
for i in range(100):
	
	take_time()
	#this time.sleep is so that the cpu will have a chance to chill out a bit
	#after all this "monster computing"
	#Just wanted to make sure that the tests were all in the same conditions
	
#the following is for calculating the average time
sum_of_my = 0
sum_of_theirs = 0

for i in my_times:
	sum_of_my += i
for i in their_times:
	sum_of_theirs += i
	
	
results_file.write(f"The average for My Times was {sum_of_my/len(my_times)}\nThe average for Their Times was {sum_of_theirs/len(their_times)}")
