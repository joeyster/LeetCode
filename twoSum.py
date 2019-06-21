class Solution:
    def twoSum(self, nums, target): 
        targetSearch = target
        index = 0               
        for number in nums: 
            targetSearch -= number
            print(targetSearch)
            if targetSearch in nums and nums.index(targetSearch) != index:
                return [index, nums.index(targetSearch)]
            index += 1
            targetSearch = target
        return [] 