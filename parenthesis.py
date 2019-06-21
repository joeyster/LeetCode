class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }
        memo = []
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        if s[0] not in dictionary:
            return False
        
        for charIndex in range(len(s)):
            if s[charIndex] in dictionary: #if open
                memo.append(s[charIndex])
            else: #if close
                if s[charIndex] == dictionary[memo[-1]]:
                    memo.pop()
                else: 
                    return False
        if len(memo) != 0:
            return False
        return True
                