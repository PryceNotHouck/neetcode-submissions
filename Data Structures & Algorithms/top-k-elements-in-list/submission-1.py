class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequencies = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num in counts.keys():
            frequencies[counts[num]].append(num)

        result = []
        for freq in frequencies[::-1]:
            if len(freq) != 0:
                for n in freq:
                    result.append(n)
                    if len(result) == k:
                        return result
        return []