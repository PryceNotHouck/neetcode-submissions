class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # print(nums)
        # nums.sort()
        # print(nums)
        # nums = set(nums)
        # print(nums)
        # nums = list(nums)
        # print(nums)

        nums.sort()
        nums = list(dict.fromkeys(nums))

        if len(nums) == 0:
            return 0
        

        count = 1
        result = count
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                count += 1
            else:
                result = max(result, count)
                count = 1

        return max(result, count)