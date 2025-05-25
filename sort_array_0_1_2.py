class Solution:
    def sort_colors(self, nums):
        if nums is None or len(nums) < 3:
            return
        
        # Initialize pointers
        low, mid = 0, 0
        high = len(nums) - 1
        
        # Traverse the list
        while mid <= high:
            if nums[mid] == 0:
                # Swap nums[low] and nums[mid]
                self.swap(nums, low, mid)
                low += 1
                mid += 1
            elif nums[mid] == 2:
                # Swap nums[mid] and nums[high]
                self.swap(nums, mid, high)
                high -= 1
            else:
                mid += 1

    def swap(self, nums, index1, index2):
        if nums[index1] != nums[index2]:
            nums[index1], nums[index2] = nums[index2], nums[index1]

# Example usage
solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sort_colors(nums)
print("Sorted colors:", nums)
