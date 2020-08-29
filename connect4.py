class Connect4():

    def __init__(self):
        # numbering of grid is visualised in lines starting from bottom left
        self.grid = [i for i in range(42)]
        self.columns = [0, 0, 0, 0, 0, 0, 0]
        self.turns = 0
        self.won = False

    def play(self, col):
        if self.won: return "Game has finished!"

        position = col + self.columns[col]*7
        player = (self.turns % 2) + 1
        row = int(position / 7)

        # positions that have potential upwards or downwards diagonal win lines
        upward_diag = [
            0,1,2,3,7,8,9,10,11,14,15,16,17,18,19,
            22,23,24,25,26,27,30,31,32,33,34,38,39,40,41
        ]
        downward_diag = [
            3,4,5,6,9,10,11,12,13,15,16,17,18,19,20,
            21,22,23,24,25,26,28,29,30,31,32,35,36,37,38
        ]
       
        if position > 41:
            self.turns += 2
            return "Column full!"
        
        if self.turns % 2 == 0:
            self.grid[position] = "red"
        else: 
            self.grid[position] = "yellow"

        for i in range(col, col+15, 7):  # checking all win lines in current column
            if self.grid[i] == self.grid[i+7] == self.grid[i+14] == self.grid[i+21]:
                self.won = True
                return f"Player {player} wins!"

        for i in range(row*7,(row*7)+4):  # checking all win lines in current row
            if self.grid[i] == self.grid[i+1] == self.grid[i+2] == self.grid[i+3]:
                self.won = True
                return f"Player {player} wins!"

        if position in upward_diag:  # checking all win lines in current upward diagonal
            try:
                for i in range(position-(min(row,col)*8), position+(min(5-row,6-col)*8), 8):
                    if self.grid[i] == self.grid[i+8] == self.grid[i+16] == self.grid[i+24]:
                        self.won = True
                        return f"Player {player} wins!"
            except:
                pass

        if position in downward_diag:  # checking all win lines in current downward diagonal
            try:
                for i in range(position-(min(row,6-col)*6), position+(min(5-row,col)*6), 6):
                    if self.grid[i] == self.grid[i + 6] == self.grid[i + 12] == self.grid[i + 18]:
                        self.won = True
                        return f"Player {player} wins!"
            except:
                pass

        self.turns += 1
        self.columns[col] += 1

        return f"Player {player} has a turn"
