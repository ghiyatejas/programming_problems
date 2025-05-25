class Solution:
    def generate_matrix(self, n):
        if n <= 0:
            return None
        
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Size of the resultant matrix
        size = n * n
        
        # Value to be stored in the matrix cell [i][j]
        value = 0
        
        # Initialize boundaries
        top, left = 0, 0
        bottom, right = n - 1, n - 1
        
        while top <= bottom and left <= right:
            # Left to right loop on topmost row
            for j in range(left, right + 1):
                if value < size:
                    matrix[top][j] = value + 1
                    value += 1
            
            # Top to bottom loop on rightmost column
            for i in range(top + 1, bottom + 1):
                if value < size:
                    matrix[i][right] = value + 1
                    value += 1
            
            # Right to left loop on bottommost row
            for j in range(right - 1, left - 1, -1):
                if value < size:
                    matrix[bottom][j] = value + 1
                    value += 1
            
            # Bottom to top loop on leftmost column
            for i in range(bottom - 1, top, -1):
                if value < size:
                    matrix[i][left] = value + 1
                    value += 1
            
            # Move the boundaries inward
            top += 1
            left += 1
            bottom -= 1
            right -= 1
        
        return matrix

# Example usage
solution = Solution()
n = 3
result = solution.generate_matrix(n)
for row in result:
    print(row)
