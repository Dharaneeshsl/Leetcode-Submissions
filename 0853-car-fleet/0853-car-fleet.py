class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        result = []
        for i in range(n):
            time = (target - position[i]) / speed[i]
            result.append([position[i], time])

        result.sort(key=lambda x: x[0])
        count = 0
        prev = 0
        
        for i in range(n - 1, -1, -1):
            if result[i][1] > prev:
                count += 1
                prev = result[i][1]

        return count