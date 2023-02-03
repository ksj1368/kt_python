# Q3 answer template
def solution3(store, customer):
    answer = ["no"] * len(customer)
    
    for i in range(len(customer)):
        if customer[i] in store:
           answer[i] = "yes"
                   
    return answer

#store = [2,3,7,8,9]
#customer = [7,5,9]
store = [1, 2, 3, 7, 8]
customer = [1, 5, 8, 4, 6]
solution3(store, customer)
