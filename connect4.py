class Connect4:

    def __init__(self):
        self.grid = [[0]*7 for _ in range(6)]
        self.player = 1
        self.finished = False
 
    def check(self, row, col):
        # check potential vertical win line
        if row >= 3 and self.grid[row][col] == self.grid[row-1][col] == self.grid[row-2][col] == self.grid[row-3][col]:
            return True

        # check potential horizontal win lines
        for i in range(max(0,col-3), min(3,col)+1):
            if self.grid[row][i] == self.grid[row][i+1] == self.grid[row][i+2] == self.grid[row][i+3]:
                return True

        # check potential upward diagonal win lines
        for i in range(-min(3, row, col), min(1, 3-row, 4-col)):
            if self.grid[row+i][col+i] == self.grid[row+i+1][col+i+1] == self.grid[row+i+2][col+i+2] == self.grid[row+i+3][col+i+3]:
                return True

        # check potential downward diagonal win lines
        for i in range(-min(3, row, 6-col), min(1, 3-row, col-2)):
            if self.grid[row+i][col-i] == self.grid[row+i+1][col-i-1] == self.grid[row+i+2][col-i-2] == self.grid[row+i+3][col-i-3]:
                return True

    def play(self, col):
        if self.finished: return "Game has finished!\n"

        row = next((i for i in range(6) if not self.grid[i][col]), None)
        if row is None: return "\nColumn is full!\n"

        self.grid[row][col] = self.player
        
        if self.check(row,col):  # checks potential win based on current move 
            res = f"\nPlayer {self.player} wins!\n"
            self.finished = True
        else:
            res = f"\nPlayer {self.player} played into column {col}\n"

        self.player = 3 - self.player  # cycles player turn between 1 and 2
        
        return res 

    def visual(self):
        for row in reversed(self.grid):
            output = "|"
            for cell in row:
                if cell == 1:
                    output += "X|"
                elif cell == 2:
                    output += "O|"
                else:
                    output += " |"
            print(output)
            

def main():
    while True:
        game = Connect4()
        while game.finished == False:
            game.visual()
            col = int(input(f"\nPlayer {game.player}. Pick a column (0-6): ")) 
            print(game.play(col))         
        game.visual()
        print("\nCongratulations!")
        replay = input("Would you like to play again (y/n)? ")
        if replay == "n": break


main()
