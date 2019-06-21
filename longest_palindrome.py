class Solution:
    def longestPalindrome(self, s: str) -> str:
        dict = {}
        for elem in range(len(s)):
            temp = ""
            for char in range(elem,len(s)):
                temp = temp + s[char]
                if temp not in dict:
                    reverseTemp = temp[::-1]
                    if reverseTemp == temp:
                        dict[temp] = len(temp)
        best = ""
        for key in dict:
            if len(key) > len(best):
                best = key
        return best
             