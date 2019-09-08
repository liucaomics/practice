'''
print all vectors of a given length and a given vocabulary
under the constraints that the sum should be less than a threshold 
'''

def printVecConstraint(length,vocabulary,threshold):
    printUtil(length,vocabulary,[],threshold) 

def printUtil(n,vocabulary,state,threshold):
    if len(state) == n and sum(state) <= threshold:
        print(state)
        return 
    for v in vocabulary:
        if sum( state + [v] ) <= threshold:
            state = state + [v]
            printUtil(n,vocabulary,state,threshold)
            state.pop()
        else:
            continue

if __name__ == '__main__':
    printVecConstraint(5,[0,1,2],3)
    



