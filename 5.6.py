'''
5.6 (Bubble Sort) Sorting data (i.e. placing data into some particular order, such as ascending or descending)
is one of the most important computing applications. Python lists provide a sort meth- od. In this exercise, 
readers implement their own sorting function, using the bubble-sort method. In the bubble sort (or sinking sort), 
the smaller values gradually “bubble” their way upward to the top of the list like air bubbles rising in water, 
while the larger values sink to the bottom of the list. The pro- cess that compares each adjacent pair of elements 
in a list in turn and swaps the elements if the second element is less than the first element is called a pass. 
The technique makes several passes through the list. On each pass, successive pairs of elements are compared. 
If a pair is in increasing order, bubble sort leaves the values as they are. If a pair is in decreasing order, 
their values are swapped in the list. After the first pass, the largest value is guaranteed to sink to the highest
index of a list. After the second pass, the second largest value is guaranteed to sink to the second highest index 
of a list, and so on. Write a program that uses the function bubbleSort to sort the items in a list.
'''

def bubbleSort(item_list):
    for i in range(0, len(item_list)):
        for j in range(i, len(item_list)):
            if item_list[i]>item_list[j]:
                temp = item_list[j];
                item_list[j] = item_list[i]
                item_list[i] = temp
    return item_list

my_list = [12, 43, 13, 5, 67, 94, 32]
print(my_list)
my_list_sorted = bubbleSort(my_list)
print(my_list_sorted)
