class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        hs1={}
        hs2={}
        for i in range(len(word1)):
            hs1[word1[i]]=hs1.get(word1[i],0)+1
            hs2[word2[i]]=hs2.get(word2[i],0)+1
        if set(hs1.keys())==set(hs2.keys()) and sorted(hs1.values())==sorted(hs2.values()):
            return True
        
        return False