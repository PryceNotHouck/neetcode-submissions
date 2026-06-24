class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        
        for i in range(len(heights) - 1):
            for j in range(len(heights) - 1, i, -1):
                distance = j - i
                height = min(heights[i], heights[j])
                if distance * height > result:
                    result = distance * height
        
        return result