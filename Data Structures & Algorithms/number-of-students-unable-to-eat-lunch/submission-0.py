class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # sandwiches are stack, 0 is top of the stack
        # students are queue 0 is start of queue
        k = len(students)
        j = 0
        while j != k:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                j = 0
            else:
                students.append(students.pop(0))
                j +=1
            k = len(students)
        return j
            

                

            
                    
            
            
                    
                    
                
            
                 
                 
        


