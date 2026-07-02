class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            frequencies = [0] * 26
            for char in s:
                frequencies[ord(char) - ord('a')] += 1
            result[tuple(frequencies)].append(s)
        return list(result.values())