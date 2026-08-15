class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size

        runningLeft = 1
        for i in range(size):
            result[i] *= runningLeft
            runningLeft *= nums[i]
        
        runningRight = 1
        for i in range(size):
            result[~i] *= runningRight
            runningRight *= nums[~i]
        
        return result