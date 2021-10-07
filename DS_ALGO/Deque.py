#DOUBLE QUEUE

import collections

doubleEnded = collections.deque(["Mon", "Tue", "Wed"])

#Append at right
doubleEnded.append("Thu")
print(left)

#Append at left
doubleEnded.appendleft("Sun")

#Delete right
doubleEnded.pop()

#Delete left
doubleEnded.popleft()