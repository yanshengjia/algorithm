from typing import List

# Use a stack to simulate the collisions
# Time Complexity: O(n), where n is the number of asteroids
# Space Complexity: O(n), for the stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            survived = True # if current asteroid survived after collision

            # collision condition: current asteroid moving left, and last asteroid in stack moving right
            while stack and asteroid < 0 < stack[-1]:
                if abs(stack[-1]) < abs(asteroid): # current asteroid is heavier, last asteroid exploded
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    survived = False # both asteroids cancelled out
                    break # current asteroid exploaded, next one
                else: # current asteroid is lighter and exploded
                    survived = False
                    break # current asteroid exploaded, next one
            
            if survived:
                stack.append(asteroid)
        
        return stack