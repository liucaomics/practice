'''
a list with index 0...N-1

for current iteration, 
randomly find a pivot value in current interval, 
move all the values smaller than the pivot to its left,
move all the values greater than the pivot to its right,

after each iteration, the pivot value is gauranteed to be in the correct position


worst case time complexity: O(N^2)
average complexity: O(N*logN)
space complexity: O(N)
in place sorting

'''

def quickSort(list_number):
    '''
    # from small to large
    >>> quickSort([2])
    [2]

    >>> quickSort([])
    []
    
    >>> quickSort([2])
    [2]
    
    >>> quickSort([1,1,1])
    [1, 1, 1]
    
    >>> quickSort([3,5,6,9,4,2,1,8,7])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> quickSort([4,9,2,1,3,1,4,4])
    [1, 1, 2, 3, 4, 4, 4, 9]

    '''
    if len(list_number) <= 1:
        return list_number
    quickSort_util(list_number,0,len(list_number)-1)
    return list_number

def quickSort_util(list_number,low,high):
    if low >= high:
        return
    pivot_index = partition(list_number,low,high)
    quickSort_util(list_number,low,pivot_index-1)
    quickSort_util(list_number,pivot_index+1,high)

def partition(list_number, low, high):
    pivot = list_number[high]
    small = low - 1
    for i in range(low,high):
        if list_number[i] < pivot:
            small += 1
            swap(list_number,small,i)
    swap(list_number,small+1,high)
    return small+1

def swap(list_number,i,j):
    temp = list_number[i]
    list_number[i] = list_number[j]
    list_number[j] = temp

if __name__ == "__main__":
    import doctest
    doctest.testmod()




