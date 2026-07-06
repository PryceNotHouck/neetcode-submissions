class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        count = {}
        l = 0
        maxFrequency = 0
        result = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFrequency = max(count.values())
            
            while (r - l + 1) - maxFrequency > k:
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)

        return result