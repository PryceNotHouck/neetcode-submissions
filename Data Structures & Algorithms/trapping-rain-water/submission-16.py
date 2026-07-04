class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        stack = []
        result = 0
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                bottom = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    result += (min(left, right) - bottom) * (i - stack[-1] - 1)
            stack.append(i)
        return result