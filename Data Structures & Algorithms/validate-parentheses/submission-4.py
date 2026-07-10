class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 1:
            return False

        pairs = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []

        for p in s:
            if p in pairs.keys():
                stack.append(p)
            elif stack:
                if p == pairs.get(stack[-1], "."):
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
        return len(stack) == 0