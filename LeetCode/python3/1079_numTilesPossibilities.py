class Solution:
    out = set()
    def numTilePossibilities(self, tiles: str) -> int:
        self.out = set()
        state = list(tiles)
        for index, s in enumerate(state):
            self.numTilePossibilities_util(s,state[:index]+state[index+1:])
        return len(self.out)
        
    
    def numTilePossibilities_util(self, current, state):
        self.out.add(current)
        if len(state) == 0:
            return
        else:
            for index, s in enumerate(state):
                self.numTilePossibilities_util(current+s,state[:index]+state[index+1:])
            
            
            
            
        