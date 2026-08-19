class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutive = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            if maxConsecutive < current:
                maxConsecutive = current
            if nums[i] == 0:
                current = 0
        return maxConsecutive