class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0
        for index in range(len(height)-1):
            boxHeight = min(height[left], height[right])
            boxLength = right - left
            area = boxHeight * boxLength        
            if area > best:
                best = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best