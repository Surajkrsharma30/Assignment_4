#------------------Assignment 4-------------------
#write a python program to square the elememt to a list using map() function.
#sample list:[4,5,2,9]
#output:square the element of the list :[16,25,4,81]

def square_num(n):
    return n*n
nums = [4,5,2,9]
print("original list:",nums)
result = map(square_num,nums)
print("square the element of tghe said list using map():")
print(list(result))