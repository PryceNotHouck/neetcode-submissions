class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp_arr = [0] * len(nums)
        dp_arr[0] = nums[0]
        dp_arr[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp_arr[i] = max(dp_arr[i - 1], nums[i] + dp_arr[i - 2])

        return dp_arr[-1]