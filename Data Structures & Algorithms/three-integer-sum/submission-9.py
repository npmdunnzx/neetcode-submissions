class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        
        for i in range(n - 2):
            # Nhánh cắt 1: Số nhỏ nhất > 0 thì không bao giờ tổng bằng 0
            if nums[i] > 0:
                break
                
            # Bỏ qua phần tử trùng lặp cho vị trí i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Nhánh cắt 2: Tổng 3 số nhỏ nhất lớn hơn 0 -> dừng vòng lặp
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
                
            # Nhánh cắt 3: Tổng nums[i] với 2 số lớn nhất vẫn < 0 -> thử i tiếp theo
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                tong = nums[i] + nums[left] + nums[right]
                
                if tong == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    # Bỏ qua trùng lặp ở 2 đầu con trỏ
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif tong > 0:
                    right -= 1
                else:
                    left += 1
                    
        return ans