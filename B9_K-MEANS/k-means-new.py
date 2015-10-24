import math
dataset = [ [172,175,180,189,160,162,169,145,197,128,102,103,105,120,125,134,127,129,172,174,
	     172,176,123,124,190,173,165,134,200,168,165,167,160,157,159,155,139,147,178,179],
             [45,48,65,69,73,52,89,95,67,98,76,74,72,79,80,82,67,65,63,71,
	      87,88,40,45,49,50,102,100,89,95,73,75,79,55,56,57,58,54,53,60],
	     [20,21,23,23,12,19,21,17,18,19,12,11,10,10,9,8,23,34,35,40,45,32,35,56,78,80,25,
              28,29,20,27,31,30,33,42,43,47,49,65,62],
	     [105,156,160,143,123,112,119,145,147,108,120,110,111,112,115,114,117,119,123,124,
	      127,140,141,132,133,134,137,90,89,88,100,102,109,108,123,124,126,122,121,130] ]

k = 3

cluster_1_x , cluster_1_y , cluster_1_z , cluster_1_w = [ [] for i in range(4)]
cluster_2_x , cluster_2_y , cluster_2_z , cluster_2_w = [ [] for i in range(4)]
cluster_3_x , cluster_3_y , cluster_3_z , cluster_3_w = [ [] for i in range(4)]
cluster_1 , cluster_2 , cluster_3 = [ [] for i in range(3)]
e_dist    = []
centroid_1 , centroid_2 , centroid_3 = [ [] for i in range(3)]
e_dist_1 , e_dist_2 , e_dist_3 = [ [] for i in range(3)]

def k_means(dataset): 
	prev_avg_1_x,prev_avg_1_y,prev_avg_1_z,prev_avg_1_w = [[] for i in range(4)]
	prev_avg_2_x,prev_avg_2_y,prev_avg_2_z,prev_avg_2_w = [[] for i in range(4)]
	prev_avg_3_x,prev_avg_3_y,prev_avg_3_z,prev_avg_3_w = [[] for i in range(4)]	
	
	centroid_1.append(dataset[0][0])
	centroid_1.append(dataset[1][0])
	centroid_1.append(dataset[2][0])
	centroid_1.append(dataset[3][0])

	centroid_2.append(dataset[0][len(dataset)/2])
	centroid_2.append(dataset[1][len(dataset)/2])
	centroid_2.append(dataset[2][len(dataset)/2])
	centroid_2.append(dataset[3][len(dataset)/2])

	centroid_3.append(dataset[0][len(dataset)-1])
	centroid_3.append(dataset[1][len(dataset)-1])
	centroid_3.append(dataset[2][len(dataset)-1])
	centroid_3.append(dataset[3][len(dataset)-1])

	print "Initial Centroid 1 :	" , centroid_1
	print "Initial Centroid 2 :	" , centroid_2
	print "Initial Centroid 3 :	" , centroid_3
	print "		"
	while(True):
		flag_end_1_x = 1
		flag_end_1_y = 1
		flag_end_1_z = 1
		flag_end_1_w = 1
		
		flag_end_2_x = 1
		flag_end_2_y = 1
		flag_end_2_z = 1
		flag_end_2_w = 1

		flag_end_3_x = 1
		flag_end_3_y = 1
		flag_end_3_z = 1
		flag_end_3_w = 1
		
		avg_1_x ,avg_1_y,avg_1_z,avg_1_w = [ 0 for i in range(4)]
		avg_2_x ,avg_2_y,avg_2_z,avg_2_w = [ 0 for i in range(4)]
		avg_3_x ,avg_3_y,avg_3_z,avg_3_w = [ 0 for i in range(4)]
		
		for i in range (0,40):
			e_dist_1.append(math.sqrt(pow((dataset[0][i] - centroid_1[0]),2) + pow((dataset[1][i] - centroid_1[1]),2)+ pow((dataset[2][i] - centroid_1[2]),2) + pow((dataset[3][i] - centroid_1[3]),2)))
			e_dist_2.append(math.sqrt(pow((dataset[0][i] - centroid_2[0]),2) + pow((dataset[1][i] - centroid_2[1]),2)+ pow((dataset[2][i] - centroid_2[2]),2) + pow((dataset[3][i] - centroid_2[3]),2)))
			e_dist_3.append(math.sqrt(pow((dataset[0][i] - centroid_3[0]),2) + pow((dataset[1][i] - centroid_3[1]),2)+ pow((dataset[2][i] - centroid_3[2]),2) + pow((dataset[3][i] - centroid_3[3]),2)))

			if e_dist_1[i] < e_dist_2[i] and e_dist_1[i] < e_dist_3[i] :
				cluster_1_x.append(dataset[0][i])
				cluster_1_y.append(dataset[1][i])
				cluster_1_z.append(dataset[2][i])
				cluster_1_w.append(dataset[3][i])
				e_dist.append(e_dist_1[i])
			elif e_dist_2[i] < e_dist_3[i] and e_dist_2[i] < e_dist_1[i] :
				cluster_2_x.append(dataset[0][i])
				cluster_2_y.append(dataset[1][i])
				cluster_2_z.append(dataset[2][i])
				cluster_2_w.append(dataset[3][i])
				e_dist.append(e_dist_2[i])
			elif e_dist_3[i] < e_dist_2[i] and e_dist_3[i] < e_dist_1[i] :
				cluster_3_x.append(dataset[0][i])
				cluster_3_y.append(dataset[1][i])
				cluster_3_z.append(dataset[2][i])
				cluster_3_w.append(dataset[3][i])
				e_dist.append(e_dist_3[i])
			elif e_dist_1[i] == e_dist_2[i]:
				cluster_1_x.append(dataset[0][i])
				cluster_1_y.append(dataset[1][i])
				cluster_1_z.append(dataset[2][i])
				cluster_1_w.append(dataset[3][i])
				e_dist.append(e_dist_1[i])
			elif e_dist_2[i] == e_dist_3[i]:
				cluster_2_x.append(dataset[0][i])
				cluster_2_y.append(dataset[1][i])
				cluster_2_z.append(dataset[2][i])
				cluster_2_w.append(dataset[3][i])
				e_dist.append(e_dist_2[i])
		
		cluster_1.append(cluster_1_x)
		cluster_1.append(cluster_1_y)
		cluster_1.append(cluster_1_z)
		cluster_1.append(cluster_1_w)

		cluster_2.append(cluster_2_x)
		cluster_2.append(cluster_2_y)
		cluster_2.append(cluster_2_z)
		cluster_2.append(cluster_2_w)

		cluster_3.append(cluster_3_x)
		cluster_3.append(cluster_3_y)
		cluster_3.append(cluster_3_z)
		cluster_3.append(cluster_3_w)

		print "CLUSTER 1 :	",cluster_1
		print "CLUSTER 2 :	",cluster_2
		print "CLUSTER 3 :	",cluster_3
		#print "EUCLIDEAN :	",e_dist 
		print "		"
		
		del centroid_1[0:]
		del centroid_2[0:]
		del centroid_3[0:]		
		flag_end_1_x  = cmp(prev_avg_1_x,cluster_1_x)
		flag_end_1_y  = cmp(prev_avg_1_y,cluster_1_y)
		flag_end_1_z  = cmp(prev_avg_1_z,cluster_1_z)
		flag_end_1_w  = cmp(prev_avg_1_w,cluster_1_w)

		flag_end_2_x  = cmp(prev_avg_2_x,cluster_2_x)
		flag_end_2_y  = cmp(prev_avg_2_y,cluster_2_y)
		flag_end_2_z  = cmp(prev_avg_2_z,cluster_2_z)
		flag_end_2_w  = cmp(prev_avg_2_w,cluster_2_w)

		flag_end_3_x  = cmp(prev_avg_3_x,cluster_3_x)
		flag_end_3_y  = cmp(prev_avg_3_y,cluster_3_y)
		flag_end_3_z  = cmp(prev_avg_3_z,cluster_3_z)
		flag_end_3_w  = cmp(prev_avg_3_w,cluster_3_w)

		if flag_end_1_x == 0 and flag_end_1_y == 0 and flag_end_1_z == 0 and flag_end_1_w == 0:
			if flag_end_2_x == 0 and flag_end_2_y == 0 and flag_end_2_z == 0 and flag_end_2_w == 0:		
				if flag_end_3_x == 0 and flag_end_3_y == 0 and flag_end_3_z == 0 and flag_end_3_w == 0:
					break
				
		for i in range(0,len(cluster_1_x)):
			avg_1_x+=cluster_1_x[i]
			avg_1_y+=cluster_1_y[i]
			avg_1_z+=cluster_1_z[i]
			avg_1_w+=cluster_1_w[i]
			
		centroid_1.append(avg_1_x/len(cluster_1_x))
		centroid_1.append(avg_1_y/len(cluster_1_y))
		centroid_1.append(avg_1_z/len(cluster_1_z))
		centroid_1.append(avg_1_w/len(cluster_1_w))
		print "New Centroid 1 :	" , centroid_1
		

		for i in range(0,len(cluster_2_x)):
			avg_2_x+=cluster_2_x[i]
			avg_2_y+=cluster_2_y[i]
			avg_2_z+=cluster_2_z[i]
			avg_2_w+=cluster_2_w[i]
		centroid_2.append(avg_2_x/len(cluster_2_x))
		centroid_2.append(avg_2_y/len(cluster_2_y))
		centroid_2.append(avg_2_z/len(cluster_2_z))
		centroid_2.append(avg_2_w/len(cluster_2_w))
		print "New Centroid 2 :	" , centroid_2
		
		for i in range(0,len(cluster_3_x)):
			avg_3_x+=cluster_3_x[i]
			avg_3_y+=cluster_3_y[i]
			avg_3_z+=cluster_3_z[i]
			avg_3_w+=cluster_3_w[i]
		centroid_3.append(avg_3_x/len(cluster_3_x))
		centroid_3.append(avg_3_y/len(cluster_3_y))
		centroid_3.append(avg_3_z/len(cluster_3_z))
		centroid_3.append(avg_3_w/len(cluster_3_w))
		print "New Centroid 3 :	" , centroid_3
		print "		"

		prev_avg_1_x = list(cluster_1_x)
		prev_avg_1_y = list(cluster_1_y)
		prev_avg_1_z = list(cluster_1_z)
		prev_avg_1_w = list(cluster_1_w)
		
		prev_avg_2_x = list(cluster_2_x)
		prev_avg_2_y = list(cluster_2_y)
		prev_avg_2_z = list(cluster_2_z)
		prev_avg_2_w = list(cluster_2_w)
		
		prev_avg_3_x = list(cluster_3_x)
		prev_avg_3_y = list(cluster_3_y)
		prev_avg_3_z = list(cluster_3_z)
		prev_avg_3_w = list(cluster_3_w)

		del cluster_1_x[0:]
		del cluster_1_y[0:]
		del cluster_1_z[0:]
		del cluster_1_w[0:]

		del cluster_2_x[0:]
		del cluster_2_y[0:]
		del cluster_2_z[0:]
		del cluster_2_w[0:]
		
		del cluster_3_x[0:]
		del cluster_3_y[0:]
		del cluster_3_z[0:]
		del cluster_3_w[0:]
		
		del e_dist[0:]
		del e_dist_1[0:]		
		del e_dist_2[0:]
		del e_dist_3[0:]
		
		del cluster_1[0:]
		del cluster_2[0:]
		del cluster_3[0:]	
k_means(dataset)




