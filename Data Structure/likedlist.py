# https://docs.python.org/3/library/collections.html#deque-objects
from collections import deque
d = deque([1,2,3,4])

print d
for x in d:
    print x
print d.pop(), d
