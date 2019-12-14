'''
a list with index 0...N-1

for round i, 
select the smallest value in i...N-1,
move swap the smallest value and i

after round i, items in 0...i are sorted

worst case time complexity: O(N^2)
space complexity: O(n)
in place sorting

'''


def selectionSort(list_number):
    '''
    # from small to large
    >>> selectionSort([2])
    [2]

    >>> selectionSort([])
    []
    
    >>> selectionSort([2])
    [2]
    
    >>> selectionSort([1,1,1])
    [1, 1, 1]
    
    >>> selectionSort([3,5,6,9,4,2,1,8,7])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> selectionSort([4,9,2,1,3,1,4,4])
    [1, 1, 2, 3, 4, 4, 4, 9]
    '''
    if len(list_number) <= 1:
        return list_number
    for i in range(len(list_number)):
        # find minimum in [i:]
        minimum = list_number[i]
        index_min = i
        for j in range(i,len(list_number)):  
            if list_number[j] < minimum:
                minimum = list_number[j]
                index_min = j
        # swap list_number[index_min] and list_number[i]
        list_number[index_min] = list_number[i]
        list_number[i] = minimum
    return list_number

if __name__ == "__main__":
    import doctest
    doctest.testmod()




