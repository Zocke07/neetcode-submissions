class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sortedList = sorted(nums)
        return sortedList[-1] * sortedList[-2] - sortedList[1] * sortedList[0]