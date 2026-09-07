class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # ['x', '+', 'D', 'C']
        record = []
        s = 0
        last_s = 0
        for i in range(len(operations)):
            if operations[i] == '+':
                last_s = s
                l = len(record)
                s = s + record[l-2]
                record.append(s)
                print(record)
            elif operations[i] == 'D':
                last_s = s
                s = s*2
                record.append(s)
            elif operations[i] == 'C':
                record.pop(-1)
                s = last_s
                if len(record) > 2:
                    last_s = record[len(record)-2]
                else:
                    last_s = 0
            else:
                last_s = s
                s = int(operations[i])
                record.append(s)

        return sum(record)
                

