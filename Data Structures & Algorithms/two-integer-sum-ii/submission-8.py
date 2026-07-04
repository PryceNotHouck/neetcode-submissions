class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0 or len(numbers) == 1:
            return []
        
        l = 0
        r = len(numbers) - 1
        while l < r:
            curr = numbers[l] + numbers[r]
            if curr < target:
                l += 1
            if curr > target:
                r -= 1
            if curr == target:
                return [l + 1, r + 1]

        return []