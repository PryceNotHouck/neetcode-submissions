class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False

        c1 = {}
        c2 = {}
        print(s1, s2)
        for i in range(len(s1)):
            c1[s1[i]] = c1.get(s1[i], 0) + 1
            c2[s2[i]] = c2.get(s2[i], 0) + 1
        return c1 == c2

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        if len(s1) > len(s2):
            return False

        for i in range(len(s2)):
            if self.isAnagram(s1, s2[i:i + len(s1)]):
                return True

        return False