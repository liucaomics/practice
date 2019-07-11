class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            vec = emails[i].split('@')
            emails[i] = vec[0].split('+')[0].replace('.','') + '@' + vec[1]
        return len(set(emails))