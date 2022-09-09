# Container With Most Water
'''
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

# logic: use left and right pointers
# move pointer pointing to minimum height

class Solution:
    def maxArea(self, height: List[int]) -> int:

        mx = 0
        left, right = 0, (len(height)-1)

        while left < right:
            mx = max(mx, min(height[left], height[right]) * abs(left-right))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return mx
