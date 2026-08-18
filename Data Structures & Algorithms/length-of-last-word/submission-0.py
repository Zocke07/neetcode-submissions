class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split(" ")
        lastWord = words[-1]
        return len(lastWord)