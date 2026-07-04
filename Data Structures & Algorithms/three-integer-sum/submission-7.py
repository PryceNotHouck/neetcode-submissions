class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        solutions = []
        twoSums = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                twoSums[0 - (nums[i] + nums[j])].append((i, j))
                #print(nums[i], nums[j], 0 - (nums[i] + nums[j]), (i, j))
        #print()

        for i in range(len(nums)):
            #print(nums[i])
            if twoSums.get(nums[i], 0):
                #print(nums[i], nums[twoSums[nums[i]][0]], nums[twoSums[nums[i]][1]], twoSums[nums[i]])
                for pair in twoSums[nums[i]]:
                    if pair[0] != i and pair[1] != i:
                        temp = [nums[i], nums[pair[0]], nums[pair[1]]]
                        temp.sort()
                        if temp not in solutions:
                            solutions.append(temp)

        return solutions