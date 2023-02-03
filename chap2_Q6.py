# Q6 Answer template
def solution6(arr):
    minimum = arr[0]
    
    for i in arr[1:]:
        if minimum > i:
            minimum = i
    
    arr.remove(minimum)
    
    if arr:
        return arr
    else:
        return [-1]
    
arr = [4, 3, 2, 1]
#arr = [10]
solution6(arr)
