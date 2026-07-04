class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        solutions = []
        twoSums = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                twoSums[0 - (nums[i] + nums[j])].append((i, j))

        for i in range(len(nums)):
            if twoSums.get(nums[i], 0):
                for pair in twoSums[nums[i]]:
                    if pair[0] != i and pair[1] != i:
                        temp = [nums[i], nums[pair[0]], nums[pair[1]]]
                        temp.sort()
                        if temp not in solutions:
                            solutions.append(temp)

        return solutions