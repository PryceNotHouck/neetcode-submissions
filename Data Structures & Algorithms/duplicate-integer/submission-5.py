class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        chars = set()
        for num in nums:
            if num in chars:
                return True
            chars.add(num)
        return False