class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 0:
            return result
        if len(strs) == 1:
            return strs[0]
        shortestWord = min(strs, key=len)
        for index in range(len(shortestWord)):
            temp = result
            for item in range(len(strs)-1):
                if strs[item][index] == strs[item+1][index]:
                    if item == len(strs)-2:
                        result += strs[0][index]
                else:
                    break
            if temp == result:
                break
        return result 