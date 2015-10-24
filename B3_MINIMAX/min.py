from Tkinter import Tk, BOTH,RIGHT,RAISED,LEFT ,W,E
from ttk import Frame, Button, Style ,Entry

class GAME:

    def get_free_positions(self):
        moves = []
        for i,v in enumerate(master.grid):
            if i =='_':
                moves.append(i)
        return moves
########################################################################
    def mark(self,marker,button):
        self.button["text"] = marker
        self.lastmoves.append(pos)
########################################################################
    def revert_last_move(self):
        self.grid[self.lastmoves.pop()] = '_'
        self.winner = None
########################################################################
    def is_gameover(self):
        win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),(1,4,7),(2,5,8), (0,4,8), (2,4,6)]
	for i,j,k in win_positions:
            if self.grid[i] == self.grid[j] == self.grid[k] and self.grid[i] != '_':
                self.winner = self.grid[i]
                return True
	if '-' not in self.grid:
            self.winner = '_'
            return True
	return False
########################################################################
    def play(self,player1,player2):
        self.p1 = player1
        self.p2 = player2
   
        for i in range(9):
           
            if i%2==0:
                Label["text"]="PLAYER HUMAN"
                self.p1.move(self)
            else:
                Label["text"]="PLAYER COMPUTER"
          	self.p2.move(self)

            if self.is_gameover():
                self.print_board()
                if self.winner == '-':
                     Label["text"]="Game over with Draw"
                else:
                    Label["text"]="Winner is %s" %self.winner
                return
########################################################################
class Human:
    def __init__(self,marker):
        self.marker = marker
        self.type = 'H'
########################################################################
    def move(self, gameinstance):

        while True:
		gameinstance.mark(self.marker,m)
########################################################################         
class AI:
    
    def __init__(self, marker):
        self.marker = marker
        self.type = 'C'

        if self.marker == 'X':
            self.opponentmarker = 'O'
        else:
            self.opponentmarker = 'X'
########################################################################
    def move(self,gameinstance):
        move_position,score = self.maximized_move(gameinstance)
        gameinstance.mark(self.marker,move_position)
	
########################################################################

    def maximized_move(self,gameinstance):
    
        bestscore = None
        bestmove = None

        for m in gameinstance.get_free_positions():
            gameinstance.mark(self.marker,m)
       
            if gameinstance.is_gameover():
                score = self.get_score(gameinstance)
            else:
                move_position,score = self.minimized_move(gameinstance)
       		
            gameinstance.revert_last_move()
           
            if bestscore == None or score > bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore
########################################################################
    def minimized_move(self,gameinstance):
        
	bestscore = None
        bestmove = None

        for m in gameinstance.get_free_positions():
            gameinstance.mark(self.opponentmarker,m)
       
            if gameinstance.is_gameover():
                score = self.get_score(gameinstance)
            else:
                move_position,score = self.maximized_move(gameinstance)
       		
            gameinstance.revert_last_move()
           
            if bestscore == None or score < bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore
########################################################################
    def get_score(self,gameinstance):
        if gameinstance.is_gameover():
            if gameinstance.winner  == self.marker:
                return 1 # Won
            elif gameinstance.winner == self.opponentmarker:
                return -1 # Opponent won
        return 0 # Draw
       
########################################################################

master = Tk()
master.title("TIC TAC TOE :")
master.style = Style()
master.configure("TButton", padding=(0, 30, 0, 30),font='serif 10')
master.configure("TFrame", background="#786")

master.columnconfigure(0, pad=3)
master.columnconfigure(1, pad=3)
master.columnconfigure(2, pad=3)
			
master.rowconfigure(0, pad=3)
master.rowconfigure(1, pad=3)
master.rowconfigure(2, pad=3)
master.rowconfigure(3, pad=3)

entry = Entry(self)
entry.grid(row=0, columnspan=4, sticky=W+E)

T1 = Button(self, text="_")
T1.grid(row=1, column=0)
T2 = Button(self, text="_")
T2.grid(row=1, column=1)
T3 = Button(self, text="_")
T3.grid(row=1, column=2)

T4 = Button(self, text="_")
T4.grid(row=2, column=0)
T5 = Button(self, text="_")
T5.grid(row=2, column=1)
T6 = Button(self, text="_")
T6.grid(row=2, column=2)
			
T7 = Button(self, text="_")
T7.grid(row=3, column=0)
T8 = Button(self, text="_")
T8.grid(row=3, column=1)
T9 = Button(self, text="_")
T9.grid(row=3, column=2)


game=GAME()    
player1 = Human("X")
player2 = AI("O")
game.play( player1, player2)
master.mainloop()
