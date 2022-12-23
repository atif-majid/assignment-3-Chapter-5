'''
5.3 Use a list to solve the following problem: Read in 20 numbers. 
As each number is read, print it only if it is not a duplicate of a number already read.
'''

num_list = []
for i in range(0,20):
    num_temp = int(input("Enter a number: "))
    bFound = False
    for j in range(0, len(num_list)):
        if num_list[j]==num_temp:
            bFound = True
    if not bFound:
        print(f"{num_temp} is not in the list")
    num_list.append(num_temp)
