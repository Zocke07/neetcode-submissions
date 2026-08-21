class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = {}
        magazineDict = {}
        for i in ransomNote:
            if i not in ransomDict:
                ransomDict[i] = 1
            else:
                ransomDict[i] += 1
        for i in magazine:
            if i not in magazineDict:
                magazineDict[i] = 1
            else:
                magazineDict[i] += 1
        for i in ransomDict.keys():
            if i in magazineDict.keys():
                if ransomDict[i] <= magazineDict[i]:
                    continue
                else:
                    return False
            else:
                return False
        return True