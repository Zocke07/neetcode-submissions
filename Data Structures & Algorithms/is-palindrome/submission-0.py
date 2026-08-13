class Solution:
    def isPalindrome(self, s: str) -> bool:
        letterList = []
        for i in range(len(s)):
            if s[i].isalnum() == False:
                continue
            else:
                char = s[i].lower()
                letterList.append(char)
        for j in range(len(letterList)//2):
            if letterList[j] == letterList[~j]:
                continue
            else:
                return False
        return True