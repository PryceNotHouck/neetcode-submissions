class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites:
            return True
        
        depends = defaultdict(list)
        for i in range(numCourses):
            depends[i] = []

        for course, prereq in prerequisites:
            depends[course].append(prereq)

        visited = set()
        for course in range(numCourses):
            if not len(depends[course]):
                continue

            stack = [(course, 0)]
            visited.add(course)
            while stack:
                c, i = stack[-1]

                if i == len(depends[c]):
                    visited.remove(c)
                    depends[c] = []
                    stack.pop()
                    continue

                pre = depends[c][i]
                stack[-1] = (c, i + 1)

                if pre in visited:
                    return False

                if not len(depends[pre]):
                    continue

                visited.add(pre)
                stack.append((pre, 0))

        return True