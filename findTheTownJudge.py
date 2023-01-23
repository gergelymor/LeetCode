#997. Find the Town Judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n == 1:
            return 1
        trustedpeople = dict()
        trustingpeople = dict()
        for i in range(0,len(trust)):
            trustingpeople[trust[i][0]] = True
            if trust[i][1] not in trustedpeople:
                trustedpeople[trust[i][1]] = 1
            else:
                trustedpeople[trust[i][1]] += 1
        for inhabitant in trustedpeople:
            if trustedpeople[inhabitant] == n-1 and inhabitant not in trustingpeople:
                return inhabitant
        return -1
