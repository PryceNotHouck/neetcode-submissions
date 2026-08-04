class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        nums = self.arr
        nums.append(val)
        nums.sort()
        return nums[len(nums) - self.k]