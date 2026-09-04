class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        j =-1
        for i in operations:
            if i =="C":
                record.pop()
                j -=1
            elif i =="D":
                record.append(record[j] *2)


print(mate(["5","2","C","D","+"]))
    