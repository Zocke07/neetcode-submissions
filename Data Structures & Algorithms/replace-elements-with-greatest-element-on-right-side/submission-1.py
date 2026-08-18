class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):
            if i == len(arr) - 1:
                result.append(-1)
                break
            max = 0
            for j in range(i+1, len(arr)):
                if arr[j] > max:
                    max = arr[j]
            result.append(max)
        return result