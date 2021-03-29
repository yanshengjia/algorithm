"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:
* m == board.length
* n = board[i].length
* 1 <= m, n <= 6
* 1 <= word.length <= 15
* board and word consists of only lowercase and uppercase English letters.


Solution:
DFS, or more accurately, Backtracking, which is a methodology where we mark the current path of exploration, if the path does not lead to a solution, we then revert the change (i.e. backtracking) and try another path.

The skeleton of the algorithm is a loop that iterates through each cell in the grid. For each cell, we invoke the backtracking function (i.e. backtrack()) to check if we would obtain a solution, starting from this very cell.

For the backtracking function backtrack(row, col, suffix), as a DFS algorithm, it is often implemented as a recursive function. The function can be broke down into the following four steps:

Step 1). At the beginning, first we check if we reach the bottom case of the recursion, where the word to be matched is empty, i.e. we have already found the match for each prefix of the word.

Step 2). We then check if the current state is invalid, either the position of the cell is out of the boundary of the board or the letter in the current cell does not match with the first letter of the word.

Step 3). If the current step is valid, we then start the exploration of backtracking with the strategy of DFS. First, we mark the current cell as visited, e.g. any non-alphabetic letter will do. Then we iterate through the four possible directions, namely up, right, down and left. The order of the directions can be altered, to one's preference.

Step 4). At the end of the exploration, we revert the cell back to its original state. Finally we return the result of the exploration.

There is a certain code pattern for all the algorithms of backtracking. For example, one can find one template in our Explore card of Recursion II (https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2793/).
"""


# TC: O(N * 3^L) where N is the number of cells in the board and L is the length of the word to be matched.
# For the backtracking function, initially we could have at most 4 directions to explore, but further the choices are reduced into 3 (since we won't go back to where we come from). 
# As a result, the execution trace after the first step could be visualized as a 3-ary tree, each of the branches represent a potential exploration in the corresponding direction. 
# Therefore, in the worst case, the total number of invocation would be the number of nodes in a full 3-nary tree, which is about 3^L
# We iterate through the board for backtracking, i.e. there could be N times invocation for the backtracking function in the worst case.
# As a result, overall the time complexity of the algorithm would be O(N * 3^L) three to the L

# SC: O(L), L = length of the word to be matched
# The main consumption of the memory lies in the recursion call of the backtracking function. 
# The maximum length of the call stack would be the length of the word. Therefore, the space complexity of the algorithm is O(L).
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_num, col_num = len(board), len(board[0])
        
        def backtrack(row, col, suffix):
            # suffix[0] is current target letter
            # check if we reach the bottom case (bingo): we find match for each letter in the board
            if len(suffix) == 0:
                return True
            
            # check if the current is invalid, before jumping into backtracking
            if row < 0 or row >= row_num or col < 0 or col >= col_num or board[row][col] != suffix[0]:
                return False
            
            ret = False
            # mark the current choice as visited before exploring further
            board[row][col] = '#'
            # current step is valid, explore 4 direntions for current cell
            for row_delta, col_delta in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ret = backtrack(row + row_delta, col + col_delta, suffix[1:])
                # break instead of return directly to do some cleanup (revert state) afterwards
                if ret:
                    break
            
            # after each exploration, revert the visited cell back to its original state
            board[row][col] = suffix[0]
            
            # no match, return False
            return ret
        
        
        for row in range(row_num):
            for col in range(col_num):
                if backtrack(row, col, word):
                    return True
        return False
