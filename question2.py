#write a python programme to triple all numbers of a given list of integer.use python map.
#sample list:-[1,2,3,4,5,6,7]
#triple of list number:[3,,6,9,12,15,18,21]
nums = (1,2,3,4,5,6,7)
print("original list",nums)
result = map(lambda x:x+x+x,nums)
print("/n triple of said list numbers:")
print(list(result))