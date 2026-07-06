class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        if len(s) < len(t):
            return ""
        if s == t:
            return s

        countS = {}
        countT = {}
        for c in t:
            countS[c] = 0
            countT[c] = countT.get(c, 0) + 1
        
        #print(countT)
        result = ""
        l = 0
        for r in range(len(s)):
            #print(r, l, s[l:r+1])
            
            if s[r] in t:
                countS[s[r]] += 1
                while s[l] not in countT or countS[s[l]] > countT[s[l]]:
                    if s[l] in t:
                        countS[s[l]] -= 1
                    l += 1
            
            if all(countS[c] >= countT[c] for c in countT.keys()):
                while s[l] not in t:
                        l += 1
                if len(result) > len(s[l:r + 1]) or not result:
                    #print("updated")
                    result = s[l:r + 1]
            #print(r, l, s[l:r+1])
            #print()

        return result