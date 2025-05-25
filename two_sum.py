class Solution:
    def twoSum(self, numbers, target):
        indexes = [-1, -1]
        try:
            if numbers is not None and len(numbers) > 1:
                i, j = 0, len(numbers) - 1
                while i < j:
                    total = numbers[i] + numbers[j]
                    if total == target:
                        indexes[0] = i + 1
                        indexes[1] = j + 1
                        break
                    elif total > target:
                        j -= 1
                    else:
                        i += 1
        except Exception as ex:
            print(str(ex))
        return indexes
