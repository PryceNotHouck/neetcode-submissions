class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax < rightMax:
                left += 1
                if height[left] > leftMax:
                    leftMax = height[left]
                result += leftMax - height[left]
            else:
                right -= 1
                if height[right] > rightMax:
                    rightMax = height[right]
                result += rightMax - height[right]

        return result