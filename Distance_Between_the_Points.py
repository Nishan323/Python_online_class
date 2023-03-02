

import math
print("Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).")
p1=[4,0]
p2=[6,6]
distance=math.sqrt((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)
print(distance)


x1=int(input("enter x1 : "))

x2=int(input("enter x2 : "))

y1=int(input("enter y1 : "))

y2=int(input("enter y2 : "))

result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)