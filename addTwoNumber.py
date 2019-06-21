
class Solution:
    def addTwoNumbers(self, l1, l2):
        array = []
        sum = 0
        carry = 0
        while True:
            if l1 is not None and l2 is not None:
                sum = l1.val + l2.val + carry                
                carry = 0
                l1 = l1.next
                l2 = l2.next
                if sum > 9:                    
                    carry = sum / 10
                    #print("carry: " + str(int(carry)))
                    sum = sum % 10
            elif l1 is not None:
                sum = l1.val + carry                
                carry = 0
                l1 = l1.next
                if sum > 9:                    
                    carry = sum / 10
                    #print("carry: " + str(int(carry)))
                    sum = sum % 10
            elif l2 is not None:
                sum = l2.val + carry                
                carry = 0
                l2 = l2.next
                if sum > 9:                    
                    carry = sum / 10
                    #print("carry: " + str(int(carry)))
                    sum = sum % 10
            else:
                if int(carry) > 0:
                    sum = carry
                    array.append(int(sum))
                break
            #print("sum: " + str(int(sum)))
            array.append(int(sum))
        print(array)
        return array
                
                
                
                