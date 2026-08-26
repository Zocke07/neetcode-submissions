class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        represent = {}
        sWords = s.split()

        if len(pattern) != len(sWords):
            return False

        for i in range(len(pattern)):
            char = pattern[i]
            word = sWords[i]

            if char in represent.keys():
                if represent[char] != word:
                    return False
            
            elif word in represent.values():
                return False
            
            else:
                represent[char] = word
    
        return True