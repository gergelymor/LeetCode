#704. Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        p = r//2

        while l <= r:
            if nums[p] == target:
                return p
            elif target < nums[p]:
                r = p - 1
            else:
                l = p + 1
            p = (l + r) // 2
        return -1
