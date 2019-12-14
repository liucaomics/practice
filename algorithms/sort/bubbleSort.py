'''
a list with index 0...N-1

for round i, swap ajacent items in 0...N-i, so that the greatest value goes to N-i

after round i, items in N-i...N-1 are those greatest and sorted.

worst case time complexity: O(N^2)
space complexity: O(n)
in place sorting

'''

def bubbleSort(list_number):
    '''
    # from small to large
    >>> bubbleSort([2])
    [2]

    >>> bubbleSort([])
    []
    
    >>> bubbleSort([2])
    [2]
    
    >>> bubbleSort([1,1,1])
    [1, 1, 1]
    
    >>> bubbleSort([3,5,6,9,4,2,1,8,7])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> bubbleSort([4,9,2,1,3,1,4,4])
    [1, 1, 2, 3, 4, 4, 4, 9]

    '''
    if len(list_number) <= 1:
        return list_number
    for i in range(len(list_number),0,-1):
        for j in range(i-1):
            if list_number[j]>list_number[j+1]:
                temp = list_number[j+1]
                list_number[j+1] = list_number[j]
                list_number[j] = temp
    return list_number

if __name__ == "__main__":
    import doctest
    doctest.testmod()




