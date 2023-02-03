# Q2 Answer template

def solution2(numbers):
    answer = 0
    arr = [i for i in range(1, 10)]
    
    for n in arr:
        if n not in numbers:
            answer += n
    return answer

# numbers = [1,2,3,4,6,7,8,0]
numbers = [5,8,4,0,6,7,9]
solution2(numbers)
