class Solution:
    def majority_element(self, nums):
        # Initialize majority element to None and count to 0
        maj = None
        count = 0
        
        try:
            for num in nums:
                # If count is 0, choose the current element as the new majority element
                if count == 0:
                    maj = num
                    count += 1
                else:
                    # If the current element is the same as the majority element, increment count
                    # Otherwise, decrement count
                    if num == maj:
                        count += 1
                    else:
                        count -= 1
        except Exception as ex:
            print(ex)
        
        return maj
