class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes={}
        for num in range(lowLimit,highLimit+1):
            s=sum(map(int,str(num)))
            boxes[s]=boxes.get(s,0)+1
        return max(boxes.values())