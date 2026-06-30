class Solution(object):
    def maxRepeating(self, sequence, word):
        k=0
        w=word
        while w in sequence:
            k+=1
            w+=word
        return k