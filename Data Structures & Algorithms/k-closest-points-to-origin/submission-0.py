class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kDict = collections.defaultdict(list)

        closestPoints = []

        n = len(points)
        for i in range(n):
            dist = (points[i][0] ** 2 + points[i][1] ** 2) ** 0.5
            kDict[dist].append(points[i])
        
        relevantKeys = sorted(kDict.keys())

        for rk in relevantKeys:
            for point in kDict[rk]:
                if len(closestPoints) < k:
                    closestPoints.append(point)

        return closestPoints