import heapq
class Solution:
    def scheduleCourse(self,courses):
        courses.sort(key=lambda x:x[1])
        total=0
        heap=[]
        for dur,dead in courses:
            total+=dur
            heapq.heappush(heap,-dur)
            if total>dead:
                total+=heapq.heappop(heap)
        return len(heap)