# Q6 Answer template
def solution6(arr):
    minimum = 99999
    for i in arr:
        if minimum > i:
            minimum = i
    arr.remove(minimum)
    
    if arr:
        return arr
    else:
        return [-1]
    
# arr = [4, 3, 2, 1]
arr = [10]
solution6(arr)
