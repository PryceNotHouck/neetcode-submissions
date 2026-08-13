class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        result = []
        intervals = sorted(intervals)
        lower, upper = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] == lower or intervals[i][0] <= upper:
                upper = max(upper, intervals[i][1])
            else:
                result.append([lower, upper])
                lower = intervals[i][0]
                upper = intervals[i][1]
        result.append([lower, upper])

        return result