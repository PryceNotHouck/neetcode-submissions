from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = []

        for string in strs:
            s1 = sorted(string)
            placed = False
            for sub in sublists:
                if s1 == sorted(sub[0]):
                    sub.append(string)
                    placed = True
                    break
            if not placed:
                sublists.append([string])

        return sublists