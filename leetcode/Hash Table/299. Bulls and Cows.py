"""
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.


Solution:
Hash Table
guess 中有多余的字符(secret 中也有这个字符但是 wrong position)，不算 cows
"""


# Time-O(N), where N is the length of guess
# Space-O(10), since secret and guess string only contain digits.
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = dict()
        for n in secret:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        a, b = 0, 0
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                a += 1
                d[guess[i]] -= 1
        
        for i in range(len(guess)):
            if guess[i] != secret[i] and guess[i] in d and d[guess[i]] > 0:
                b += 1
                d[guess[i]] -= 1
        return "{}A{}B".format(a, b)
        