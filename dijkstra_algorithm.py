class Distance:
    def __init__(self, point1, point2, distance):
        self.point1 = point1
        self.point2 = point2
        self.distance = distance

    def updateDistance(self, distance):
        if self.distance > distance:
            self.distance = distance

    def isTo(self, toPoint):
        return self.point2 == toPoint

    def __repr__(self):
        return "point1: " + self.point1 + ", point2: " + self.point2 + ", distance: " + str(self.distance)

class Distances:
    def __init__(self):
        self.distances = {}

    def add(self, point, to, distance):
        if not self.getDistancePointingTo(point, to):
            self._add(point, to, distance)
        return self

    def getDistancePointingTo(self, point, withPoint):
        if point not in self.distances:
            return None
        for distance in self.distances[point]:
            if distance.isTo(withPoint):
                return distance

    def _add(self, point, to, distance):
        if point not in self.distances:
            self.distances[point] = []
        self.distances[point].append(Distance(point, to, distance))

    def merge(self, point, mainDistance, withDistance):
        previousDistance = self.getDistancePointingTo(point, withDistance.point2)
        if not previousDistance:
            self._add(point, withDistance.point2, mainDistance.distance + withDistance.distance)
        else:
            previousDistance.updateDistance(mainDistance.distance + withDistance.distance)

    def _explore(self, point, withPoint, mainDistance):
        for withDistance in self.distances[withPoint]:
            self.merge(point, mainDistance, withDistance)

    def explore(self, point):
        explored = []
        while len(explored) != (len(self.distances.keys()) - 1):
            for withPoint in self.distances:
                if withPoint == point:
                    continue
                mainDistance = self.getDistancePointingTo(point, withPoint)
                if not mainDistance:
                    continue
                if withPoint in explored:
                    continue
                self._explore(point, withPoint, mainDistance)
                explored.append(withPoint)

def solution():
    distances = Distances().add("a", "b", 4).add("a", "c", 3)
    distances.add("b", "c", 2).add("b", "d", 5).add("b", "a", 4)
    distances.add("c", "b", 2).add("c", "d", 3).add("c", "e", 6).add("c", "a", 3)
    distances.add("d", "b", 5).add("d", "c", 3).add("d", "e", 1).add("d", "f", 5)
    distances.add("e", "c", 6).add("e", "d", 1).add("e", "g", 5)
    distances.add("f", "d", 5).add("f", "g", 2).add("f", "z", 7)
    distances.add("g", "e", 5).add("g", "f", 2).add("g", "z", 4)
    distances.add("z", "f", 7).add("z", "g", 4)
    distances.explore("a")
    return distances.getDistancePointingTo("a", "z").distance

print(solution())
