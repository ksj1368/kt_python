# Q1 Answer template

def solution1(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    zero_cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt +=1
        if i == 0:
            zero_cnt +=1
    answer = [rank[cnt+zero_cnt], rank[cnt]]
    return answer
  
# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]
lottos = [0, 0, 0, 0, 0, 0]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution1(lottos, win_nums)
print(answer)
