class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hs={}
        for i in range(len(score)):
            hs[score[i]]=i
        count=1
        res=[0]*len(score)
        for x in sorted(hs.keys(),reverse=True):
            i=hs[x]
            if count==1:
                res[i]="Gold Medal"
                count+=1
            elif count==2:
                res[i]="Silver Medal"
                count+=1
            elif count==3:
                res[i]="Bronze Medal"
                count+=1
            else:
                res[i]=str(count)
                count+=1
        return res


            
