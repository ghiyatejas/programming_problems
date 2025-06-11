def is_sorted(arr):
    if arr is None:
        return "Error! Input is None"
   
    if not isinstance(arr, list):
        return "Error! Input must be a valid list"
   
    if len(arr) == 0:
        return "Error! List is empty"
       
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
               return False
