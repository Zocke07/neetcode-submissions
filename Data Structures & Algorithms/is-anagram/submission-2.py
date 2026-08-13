class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = set(s)
        second = set(t)
        firstList = sorted(first)
        secondList = sorted(second)
        if firstList == secondList:
            for i in firstList:
                if s.count(i) == t.count(i):
                    continue
                else:
                    return False
            return True
        return False