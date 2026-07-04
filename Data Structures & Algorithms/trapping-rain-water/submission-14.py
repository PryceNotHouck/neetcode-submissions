class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l = 0
        r = len(height) - 1
        lMax = height[l]
        rMax = height[r]
        result = 0

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                result += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                result += rMax - height[r]
        return result