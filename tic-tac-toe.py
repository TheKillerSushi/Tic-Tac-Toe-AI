class GAME:
    def __init__(self):
        self.turn = 0
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

        # Initialize AI
        self.ai = self.AI(self.board)

    # move is [x,y]
    def shift_board(self, move):
        if 0 <= move[0] <= 2 and 0 <= move[1] <= 2:
            if self.board[move[0]][move[1]] is None:
                if self.turn % 2 == 0:
                    self.board[move[0]][move[1]] = 1
                else:
                    self.board[move[0]][move[1]] = 0
                self.turn += 1
                if self.check_wins() == 0:
                    return -1
            return 0
        return 1

    def check_wins(self):
        possible_wins = [
            [[0, 0], [0, 1], [0, 2]], 
            [[0, 0], [1, 0], [2, 0]], 
            [[0, 0], [1, 1], [2, 2]], 
            [[2, 0], [2, 1], [2, 2]], 
            [[0, 2], [1, 2], [2, 2]], 
            [[2, 0], [1, 1], [0, 2]], 
            [[0, 1], [1, 1], [2, 1]]
        ]
        for m in possible_wins:
            if (self.board[m[0][0]][m[0][1]] == 1 and 
                self.board[m[1][0]][m[1][1]] == 1 and 
                self.board[m[2][0]][m[2][1]] == 1) or (
                self.board[m[0][0]][m[0][1]] == 0 and 
                self.board[m[1][0]][m[1][1]] == 0 and 
                self.board[m[2][0]][m[2][1]] == 0):
                self.get_board(True)
                if m[0][0] == 0:
                    print("Player 1 wins")
                else:
                    print("Player 2 wins")
                return 0
        return 1

    def get_board(self, write_board=False):
        if write_board:
            for i in self.board:
                print("-------")
                current_line = "|"
                for j in i:
                    if j is None:
                        current_line += "#"
                    if j == 1:
                        current_line += "X"
                    if j == 0:
                        current_line += "O"
                    current_line += "|"
                print(current_line)
            print("-------")
        return self.board

    class AI:
        def __init__(self, board):
            self.board = board

# Creating an instance of the game
game_instance = GAME()

# Example: accessing AI's board
print(game_instance.ai.board)
game_instance.shift_board([0,0])
print(game_instance.ai.board)