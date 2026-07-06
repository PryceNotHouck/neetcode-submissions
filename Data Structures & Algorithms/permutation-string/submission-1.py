class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        return sorted(s1) == sorted(s2)

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        if len(s1) > len(s2):
            return False

        for i in range(len(s2)):
            if self.isAnagram(s1, s2[i:i + len(s1)]):
                return True

        return False