def missing_number(arr):
    if arr is None:
        return "Error! Input is None"
   
    if not isinstance(arr, list):
        return "Error! Input must be a valid list"
   
    if len(arr) == 0:
        return "Error! List is empty"
   
    z = len(arr) +1
    expected_value = 0
    for i in range(1, n+1):
        expected_sum = expected_sum + i
   
    actual_sum = 0
    for i in range(len(arr)):
        actual_sum = actual_sum + arr[i]
       
    missing = expected_sum - actual_sum
