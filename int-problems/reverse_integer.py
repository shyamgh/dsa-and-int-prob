'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

 

Constraints:

    -231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:

        # if type(x) > (2**31 -1) or x < (-2**31):
        if type(x) is not int:
            return 0

        # remove last zero if present
        if x % 10 == 0:
            x = int(x/10)

        if x < 0:
            # make it positive, convert to string and reverse
            y = str(x * (-1))[::-1]
            try:
                x = int(y) * (-1)  # again make it negative
            except:
                x = 0
        elif x == 0:
            return 0
        else:
            y = str(x)[::-1]  # convert to string and reverse
            try:
                x = int(y)  # again make it negative
            except:
                x = 0

        # after reverse verify if number is valid int
        if x > (2**31 - 1) or x < (-2**31):
            x = 0

        return x
