class Solution:
    def product_except_self(self, nums):
        if nums is None or len(nums) == 0:
            return None
        
        # Initialize the left product array
        L = [0] * len(nums)
        # Initialize the right product array
        R = [0] * len(nums)
        # Initialize the answer array
        answer = [0] * len(nums)
        
        # Construct the L array
        L[0] = 1
        for i in range(1, len(nums)):
            L[i] = L[i - 1] * nums[i - 1]
        
        # Construct the R array
        R[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            R[i] = R[i + 1] * nums[i + 1]
        
        # Construct the answer array
        for i in range(len(nums)):
            answer[i] = L[i] * R[i]
        
        return answer

# Example usage
solution = Solution()
nums = [1, 2, 3, 4]
result = solution.product_except_self(nums)
print("Product except self:", result)
