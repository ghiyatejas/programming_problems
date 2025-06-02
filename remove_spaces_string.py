def remove_spaces(input_string):
    if input_string is None:    
        return "Error! Input is None"
    if not isinstance(input_string, str) :
        return "Error! Input must be a string"
       
    result = ""
    for ch in input_string:
        if ch != " ":
            result += ch
    return result        

print(remove_spaces(" my name  is tejas  "))
print(remove_spaces("abcd ef gh"))  
