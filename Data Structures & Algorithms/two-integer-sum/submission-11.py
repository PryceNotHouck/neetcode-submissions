class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, n in enumerate(nums):
            sums[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in sums and sums[diff] != i:
                return [i, sums[diff]]
        return []