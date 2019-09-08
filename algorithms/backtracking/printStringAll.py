'''
print all strings of a given length and a given vocabulary
'''

def printAllString(length,vocabulary):
    printUtil(length,vocabulary,[]) 

def printUtil(n,vocabulary,state):
    if len(state) == n:
        print(state)
        return
    for v in vocabulary:
        state = state+[v]
        printUtil(n,vocabulary,state)
        state.pop()

if __name__ == '__main__':
    printAllString(4,[0,1])
    



