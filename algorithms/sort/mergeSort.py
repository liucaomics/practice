'''
a list with index 0...N-1


iteratively split the list into intervals until intervals
for current iteration, 
merge adjacent intervals in a sorted way.

after each iteration, the merged interval is gauranteed to be sorted

worst case time complexity: O(N^2)
auxiliary space complexity: O(N)
in place sorting

'''

def mergeSort(list_number):
    '''
    # from small to large
    >>> mergeSort([2])
    [2]

    >>> mergeSort([])
    []
    
    >>> mergeSort([2])
    [2]
    
    >>> mergeSort([1,1,1])
    [1, 1, 1]
    
    >>> mergeSort([3,5,6,9,4,2,1,8,7])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> mergeSort([4,9,2,1,3,1,4,4])
    [1, 1, 2, 3, 4, 4, 4, 9]

    '''
    if len(list_number) <= 1:
        return list_number
    mergeSort_util(list_number,0,len(list_number)-1)
    return list_number

def mergeSort_util(list_number,left,right):
    if left>=right:
        return
    mid = (left + right) // 2
    mergeSort_util(list_number,left,mid)
    mergeSort_util(list_number,mid+1,right)
    merge(list_number,left,mid,right)

def merge(list_number,left,mid,right):
    # copy of [left...mid] and [mid+1...right]
    list_left = list( list_number[left:mid+1] )
    list_right = list( list_number[mid+1:right+1] )
    
    i, j, k = 0, 0, 0
    while i < len(list_left) and j < len(list_right):
        if list_left[i] <= list_right[j]:
            list_number[left+k] = list_left[i]
            i += 1
            k += 1
        else:
            list_number[left+k] = list_right[j]
            j += 1
            k += 1
    if i < len(list_left):
        list_number[right-len(list_left[i:])+1:right+1] = list_left[i:]
    if j < len(list_right):
        list_number[right-len(list_right[j:])+1:right+1] = list_right[j:]
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()




