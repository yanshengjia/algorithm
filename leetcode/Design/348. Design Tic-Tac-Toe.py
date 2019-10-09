"""
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

Follow up:
Could you do better than O(n2) per move() operation?


Solution:
1. Everytime a player placed a chess, check current row, current column, current diagonal, current anti-diagonal. If there is a n-chess line, return player id. Else return 0.
Time: O(n) for move()

2. Record the number of chesses placed on which row/column/diagonal/anti-diagonal. Use two array to represent the number of chess at row/colum, use 2 variables to record it on diagonal/antidiagonal. If a element in array or a variable reach n, return player id.
Time: 0(1) for move()
"""


# For each chess placed, check current row, col, diagonal, anti-diagonal
# Time: O(n)
# Space: O(n^2)
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # check cur row, col, diagonal, anti-diagonal
        self.board[row][col] = player
                      
        # row
        counter = 0
        for i in range(self.n):
            if self.board[row][i] != player:
                break
            counter += 1
        if counter == self.n:
            return player
        
        # col
        counter = 0
        for i in range(self.n):
            if self.board[i][col] != player:
                break
            counter += 1
        if counter == self.n:
            return player
    
        # diagonal
        counter = 0
        if row == col:
            for i in range(self.n):
                if self.board[i][i] != player:
                    break
                counter += 1
            if counter == self.n:
                return player
                      
        # anti-diagonal
        counter = 0
        if row + col == self.n - 1:
            for i in range(self.n):
                if self.board[i][self.n - i - 1] != player:
                    break
                counter += 1
            if counter == self.n:
                return player
        return 0


# Record the number of chess in each row/col/diagonal/anti-diagonal
# Time: O(1)
# Space: O(n)
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = [0] * n
        self.col = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # for player 1, increment number by one
        # for player 2, decrement number by one
        
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row == col:
                self.diagonal += 1
            if row + col == self.n - 1:
                self.anti_diagonal += 1
        else:
            self.row[row] -= 1
            self.col[col] -= 1
            if row == col:
                self.diagonal -= 1
            if row + col == self.n - 1:
                self.anti_diagonal -= 1
        
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diagonal) == self.n or abs(self.anti_diagonal) == self.n:
            return player
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)