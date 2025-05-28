 def unique_character(input_string):
    if input_string is None:
        return "Error! Input is None"
    if not isinstance(input_string, str):
        return "Error! Input must be a string"

    check = {}
    for ch in input_string:
        if ch in check:
            return false
        else:
            check[ch] = 1
    return true    

