board = '1234_5678'
DFS = []
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

def DFS_SEARCH(board_temp,depth):
	if board_temp == goal:
		print board_temp
		print "Solution found at depth %d"%depth
		return True
	elif depth < 5:
		empty_tile=getMoves(board_temp)
		for i in slides[empty_tile]:
			temp=makeMove(board_temp,empty_tile,i)
			result = DFS_SEARCH(temp,depth+1)
			if result:
				DFS.append(temp)
				return True
	return False

		

goal =raw_input("Enter the Goal State (Enter '_' for Empty Tile) :")
DFS.append(board)
flag = DFS_SEARCH(DFS.pop(),depth)
	

if not flag:
	print "Solution not found ...."
