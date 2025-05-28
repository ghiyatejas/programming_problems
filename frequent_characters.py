def frequent_character(input_string):
    if input_string is None:
        return "Error! Input is None"
    if not isinstance(input_string, str):
        return "Error! Input must be a string"

    freq = {}
    for ch in input_string:
        if ch in freq:
            freq[ch]++;
        else:
            freq[ch] = 1;

   max_char = ''    
   max_count = 0
   for store in freq:
       if freq[store] > max_count:
            max_count = freq[store]
            max_char = store
   return max_char;
