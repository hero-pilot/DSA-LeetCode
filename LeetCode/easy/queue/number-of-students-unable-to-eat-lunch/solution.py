class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        res = len(students)
        counter = {}
        for i in students:
            if i not in counter:
                counter[i] = 0
            counter[i] +=1
        
        for i in sandwiches :
            if i in counter and counter[i] >0 :
                counter[i] -=1
                res -=1
            else: 
                break
        return res