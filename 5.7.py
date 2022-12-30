'''
5.7 (Binary Search) When a list is sorted, a high-speed binary search technique
can find items in the list quickly. The binary search algorithm eliminates from
consideration one-half of the elements in the list being searched after each comparison. 
The algorithm locates the middle element of the list and compares it with the search key. 
If they are equal, the search key is found, and the subscript of that element is returned. 
Otherwise, the problem is reduced to searching one half of the list. If the search key is 
less than the middle element of the list, the first half of the list is searched. 
If the search key is not the middle element in the specified piece of the original list, 
the algorithm is repeated on one-quarter of the original list. The search continues until 
the search key is equal to the middle ele- ment of the smaller list or until the smaller 
list consists of one element that is not equal to the search key (i.e. the search key is not found.)
Even in a worst-case scenario, searching a list of 1024 elements will take only 10 comparisons 
during a binary search. Repeatedly dividing 1024 by 2 (because after each comparison we are able 
to eliminate from the consideration half the list) yields the values 512, 256, 128, 64, 32, 16, 8, 4, 2 and 1. 
The number 1024 (210) is divided by 2 only ten times to get the value 1. Dividing by 2 is equivalent to
one comparison in the binary-search algorithm. A list of 1,048,576 (220) elements takes a maximum of 20
comparisons to find the key. A list of one billion elements takes a maximum of 30 comparisons to find the key. 
The maximum number of comparisons needed for the binary search of any sorted list can be determined by finding 
the first power of 2 greater than or equal to the number of elements in the list.

Write a program that implements function binarySearch, which takes a sorted list and a search key as arguments. 
The function should return the index of the list value that matches the search key (or -1, if the search key is not found).
'''

def binarysearch(the_list, item):
    startIndex = 0
    lastIndex = len(the_list)-1
    nFoundIndex = -1
    while startIndex<=lastIndex:
        nMiddle = ((lastIndex-startIndex)//2) + startIndex
        if the_list[nMiddle]==item:
            nFoundIndex = nMiddle
            break
        elif the_list[nMiddle]>item:
            lastIndex = nMiddle-1
        else:
            startIndex = nMiddle+1
    return nFoundIndex


the_list = [2, 4, 6, 10, 23, 45, 88, 94, 112, 114, 126,
            210, 223, 345, 488, 594, 662, 754, 846, 910, 1223, 1345, 1488, 1594]
item = 753

print(binarysearch(the_list, item))