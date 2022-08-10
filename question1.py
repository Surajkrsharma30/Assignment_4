#write a python program to create a lambda function that adds 25 to a given number passed in a argument.
#sample input:10
#sample output:35
def add(x):
    return lambda num:x+num
num = 10  #int(input("enter any number to add with 25"))
result = add(25)
print("result :",result(num))