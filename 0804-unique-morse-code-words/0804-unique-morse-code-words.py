class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arr=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        hs={}
        for word in words:
            res=[]
            for x in word:
                res.append(arr[ord(x)-ord('a')])
            res=''.join(res)
            hs[res]=hs.get(res,0)+1

        return len(hs)


