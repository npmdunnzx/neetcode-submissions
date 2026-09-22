class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(height[left], left_max)
                s += left_max - height[left]
            else:
                right -= 1
                right_max = max(height[right], right_max)
                s += right_max - height[right]

        return s