import dataclasses
import math


@dataclasses.dataclass
class Point:
    x: float
    y: float
    z: float = 0.0

    def norm(self):
        return math.sqrt(sum(axis ** 2 for axis in dataclasses.astuple(self)))
    


a = Point(1, 2, 3)
print(a.norm())