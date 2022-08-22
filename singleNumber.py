#136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        elements = set()
        for num in nums:
            if num not in elements:
                elements.add(num)
            else:
                elements.remove(num)
        return list(elements).pop()
