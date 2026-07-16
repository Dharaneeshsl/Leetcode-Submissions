class Solution:
    def compress(self, chars: List[str]) -> int:

        i=0
        j=0
        count=0
        while j<len(chars):
            while j<len(chars) and chars[i]==chars[j] :
                j+=1

            if (j-i)==1:
                chars[count]=chars[i]
                count+=1
            else:
                chars[count]=chars[i]
                for x in str(j-i):
                    count+=1
                    chars[count]=x
                count+=1
            i=j
            
        return count

