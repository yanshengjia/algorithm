"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)


Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]


Solution:
Since the length of the prison is constant, so the number of states which prison can have is limited.
For this question, prison length is 8, the max number of states is 2^8 = 256.
We can use a hashmap to record the state and its corresponding date, if the state repeats, we can get the period of the prison states. 
"""


# Time: O(2^N), N is the length of cells
# Space: O(N * 2^N)
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        l = len(cells)
        if l <= 2 or N == 0:
            return cells
        
        def change(cells):
            new_state = [0] * l
            for i in range(1, l - 1):
                if cells[i-1] == cells[i+1]:
                    new_state[i] = 1
            return new_state
        
        d = dict()
        first_day = ''.join([str(i) for i in cells])
        d[first_day] = 1
        date = 1
        t = cells
        flag = False
        
        for i in range(N):
            t = change(t)
            date += 1
            state = ''.join([str(i) for i in t])
            if state not in d:
                d[state] = date
            else:
                flag = True
                loop = date - d[state]
                start = d[state]
                break
        
        if flag:
            N = start + (N - start) % loop
            for i in range(N):
                cells = change(cells)
        else:
            cells = t
        return cells
