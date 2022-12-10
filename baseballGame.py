#682. Baseball Game

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            print(record)
            if record and op == "D":
                record.append(int(2*record[len(record)-1]))
            elif record and op == "C":
                del record[-1]
            elif len(record) > 1 and op == "+":
                record.append(int(record[len(record)-2])+int(record[len(record)-1]))
            else:
                record.append(int(op))
        return sum(record)
