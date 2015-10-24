board = '1234_5678'
BFS = []
flag = 0
slides = (      # squares ...
   (1,3 ),      # can slide into square 0
   (0,4,2),     # can slide into square 1
   (1,5),       # can slide into square 2
   (0,4,6),     # can slide into square 3
   (1,3,5,7),   # can slide into square 4
   (2,4,8),     # can slide into square 5
   (3,7),       # can slide into square 6
   (4,6,8),     # can slide into square 7
   (5,7))       # can slide into square 8

depth = 1

def getMoves(board) :
    empty = board.find('_')
    return empty

def makeMove(board, empty, mov) :
    lbrd = list(board)
    lbrd[empty],lbrd[mov] = lbrd[mov],lbrd[empty]
    return "".join(lbrd)

goal =raw_input("Enter the Goal State (Enter '_' for Empty Tile) :") 
BFS.append(board)
moves = 1

while(depth < 5):
	count = 0
	for i in range(0,moves):
		board_test = BFS[0]	
		if board_test == goal:
			print board_test
			print "Solution Found At Level %d   " %depth
			flag = 1		
			break
		empty_tile=getMoves(board_test)
		del BFS[0]
		for i in slides[empty_tile]:
			temp=makeMove(board_test,empty_tile,i)
			BFS.append(temp)
			count+=1
	if flag==1:
		break
	else:	
		depth+=1
		moves=count
if flag==0:
	print "Solution Not Found Depth Exceeded...."

