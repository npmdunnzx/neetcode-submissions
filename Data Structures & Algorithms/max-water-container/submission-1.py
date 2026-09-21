class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxS = 0
        while (left < right):
            s = (right - left)*min(heights[left],heights[right])
            # print(right, left,min(heights[left],heights[right]), s )
            if maxS <= s:
                maxS = s
                if heights[left] <= heights[right]:
                    left += 1
                else:
                    right -= 1
            else:
                if heights[left] >= heights[right]:
                    right -= 1
                else:
                    left += 1
        return maxS
