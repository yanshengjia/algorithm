"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
 
Constraints:
* 0 <= digits.length <= 4
* digits[i] is a digit in the range ['2', '9'].


Solution:
Backtracking
* it uses recursive calling to find a solution set by building a solution step by step, increasing levels with time, and remove the failed trials.
* backtracking algorithm uses the depth-first search method
* backtracking algorithms can often keep the space complexity linear with the input size.
"""


# TC: O(4^N), where N is the length of digits. 4 is referring to the maximum value length in the hash map (wxyz)
# SC: O(N). Recursion stack. It will only go as deep as the number of digits in the input since whenever we reach that depth, we backtrack.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letters = {
            "2": "abc",
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index: int, path: [str]):
            # if the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                res.append("".join(path))
                return # backtrack
            
            # get the letters map at current index, and scan them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # add the letter to our current path
                path.append(letter)
                # move on to the next digit
                backtrack(index + 1, path)
                # backtrack by removing the last letter in path before moving onto the next
                path.pop()
            
        # init backtracking with an empty path and starting index of 0
        backtrack(0, [])
        return res
