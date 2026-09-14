class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        dct = {}
        for i in range(numCourses):
            dct[i] = []
        for i in prerequisites:
            course = i[0]
            prereq = i[1]
            dct[course].append(prereq)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if dct[crs] == []:
                return True

            visiting.add(crs)

            for prereq in dct[crs]:
                if not dfs(prereq):
                    return False
            visiting.remove(crs)
            dct[crs] = []
            return True

        for crs, prereq in dct.items():
            if not dfs(crs):
                return False
        return True

        