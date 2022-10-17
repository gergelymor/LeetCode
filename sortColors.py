#75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0,0,0]
        for i in range(0,len(nums)):
            count[nums[i]] = count[nums[i]] + 1
        for i in range(0,count[0]):
            nums[i] = 0
        for i in range(0,count[1]):
            nums[count[0]+i] = 1
        for i in range(0,count[2]):
            nums[count[0]+count[1]+i] = 2
