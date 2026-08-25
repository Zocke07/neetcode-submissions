class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letterDict = {}
        balloon = ["b", "a", "l", "o", "n"]
        result = 0
        for i in text:
            if i in letterDict:
                letterDict[i] += 1
            else:
                letterDict[i] = 1
        if set(balloon).issubset(letterDict.keys()):
            while True:
                if letterDict["b"] >= 1 and letterDict["a"] >= 1 and letterDict["l"] >= 2 and letterDict["o"] >= 2 and letterDict["n"] >= 1:
                    letterDict["b"] -= 1
                    letterDict["a"] -= 1
                    letterDict["l"] -= 2
                    letterDict["o"] -= 2
                    letterDict["n"] -= 1
                    result += 1
                else:
                    break
        return result