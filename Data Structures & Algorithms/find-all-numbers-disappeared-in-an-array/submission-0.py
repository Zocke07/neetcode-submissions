class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numSet = set(nums)
        result = []
        for i in range(1, len(nums)+1):
            if i not in numSet:
                result.append(i)
        return result