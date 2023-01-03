#944. Delete Columns to Make Sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleteCount = 0
        for j in range(0,len(strs[0])):
            for i in range(0, len(strs)):
                if len(strs) > i + 1 and strs[i][j] > strs[i+1][j]:
                    deleteCount = deleteCount + 1
                    break
        return deleteCount
