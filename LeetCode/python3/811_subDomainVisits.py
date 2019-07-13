class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash_visit = dict()
        out = []
        for domain in cpdomains:
            count, dom = domain.split()
            count = int(count)
            v_dom = dom.split('.')
            for i in range(len(v_dom)):
                dom = '.'.join(v_dom[i:])
                hash_visit[dom] = hash_visit.get(dom,0) + count
        for key, value in hash_visit.items():
            out.append(str(value) + ' ' + key)
        return out