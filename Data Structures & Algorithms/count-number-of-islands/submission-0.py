class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        result = 0
        seen = defaultdict(list)
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1" and not seen.get((r, c), False):
                    q = deque()
                    q.append((r, c))
                    while q:
                        curr = q.popleft()
                        seen[curr] = True
                        
                        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            curr_r, curr_c = curr[0] + i, curr[1] + j
                            try:
                                if grid[curr_r][curr_c] == "1" and not seen.get((curr_r, curr_c), False):
                                    q.append((curr_r, curr_c))
                                    seen[(curr_r, curr_c)] = True
                            except IndexError:
                                pass

                    result += 1

        return result