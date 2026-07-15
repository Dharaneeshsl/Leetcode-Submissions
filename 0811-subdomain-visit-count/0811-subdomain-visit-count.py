from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp=defaultdict(int)
        for s in cpdomains:
            cnt,domain=s.split()
            cnt=int(cnt)
            parts=domain.split(".")
            for i in range(len(parts)):
                mp[".".join(parts[i:])]+=cnt
        ans=[]
        for domain,cnt in mp.items():
            ans.append(str(cnt)+" "+domain)
        return ans