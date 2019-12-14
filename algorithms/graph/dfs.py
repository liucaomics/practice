'''
need a flag list to record if a node has already been visited

time complexity: O(V+E)

'''

def dfs(adjMat, v):
    '''
    >>> dfs([[0,1,1,0],[1,0,0,0],[1,0,0,1],[0,0,1,0]],0)
    0
    1
    2
    3

    >>> dfs([[0,1,1,0],[1,0,0,0],[1,0,0,1],[0,0,1,0]],3)
    3
    2
    0
    1
    
    '''

    visited = [False]*len(adjMat)
    dfs_util(adjMat,v,visited)

def dfs_util(adjMat,v,visited):
    if visited[v]:
       return
    visited[v] = True
    print(v)
    for i in range(len(adjMat[v])):
        if adjMat[v][i] > 0:
            dfs_util(adjMat,i,visited)

def dfs_stack(adjMat,v):
    '''
    >>> dfs_stack([[0,1,1,0],[1,0,0,0],[1,0,0,1],[0,0,1,0]],0)
    0
    1
    2
    3

    >>> dfs_stack([[0,1,1,0],[1,0,0,0],[1,0,0,1],[0,0,1,0]],3)
    3
    2
    0
    1
    
    '''

    visited = [False]*len(adjMat)
    stack = [v]
    visited[v] = True
    while stack:
        node = stack.pop()
        print(node)
        for i in range(len(adjMat[node])-1,-1,-1):
            if (not visited[i]) and adjMat[node][i] > 0:
                stack.append(i)
                visited[i] = True

if __name__ == "__main__":
    import doctest
    doctest.testmod()

