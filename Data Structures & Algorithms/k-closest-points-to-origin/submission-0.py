import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        dist = lambda point: (point[0]**2 + point[1]**2) ** (1/2)
        for point in points:
            if len(distances) < k:
                heapq.heappush(distances, (-dist(point), point))
            else:
                heapq.heappushpop(distances, (-dist(point), point))
        return [elem[1] for elem in distances]
