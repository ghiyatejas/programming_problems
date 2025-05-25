class Solution:
    def is_palindrome(self, x):
        if x < 0:
            return False
        
        reverse_num = 0
        n = x
        
        while n != 0:
            mod = n % 10
            reverse_num = reverse_num * 10 + mod
            n //= 10
        
        return x == reverse_num
