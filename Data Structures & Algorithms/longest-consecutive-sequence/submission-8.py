class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        nums = list(dict.fromkeys(nums))

        count = 1
        result = count
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                count += 1
            else:
                result = max(result, count)
                count = 1

        return max(result, count)