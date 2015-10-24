from random import choice
from numpy import array, dot, random

def unit_step(X):
	if X < 0:
		return 0
	elif X > 0:
		return 1
	

training_data = [
    (array([0,0,1]), 0),
    (array([0,1,1]), 0),
    (array([1,0,1]), 0),
    (array([1,1,1]), 1),
		]

itr = 0
w = random.rand(3)
errors = []
eta = 0.001
print "OUTPUT AFTER TRAINING  : "
while(True):
    iterator = 0
    itr+=1
    x, expected = choice(training_data)
    result = dot(w, x)
    error = expected - unit_step(result)
    errors.append(error)
    w += eta * error * x
    for x, expected in training_data:
	result = dot(x, w)
	if unit_step(result) ==  expected:
		iterator+=1
    if iterator == 4 :
		break
for x, expected in training_data: 
	result = dot(x, w) 
	print("{}: {} -> {}".format(x[:2], result, unit_step(result)))
print 
print "NO. OF ITERATIONS TAKEN %s WITH  ETA  %s: "%(itr,eta)

   
################### 	OUTPUT  ####################################
'''
rohan@rohan-HP-ProBook-4410s:~/Dropbox/7_SEMESTER$ python and.py
OUTPUT AFTER TRAINING  : 
[0 0]: -0.349125958171 -> 0
[0 1]: -0.0191090745277 -> 0
[1 0]: -0.309028313866 -> 0
[1 1]: 0.0209885697774 -> 1

NO. OF ITERATIONS TAKEN 15 WITH  ETA  0.2: 

rohan@rohan-HP-ProBook-4410s:~/Dropbox/7_SEMESTER$ python and.py
OUTPUT AFTER TRAINING  : 
[0 0]: -0.376182263966 -> 0
[0 1]: -0.185820947767 -> 0
[1 0]: -0.102678834368 -> 0
[1 1]: 0.0876824818311 -> 1

NO. OF ITERATIONS TAKEN 40 WITH  ETA  0.1

rohan@rohan-HP-ProBook-4410s:~/Dropbox/7_SEMESTER$ python and.py
OUTPUT AFTER TRAINING  : 
[0 0]: -0.498423781255 -> 0
[0 1]: -0.14812646386 -> 0
[1 0]: -0.00199745582844 -> 0
[1 1]: 0.348299861567 -> 1

NO. OF ITERATIONS TAKEN 1372 WITH  ETA  0.001:

'''
