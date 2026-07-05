class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        index = {}
        l = 0
        result = 0
        for r in range(len(s)):
            if s[r] in index:
                l = max(index[s[r]] + 1, l)
            index[s[r]] = r
            result = max(result, r - l + 1)
        return result