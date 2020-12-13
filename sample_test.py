# linear search function 
from typing import List
def linear_search(arr:List, x:int) -> int:
    """
    Time complexity of O(n)
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i 
    return -1 


def binary_search(arr:List, x:int):
    low = 0
    mid = 0 
    high = len(arr)-1 

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] == x:
             return mid 

        elif arr[mid] < x :
            low = mid + 1 
        
        else:
            high = mid - 1 
    
    return -1
