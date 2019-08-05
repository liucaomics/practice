class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        a = 'abcdefghijklmnopqrstuvwxyz'
        d = {}
        for i in range(len(a)):
            d[a[i]] = widths[i]
        currentWidth = 0
        out_count = 0
        for s in S:
            nextWidth = d[s]
            if currentWidth + nextWidth>100:
                currentWidth = nextWidth
                out_count += 1
            else:
                currentWidth += nextWidth
        return [out_count+1,currentWidth]
        