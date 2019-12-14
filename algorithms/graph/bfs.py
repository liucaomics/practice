'''
need a flag list to record if a node has already been visited

time complexity: O(V+E)

'''

def bfs(adjMat, v):
    '''
    >>> bfs([[0,1,1,0],[1,0,0,0],[1,0,0,1],[0,0,1,0]],0)
    0
    1
    2
    3

    >>> bfs([[0,1,1,0],[1,0,0,0],[1,0,0,1],[0,0,1,0]],3)
    3
    2
    0
    1
    
    '''

    visited = [False]*len(adjMat)
    que = [v]
    visited[v] = True
    while que:
        node = que.pop(0)
        print(node)
        for i in range(len(adjMat[node])):
            if (not visited[i]) and adjMat[node][i]>0 :
                que.append(i)
                visited[i] = True

if __name__ == "__main__":
    import doctest
    doctest.testmod()

