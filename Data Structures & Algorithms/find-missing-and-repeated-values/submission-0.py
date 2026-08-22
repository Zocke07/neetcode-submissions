class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numSet = set()
        repeat = 0
        missing = 0
        for group in grid:
            for num in group:
                if num not in numSet:
                    numSet.add(num)
                else:
                    repeat = num
        for i in range(1, len(grid)*len(grid)+1):
            if i not in numSet:
                missing = i
        return [repeat, missing]