import math
points=[]
points.append((1,2))
points.append((-1,2))
points.append((1,-2))
points.append((1,3))
points.append((-1,-2))
points.append((4,2))

def euclideanDistance(point1,point2):
    return math.sqrt(pow((point1[0]-point2[0]),2)+pow((point1[1]-point2[1]),2))

euclideanDistance(points[0],points[3])

distances=[]
for i in range(len(points)):
    for index_inside in range(i+1,len(points)):
        #print(points[i]," ",points[index_inside]," ",euclideanDistance(points[i],points[index_inside]))
        distances.append(euclideanDistance(points[i],points[index_inside]))

minimum_distance=distances[0]
for i in range(len(distances)):
    if distances[i]<minimum_distance:
        minimum_distance=distances[i]
        
print(minimum_distance)