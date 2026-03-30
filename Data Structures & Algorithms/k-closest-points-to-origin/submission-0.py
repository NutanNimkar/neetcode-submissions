import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distanceToPoints = {n: [] for n in range(len(points))}
        #I want to map the distances to the points, 2 -> 0,2 n 2, 0
        #I want to iterate over the points list take a point calculate its distance
        #if the distance exists append the point to if it doesnt 
        #create a new one
        for point in points:
            x, y = point
            dist = self.calculateDistance(x, y)
            if dist in distanceToPoints:
                distanceToPoints[dist].append([x,y])
            else:
                distanceToPoints[dist] = [[x, y]]
        #i want to create a heap using the 
        #keys of the hashmap which are distances
        heap = []
        for dist in distanceToPoints:
            heapq.heappush(heap, dist)
        result = []
        while len(result) < k:
            dist = heapq.heappop(heap)  # Get the smallest distance
            result.extend(distanceToPoints[dist])  # Add corresponding points to result
            if len(result) >= k:
                result = result[:k]  # Limit the result to k points
        
        return result


            
    def calculateDistance(self, x, y):
        return math.sqrt((x ** 2) + (y ** 2))