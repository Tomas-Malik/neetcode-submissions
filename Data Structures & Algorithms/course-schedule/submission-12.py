class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        done = set()
        not_done = {}
        for i in range(numCourses):
            not_done[i] = []
        for i in prerequisites:
            course = i[0]
            prereq = i[1]
            not_done[course].append(prereq)
            
        last_size = len(done)
        new_size = -1
        while numCourses > 0 and (last_size != new_size):
            last_size = len(done)
            print(done)
            for key, val in not_done.items():
                
                for j in range(len(val)-1,-1,-1):
                    if not val:
                        break
                    
                    if val[j] in done:
                        val.pop(j)
                if not val:
                    done.add(key)
                    
                    
            new_size = len(done)
        
        if len(done) < numCourses:
            return False
        else:
            return True
            






        
        