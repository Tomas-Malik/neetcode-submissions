class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        
        zeros_stu = 0
        
        ones_stu = 0
        k = len(sandwiches)
        pt = 0
        
        for i in range(k):

            if students[i] == 0:
                zeros_stu += 1
            else:
                ones_stu +=1
        stuck = 0
        for i in sandwiches:
            
            if i == 0:
                if zeros_stu > 0:
                    zeros_stu -=1
                    stuck +=1
                else:
                    break
            else:
                if ones_stu > 0:
                    ones_stu -= 1
                    stuck +=1
                else:
                    break
        return k - stuck
            

            

            

            
        
        
        return 