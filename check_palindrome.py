def palindrome_string(input_string):
    if input_string is None:
        return "Error! Input is None"
    if not isinstance(input_string, str):
        return "Error! Input must be a string"

    left = 0
    right = len(input_string) - 1

    while left < right:
        if input_string[left] != input_string[right]:
            return "Not a palindrome"
        left += 1
        right -= 1

    return "Palindrome"
