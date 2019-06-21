class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        elif x < 0:
            temp = str(x)
            temp = temp.lstrip("-")
            temp = temp[::-1]
            temp = temp.lstrip("0")
            temp = "-" + temp
        else:
            temp = str(x)
            temp = temp[::-1]
            temp = temp.lstrip("0")
            
        if int(temp) < -2**31 or int(temp) > 2**31-1:
            return 0
        else:
            return int(temp)
             