# Q7 Answer Template
def solution7(arr):
    prev = arr[0]
    answer = [prev]
    
    for i in arr[1:]:
        if prev != i:
            answer.append(i)
            prev = i
    return answer

#arr = [1,1,3,3,0,1,1]
arr = [4,4,4,3,3]
solution7(arr)
