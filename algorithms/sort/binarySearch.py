'''
time complexity
O(logN)
'''

def binarySearch(list_number,a):
    '''
    # from small to large
    >>> binarySearch([2],2)
    True

    >>> binarySearch([2],1)
    False

    >>> binarySearch([2,2,3],1)
    False

    >>> binarySearch([2,2,3],2)
    True

    >>> binarySearch([1,2,3,4,6,7],5)
    False

    >>> binarySearch([],0)
    False

    >>> binarySearch([1,2,3,4,5,6],7)
    False

    >>> binarySearch([1,2,3,4,5,6],0)
    False
    '''
    if len(list_number) == 0:
        return False
    low = 0
    high = len(list_number)-1
    return binarySearch_util(list_number,low,high,a)

def binarySearch_util(list_number,low,high,a):
    if low > high:
        return False
    mid = (low+high) // 2
    if list_number[mid] == a:
        return True
    elif list_number[mid] < a:
        return binarySearch_util(list_number,mid+1,high,a)
    else:
        return binarySearch_util(list_number,low,mid-1,a)

if __name__ == "__main__":
    import doctest
    doctest.testmod()




