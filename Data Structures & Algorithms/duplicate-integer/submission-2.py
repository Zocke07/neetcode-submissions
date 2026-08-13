class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if 0 <= len(nums) <= 10 ** 5:
            done = []
            for i in nums:
                if -10 ** 9 <= i <= 10 **9:
                    if i not in done:
                        done.append(i)
                        continue
                    else:
                        return True
        return False