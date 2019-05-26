class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rowDict = {}
        
        if numRows == 1:
            return s
        
        #get the dict ready
        for row in range(numRows):
            rowDict[row] =  ''
            
        #starting state
        state = 'down'
        
        #offset for loop to start at 0
        index = -1
        
        for letter in s:
            if index == 0:
                state = 'down'
            elif index == numRows-1:
                state = 'up'
            if state == 'down':
                index += 1
            elif state == 'up':
                index -= 1
            else:
                print('something went wrong')
            rowDict[index] += letter
            
       # #print to check
       # for key, value in rowDict.items():
       #     print(str(key) + ": "+ value)
            
        zigzag = ''
        for value in rowDict.values():
            zigzag += value
            
        return zigzag
        