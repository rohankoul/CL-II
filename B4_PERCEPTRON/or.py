from random import choice
from numpy import array, dot, random

def unit_step(X):
	if X < 0:
		return 0
	elif X > 0:
		return 1
	

training_data = [
    (array([0,0,1]), 0),
    (array([0,1,1]), 1),
    (array([1,0,1]), 1),
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
rohan@rohan-HP-ProBook-4410s:~/Dropbox/7_SEMESTER$ python or.py
OUTPUT AFTER TRAINING  : 
[0 0]: -0.11578454477 -> 0
[0 1]: 0.26909686998 -> 1
[1 0]: 0.439795539874 -> 1
[1 1]: 0.824676954624 -> 1

NO. OF ITERATIONS TAKEN 9 WITH  ETA  0.2

rohan@rohan-HP-ProBook-4410s:~/Dropbox/7_SEMESTER$ python or.py
OUTPUT AFTER TRAINING  : 
[0 0]: -0.037443821454 -> 0
[0 1]: 0.0680144468553 -> 1
[1 0]: 0.696324537022 -> 1
[1 1]: 0.801782805331 -> 1

NO. OF ITERATIONS TAKEN 17 WITH  ETA  0.1

rohan@rohan-HP-ProBook-4410s:~/Dropbox/7_SEMESTER$ python or.py
OUTPUT AFTER TRAINING  : 
[0 0]: -0.000358299877256 -> 0
[0 1]: 0.904860824171 -> 1
[1 0]: 0.464755428227 -> 1
[1 1]: 1.36997455228 -> 1

NO. OF ITERATIONS TAKEN 1359 WITH  ETA  0.001

'''
