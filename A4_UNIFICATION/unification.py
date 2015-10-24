unify_1 = raw_input("ENTER E1 ")
UNIFY_1 =[] 
UNIFY_2 =[]
temp_a =[]
temp_b =[]
unify_2 = raw_input("ENTER E2 ")
sub_1 =''
sub_2 =''
x = ''
y = ''
a = ''
b = ''
print "STARTING  UNIFICATION PROCESS...."
print "	"
pos = 0
seek = 0
while(unify_1[seek]!= '(' and unify_2[seek]!= '('):
	if unify_1[seek] == unify_2[seek]:
		pos+=1
	seek+=1
if unify_1[pos]!='(' or unify_2[pos]!='(':
	print  "CANNOT APPLY UNIFICATION (PREDICATES NOT MATCHING..)"
else:
	UNIFY_1.append(unify_1[0:pos])
	UNIFY_2.append(unify_2[0:pos])
	if UNIFY_1 != UNIFY_2:
		print  "CANNOT APPLY UNIFICATION  (PREDICATES NOT MATCHING..)"
	x,y = unify_1[pos+1:len(unify_1)-1].split(',')		
	a,b = unify_2[pos+1:len(unify_2)-1].split(',')	
	temp_a.append(unify_1[pos+1:len(unify_1)-1].split(','))
	temp_b.append(unify_2[pos+1:len(unify_2)-1].split(','))
	
	for i in range(len(temp_a)):
		if unify_1[0:pos+2] in temp_b[i]:
			print  "CANNOT APPLY UNIFICATION "
		elif unify_2[0:pos+2] in temp_a[i]:
			print  "CANNOT APPLY UNIFICATION "
		elif unify_1[0:pos+2]+')' in temp_b[i]:
			print  "CANNOT APPLY UNIFICATION "
		elif unify_2[0:pos+2]+')' in temp_a[i]:
			print  "CANNOT APPLY UNIFICATION "
	if y == a:
		print  "CANNOT APPLY UNIFICATION (%s) CANNOT TAKE VALUES %s and %s"%(y,x,b)
	else:	
		if x != a:
			print a+' / '+x
			if a in b:
				b = b.replace(a,x)
		if y != a:
	
			print b+' / '+y
			
			
