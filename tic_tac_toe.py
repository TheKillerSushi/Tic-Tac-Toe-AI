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

    class AI:
        def __init__(self, board):
            self.turn = -1
            self.board = board
            self.possible_wins = [
            [[0, 0], [0, 1], [0, 2]], 
            [[0, 0], [1, 0], [2, 0]], 
            [[0, 0], [1, 1], [2, 2]], 
            [[2, 0], [2, 1], [2, 2]], 
            [[0, 2], [1, 2], [2, 2]], 
            [[2, 0], [1, 1], [0, 2]], 
            [[0, 1], [1, 1], [2, 1]],
            [[1, 0], [1, 1], [1, 2]]
        ]
            
        def check_win(self,square):
            # check if win
            board = self.board
            
            t = 0
            for p in self.possible_wins:
                if ((board[square[0]][square[1]] == None and square == p[0] and board[p[1][0]][p[1][1]] == 0 and board[p[2][0]][p[2][1]] == 0) or 
                    (board[p[0][0]][p[0][1]] == 0 and board[square[0]][square[1]] == None and square == p[1] and board[p[2][0]][p[2][1]] == 0) or
                    (board[p[0][0]][p[0][1]] == 0 and board[p[1][0]][p[1][1]] == 0 and board[square[0]][square[1]] == None and square == p[2])):
                        t += 1
                        #return True
            if t >= 1:
                 print("Win ", t)
                 return True, t
            else:
                 print("No Win ", t)
                 return False, 0
        
        def check_middle(self,square):
            # check middle
            if self.board[square[0]][square[1]] == None and square[0] == 1 and square[1] == 1: 
                print("Yes Middle")
                return True
            else:
                print("No Middle") 
                return False
        
        def check_block(self,square):
            board = self.board
            t = 0
            for p in self.possible_wins:
                if ((board[square[0]][square[1]] == None and square == p[0] and board[p[1][0]][p[1][1]] == 1 and board[p[2][0]][p[2][1]] == 1) or 
                    (board[p[0][0]][p[0][1]] == 1 and board[square[0]][square[1]] == None and square == p[1] and board[p[2][0]][p[2][1]] == 1) or
                    (board[p[0][0]][p[0][1]] == 1 and board[p[1][0]][p[1][1]] == 1 and board[square[0]][square[1]] == None and square == p[2])):
                        t += 1                
            if t >= 1:
                print("Blocks ", t)
                return True, t
            else:
                print("Does not block")
                return False, 0
        
        def check_create_win(self,square):
            board = self.board
            t = 0
            for p in self.possible_wins:
                # check if creating a win opportunity
                if ((board[square[0]][square[1]] == None and square == p[0] and board[p[1][0]][p[1][1]] == None and board[p[2][0]][p[2][1]] == 0) or
                    (board[square[0]][square[1]] == None and square == p[0] and board[p[1][0]][p[1][1]] == 0 and board[p[2][0]][p[2][1]] == None) or 
                    (board[p[0][0]][p[0][1]] == None and board[square[0]][square[1]] == None and square == p[1] and board[p[2][0]][p[2][1]] == 0) or
                    (board[p[0][0]][p[0][1]] == 0 and board[square[0]][square[1]] == None and square == p[1] and board[p[2][0]][p[2][1]] == None) or
                    (board[p[0][0]][p[0][1]] == None and board[p[1][0]][p[1][1]] == 0 and board[square[0]][square[1]] == None and square == p[2]) or
                    (board[p[0][0]][p[0][1]] == 0 and board[p[1][0]][p[1][1]] == None and board[square[0]][square[1]] == None and square == p[2])) :
                        t += 1
            if t > 0:
                 print("Creates ", t, " win(s)")
                 return True, t
            else:
                 print("No wins made")
                 return False, 0

        def allow_enemy_create_win(self,square):
            board = self.board
            t = 0
            for p in self.possible_wins:
                # check if creating a win opportunity
                if ((board[square[0]][square[1]] == None and square == p[0] and board[p[1][0]][p[1][1]] == None and board[p[2][0]][p[2][1]] == 1) or
                    (board[square[0]][square[1]] == None and square == p[0] and board[p[1][0]][p[1][1]] == 1 and board[p[2][0]][p[2][1]] == None) or 
                    (board[p[0][0]][p[0][1]] == None and board[square[0]][square[1]] == None and square == p[1] and board[p[2][0]][p[2][1]] == 1) or
                    (board[p[0][0]][p[0][1]] == 1 and board[square[0]][square[1]] == None and square == p[1] and board[p[2][0]][p[2][1]] == None) or
                    (board[p[0][0]][p[0][1]] == None and board[p[1][0]][p[1][1]] == 1 and board[square[0]][square[1]] == None and square == p[2]) or
                    (board[p[0][0]][p[0][1]] == 1 and board[p[1][0]][p[1][1]] == None and board[square[0]][square[1]] == None and square == p[2])) :
                        t += 1
            if t > 0:
                 print("Creates Enemies ", t, " win(s)")
                 return True, t
            else:
                 print("No wins made")
                 return False, 0
        
        def constant_checks(self,square):
            num_checks = 0
            if (((self.board[0][0] == 1 and self.board[2][2] == 1) and square[0] == 0 and square[1] == 1) or ((self.board[0][2] == 1 and self.board[2][0] == 1) and square[0] == 0 and square[1] == 1)) and self.board[1][1] == 0 and self.turn == 3:
                num_checks += 1
            if ((self.board[1][0] == 1 or self.board[0][1] == 1) and self.board[0][0] == None and [square[0],square[1]] == [0,0]) or ((self.board[2][1] == 1 or self.board[1][2] == 1) and self.board[2][2] == None and [square[0],square[1]] == [2,2]):
                num_checks += 1
            if (self.board[0][0] == 1 and self.board[2][2] == 1 and self.board[1][1] == 0 and [square[0], square[1]] == [0, 1]) or (self.board[0][2] == 1 and self.board[2][0] == 1 and self.board[1][1] == 0 and [square[0], square[1]] == [0, 1]):
                num_checks += 1
            if ((self.board[1][0] == 1 and self.board[2][1] == 1 and (self.board[0][0] == 0 or self.board[2][2] == 0)) or (self.board[0][1] == 1 and self.board[1][2] == 1 and (self.board[2][2] == 0 or self.board[0][0] == 0))) and [square[0],square[1]] == [1,1]:
                num_checks += 1
            if ([square[0],square[1]] == [0,2] and self.board[1][0] == 1 and self.board[2][1] == 1 and self.board[0][0] == 0) or ([square[0],square[1]] == [2,0] and self.board[0][1] == 1 and self.board[1][2] == 1 and self.board[0][0] == 0) or ([square[0],square[1]] == [2,0] and self.board[0][1] == 1 and self.board[1][2] == 1 and self.board[2][2] == 0) or ([square[0],square[1]] == [0,2] and self.board[1][0] == 1 and self.board[2][1] == 1 and self.board[2][2] == 0):
                num_checks += 2
            if num_checks > 0:
                return True, num_checks
            return False, 0
        
        def check_empty(self,square):
            if self.board[square[0]][square[1]] == None:
                return True
            return False
        # IMPORTANT: CHECKS SQUARE's VALUE per MOVE
        def check_square(self,square):

            check_score = 0
            possible_wins = self.possible_wins
            
            # Check square empty
            if not self.check_empty(square): 
                return -1
            
            # check if its a win:
            r = self.check_win(square)
            check_score += 65536 * r[1]

            # check that middle is empty
            r = self.check_middle(square)
            if r: check_score += 4

            # check if blocking a win ------------------- basically check win but with 0's set to 1
            r = self.check_block(square)
            if r[0]: check_score += 1000 * r[1]

            # check if creating a win possibility ------------------------- basically check win but it has 2 None's
            r = self.check_create_win(square)
            if r[0]: check_score += 100 * r[1]

            # check if it creates a win for the enemy
            r = self.allow_enemy_create_win(square)
            if r[0]: check_score += 33 * r[1]

            # check glitched positions that need manual checking
            r = self.constant_checks(square)
            if r[0]: check_score += 500 * r[1]

            # check if the opponent blocks a win and creat
            # RETURN FINAL SCORE OF SQUARE
            return check_score

            
        def find_move(self,):
            self.turn += 2
            best_move = [None, None, -1]
            for j in range(3):
                for i in range(3):
                    p = self.check_square([j,i])
                    if p > best_move[2]:
                        best_move = [j, i, p]
                    print()
            return [best_move[0],best_move[1]]
    
    # move is [x,y]
    def shift_board(self, move):
        if 0 <= move[0] <= 2 and 0 <= move[1] <= 2:

            if self.board[move[0]][move[1]] is None:
                if self.turn % 2 == 0:
                    self.board[move[0]][move[1]] = 1
                else:
                    self.board[move[0]][move[1]] = 0
                self.ai.board = self.board
                self.turn += 1
                self.ai.turn = self.turn
                if self.turn == 9:
                    print("TIE")
                    return True
                if self.check_wins() == True:
                    return True
        
            return False
        return False

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
                    print("The AI wins")
                else:
                    print("Player 1 wins")
                return True
        return False

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
    
g = GAME()
used = ["[, ]"]
while not g.check_wins() and g.turn != 9:
    m = ""
    n = ""
    while "[" + m + ", " + n + "]" in used:
        while m not in ["0", "1", "2"] or n not in ["0", "1", "2"]:
            m = input("1: ")
            n = input("2: ")
            print()
        if f"[{m}, {n}]" not in used:
            used.append(f"[{m}, {n}]")
            break
        else:
            m = ""
            n = ""


    g.shift_board([int(m), int(n)])
    g.get_board(True)
    if g.turn >= 9:
        break
    AI_move = g.ai.find_move()
    used.append(str(AI_move))
    g.shift_board(AI_move)
    g.get_board(True)
