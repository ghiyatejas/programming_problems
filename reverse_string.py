def reverse_string(s):
    if input_string is None:
        return "Error! Input is None"
    if not isinstance(input_string, str):
        return "Error! Input must be a string"

    # Keep left pointer at start and right pointer at end.
    left = 0
    right = len(s) - 1
   
    # Swap characters from the start and end, moving towards the center
    while left < right:
        # Swap characters at the left and right pointers
        s[left], s[right] = s[right], s[left]
       
        # Move the pointers towards the center
        left += 1
        right -= 1
   
    # Join the list of characters back into a string
    return ''.join(s)
