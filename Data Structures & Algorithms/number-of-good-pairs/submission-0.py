class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if i < j and nums[i] == nums[j]:
                    goodPairs += 1
        return goodPairs