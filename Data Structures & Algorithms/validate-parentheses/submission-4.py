class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        currentOpen = []
        for i in range(len(s)):
            if s[i] in opening:
                currentOpen.append(s[i])
            else:
                if len(currentOpen) == 0:
                    return False
                else:
                    if opening.index(currentOpen[-1]) == closing.index(s[i]):
                        currentOpen.pop(-1)
                    else:
                        return False
        if len(currentOpen) == 0:
            return True
        else:
            return False
