class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                return min(result, nums[left])
            else:
                mid = (left + right) // 2
                result = min(result, nums[mid])
                if nums[left] <= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return result