'''
a list with index 0...N-1

for round i, 
0...i-1 are sorted, i...N-1 are not
insert ith item into 0...i-1, so that the 0...i are sorted

after round i, items in 0...i are sorted

worst case time complexity: O(N^2)
space complexity: O(n)
in place sorting

'''

def insertionSort(list_number):
    '''
    # from small to large
    >>> insertionSort([2])
    [2]

    >>> insertionSort([])
    []
    
    >>> insertionSort([2])
    [2]
    
    >>> insertionSort([1,1,1])
    [1, 1, 1]
    
    >>> insertionSort([3,5,6,9,4,2,1,8,7])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> insertionSort([4,9,2,1,3,1,4,4])
    [1, 1, 2, 3, 4, 4, 4, 9]

    '''
    if len(list_number) <= 1:
        return list_number
    for i in range(1,len(list_number)):
        for j in range(i):
            if list_number[i] <= list_number[j]:
            # then i should be in position j, and the rest are push away
                temp = list_number[i]
                for k in range(i,j,-1):
                    list_number[k] = list_number[k-1]
                list_number[j] = temp
                break
    return list_number

if __name__ == "__main__":
    import doctest
    doctest.testmod()




