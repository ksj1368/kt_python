# Q5 Answer template
def solution5(n, s):
    result = 0
    answer = 0
    if n > s:
        return -1
    else:
        for i in range(1, (int(s/2 + 0.5)) + 1):
            mult = i * (s-i)
            if result < mult:
                answer = [s-i, i]
    return answer

# n, s = 2, 9
# n, s = 2, 1
n, s = 2, 8
solution5(n, s)
