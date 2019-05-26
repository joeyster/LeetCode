class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counterDict = {}
        lengthDict = {}
        dummyString = s
        substr = ""
        
        if len(s) == 1:
            return 1;
        
        for index in range(len(s)):
            for x in dummyString:
                substr += x
                if x in counterDict:
                    counterDict.clear()
                    lengthDict[substr[:-1]] = len(substr)-1
                    substr = ''
                    dummyString = dummyString[1:]
                    break;
                else:
                    counterDict[x] = 1
                
        max = 0s
        for key, value in lengthDict.items():
            if value > max:
                max = value
        return max
        
        