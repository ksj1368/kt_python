# Q4 Answer Template
def solution4(arr):
    cnt = 0
    temp = max(arr)
    
    while cnt != len(arr):
        for i in arr:
            if temp%i == 0:
                cnt +=1
            else: 
                cnt = 0
                temp +=1
                break
    return temp

#arr = [2,6,8,14]
arr = [1,2,3]
solution4(arr)
