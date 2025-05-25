class Solution:
    def removeDuplicates(self, nums):
        try:
            if nums is None or len(nums) == 0:
                return -1
            if len(nums) == 1:
                return 1

            i = 0
            for j in range(1, len(nums)):
                if nums[j] == nums[i]:
                    continue
                i += 1
                nums[i] = nums[j]

            return i + 1

        except Exception as ex:
            print("Exception while processing the array")
            print(str(ex))
            return -1
