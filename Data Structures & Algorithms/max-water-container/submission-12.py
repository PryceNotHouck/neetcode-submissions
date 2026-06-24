# Follow Solution
# O(n) time

# Two pointer solution: initialize L at 0 and R at max to maximize width
# At each iteration, only move the pointer of the smaller value
    # If heights[L] > heights[R] --> move R left by 1
    # If heights[L] < heights[R] --> move L right by 1
    # Update result if this resulting state creates a larger area

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            distance = right - left
            height = min(heights[left], heights[right])
            if distance * height > result:
                result = distance * height

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return result