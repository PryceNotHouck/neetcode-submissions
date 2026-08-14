class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return 0

        maximum = max(i[0] for i in intervals)
        farthest = [0] * (maximum + 1)
        for lower, upper in intervals:
            farthest[lower] = max(upper + 1, farthest[lower])

        result = []
        curr_lower, curr_upper = -1, -1
        for i in range(len(farthest)):
            if farthest[i] != 0:
                if curr_lower == -1:
                    curr_lower = i
                curr_upper = max(farthest[i] - 1, curr_upper)

            if curr_upper == i:
                result.append([curr_lower, curr_upper])
                curr_lower, curr_upper = -1, -1

        if curr_lower != -1:
            result.append([curr_lower, curr_upper])

        return result