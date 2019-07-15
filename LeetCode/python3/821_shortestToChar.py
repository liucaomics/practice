from collections import deque 

class Solution:
    def bfs_dist(self,S,C,query):
        queue = deque([[query,0]])
        visit = [False]*len(S)
        visit[query] = True
        while queue:
            query, dist = queue.popleft()
            if S[query] == C:
                return dist
            if query - 1>=0 and (not visit[query-1]):
                queue.append([query-1,dist+1])
                visit[query-1] = True
            if query + 1<len(S) and (not visit[query+1]):
                queue.append([query+1,dist+1])
                visit[query+1] = True

    def shortestToChar(self, S: str, C: str) -> List[int]:
        dist = [0]*len(S)
        for i in range(len(S)):
            dist[i] = self.bfs_dist(S,C,i)
        return dist
        