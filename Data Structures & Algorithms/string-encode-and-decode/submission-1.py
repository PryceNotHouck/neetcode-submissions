class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += s
            encoded += "."
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        temp = ""
        for char in s:
            if char == '.':
                decoded.append(temp)
                temp = ""
            else:
                temp += char
        return decoded