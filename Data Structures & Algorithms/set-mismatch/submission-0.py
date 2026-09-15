class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numSet = {i for i in range(1, len(nums)+1)}
        twice = 0
        lost = 0
        for i in numSet:
            if nums.count(i) > 1:
                twice = i
            if i not in nums:
                lost = i
        return [twice, lost]