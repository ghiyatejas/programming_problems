class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0

        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0
        for i in range(len(s) - 1, -1, -1):
            val = roman_map[s[i]]
            if i == len(s) - 1 or val >= roman_map[s[i + 1]]:
                num += val
            else:
                num -= val

        return num
