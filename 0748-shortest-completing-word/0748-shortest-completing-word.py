class Solution:
    def shortestCompletingWord(self,licensePlate,words):
        need=[0]*26
        for c in licensePlate.lower():
            if c.isalpha():
                need[ord(c)-97]+=1
        ans=""
        for word in words:
            cnt=[0]*26
            for c in word:
                cnt[ord(c)-97]+=1
            if all(cnt[i]>=need[i] for i in range(26)):
                if not ans or len(word)<len(ans):
                    ans=word
        return ans