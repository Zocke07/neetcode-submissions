class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        results = []
        for i in range(k):
            maxNum = 0
            maxCount = 0
            for num, count in counts.items():
                if count > maxCount:
                    maxNum = num
                    maxCount = count
            results.append(maxNum)
            counts.pop(maxNum)
        return results