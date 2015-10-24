import math
evidence_dataset = { "1":['C',30,'P',9],  "2":['S',21,'M',1],
		     "3":['R',26,'M',2],  "4":['S',28,'B',10],
		     "5":['C',40,'M',14], "6":['R',35,'P',10],
	             "7":['R',27,'B',6],  "8":['S',32,'M',9],
		     "9":['C',45,'B',17], "10":['R',36,'P',7]
		   }
sum_age_C,sum_age_R,sum_age_S = [0 for dummy in range(3)]
sum_experience_C,sum_experience_R,sum_experience_S = [0 for dummy in range(3)]
count_C,count_R,count_S = [0 for dummy in range(3)]
st_age_C,st_age_R,st_age_S = [0 for dummy in range(3)]
st_exp_C,st_exp_R,st_exp_S = [0 for dummy in range(3)]
st_sum_age_C,st_sum_age_R,st_sum_age_S  = [0 for dummy in range(3)]
st_sum_experience_C,st_sum_experience_R,st_sum_experience_S  = [0 for dummy in range(3)]
gauss_age_C,gauss_age_R,gauss_age_S  = [0 for dummy in range(3)]
gauss_exp_C,gauss_exp_R,gauss_exp_S  = [0 for dummy in range(3)]
count_C_M,count_C_P,count_C_B = [0 for dummy in range(3)]
count_R_M,count_R_P,count_R_B = [0 for dummy in range(3)]
count_S_M,count_S_P,count_S_B = [0 for dummy in range(3)]

for i in range(1,len(evidence_dataset)+1): 
	if evidence_dataset[str(i)][0] == 'C':
		sum_age_C+=(evidence_dataset[str(i)][1])	
		sum_experience_C+=(evidence_dataset[str(i)][3])
		count_C+=1
	if evidence_dataset[str(i)][0] == 'R':
		sum_age_R+=(evidence_dataset[str(i)][1])	
		sum_experience_R+=(evidence_dataset[str(i)][3])	
		count_R+=1
	if evidence_dataset[str(i)][0] == 'S':
		sum_age_S+=(evidence_dataset[str(i)][1])	
		sum_experience_S+=(evidence_dataset[str(i)][3])
		count_S+=1

mean_age_C = sum_age_C/count_C
mean_age_R = sum_age_R/count_R
mean_age_S = sum_age_S/count_S

mean_experience_C = sum_experience_C/count_C
mean_experience_R = sum_experience_R/count_R
mean_experience_S = sum_experience_S/count_S

for i in range(1,len(evidence_dataset)+1):
	if evidence_dataset[str(i)][0] == 'C':
		st_age_C+=(pow(((mean_age_C)-(evidence_dataset[str(i)][1])),2))
		st_exp_C+=(pow(((mean_experience_C)-(evidence_dataset[str(i)][3])),2))
	if evidence_dataset[str(i)][0] == 'R':
		st_age_R+=(pow(((mean_age_R)-(evidence_dataset[str(i)][1])),2))
		st_exp_R+=(pow(((mean_experience_R)-(evidence_dataset[str(i)][3])),2))
	if evidence_dataset[str(i)][0] == 'S':
		st_age_S+=(pow(((mean_age_S)-(evidence_dataset[str(i)][1])),2))
		st_exp_S+=(pow(((mean_experience_S)-(evidence_dataset[str(i)][3])),2))

st_sum_age_C = math.sqrt(st_age_C/count_C)
st_sum_experience_C = math.sqrt(st_exp_C/count_C)

st_sum_age_R = math.sqrt(st_age_R/count_R)
st_sum_experience_R = math.sqrt(st_exp_R/count_R)

st_sum_age_S = math.sqrt(st_age_S/count_S)
st_sum_experience_S = math.sqrt(st_exp_S/count_S)

age  =  int(input("ENTER AGE :"))
qual =  input("ENTER QUALIFICATION :")
exp  =  int(input("ENTER EXPERIENCE :"))


	
temp_a = pow(math.e,(-0.5*pow(((age-mean_age_C)/st_sum_age_C),2)))
gauss_age_C = (temp_a*(1/((st_sum_age_C)*(math.sqrt(2*math.pi)))))
temp_b = pow(math.e,(-0.5*pow(((exp-mean_experience_C)/st_sum_experience_C),2)))
gauss_exp_C = (temp_a*(1/((st_sum_experience_C)*(math.sqrt(2*math.pi)))))
	
temp_a = pow(math.e,(-0.5*pow(((age-mean_age_R)/st_sum_age_R),2)))
gauss_age_R = (temp_a*(1/((st_sum_age_R)*(math.sqrt(2*math.pi)))))
temp_b = pow(math.e,(-0.5*pow(((exp-mean_experience_R)/st_sum_experience_R),2)))
gauss_exp_R = (temp_a*(1/((st_sum_experience_R)*(math.sqrt(2*math.pi)))))
	
temp_a = pow(math.e,(-0.5*pow(((age-mean_age_S)/st_sum_age_S),2)))
gauss_age_S = (temp_a*(1/((st_sum_age_S)*(math.sqrt(2*math.pi)))))
temp_b = pow(math.e,(-0.5*pow(((exp-mean_experience_S)/st_sum_experience_S),2)))
gauss_exp_S = (temp_a*(1/((st_sum_experience_S)*(math.sqrt(2*math.pi)))))



for i in range(1,len(evidence_dataset)+1):
	if evidence_dataset[str(i)][0] == 'C'and evidence_dataset[str(i)][2] == 'M':
		count_C_M+=1
	if evidence_dataset[str(i)][0] == 'C'and evidence_dataset[str(i)][2] == 'B':
		count_C_B+=1
	if evidence_dataset[str(i)][0] == 'C'and evidence_dataset[str(i)][2] == 'P':
		count_C_P+=1

	if evidence_dataset[str(i)][0] == 'R'and evidence_dataset[str(i)][2] == 'M':
		count_R_M+=1
	if evidence_dataset[str(i)][0] == 'R'and evidence_dataset[str(i)][2] == 'B':
		count_R_B+=1
	if evidence_dataset[str(i)][0] == 'R'and evidence_dataset[str(i)][2] == 'P':
		count_R_P+=1
	
	if evidence_dataset[str(i)][0] == 'S'and evidence_dataset[str(i)][2] == 'M':
		count_S_M+=1
	if evidence_dataset[str(i)][0] == 'S'and evidence_dataset[str(i)][2] == 'B':
		count_S_B+=1
	if evidence_dataset[str(i)][0] == 'S'and evidence_dataset[str(i)][2] == 'P':
		count_S_P+=1

P_C = (gauss_age_C) * (count_C_M / count_C) * (gauss_exp_C) * (count_C / len(evidence_dataset))
P_R = (gauss_age_R) * (count_R_M / count_R) * (gauss_exp_R) * (count_R / len(evidence_dataset))
P_S = (gauss_age_S) * (count_S_M / count_S) * (gauss_exp_S) * (count_S / len(evidence_dataset))

if P_C > P_R and P_C > P_S:
	print("PREDICTED WORKTYPE : Consultancy")
if P_S > P_C and P_S > P_R:
	print("PREDICTED WORKTYPE : Service")
if P_R > P_C and P_R > P_S:
	print("PREDICTED WORKTYPE : Research")
