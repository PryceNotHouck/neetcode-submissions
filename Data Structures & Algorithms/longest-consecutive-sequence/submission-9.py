class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        count = 0

        for num in nums:
            if num - 1 not in nums:
                count += 1
                i = 1
                while num + i in nums:
                    count += 1
                    i += 1
                result = max(result, count)
                count = 0

        return result