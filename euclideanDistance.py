# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:21:38 2025

@author: Aysu
"""
import math 

points= [(3,4),(5,12),(8,16),[1,1]]

def euclideanDistance(point1,point2):
    eDis= math.sqrt((point2[0]-point1[0])**2+(point2[1]-point1[1])**2)
    return eDis
distances=[]
for i in range(len(points)-1):
    for j in range(i + 1, len(points)):  
        distance = euclideanDistance(points[i], points[j])
        distances.append((points[i], points[j], distance))
    
for p1,p2,d in (distances):
    print("{} noktası ve {} noktası arasındaki öklid mesafesi: {} ".format(p1,p2,d))    

min_distance_pair = min(distances, key=lambda x: x[2])      
print("\nEn kısa mesafe:")
print(f"{min_distance_pair[0]} ile {min_distance_pair[1]} arasındaki mesafe: {min_distance_pair[2]:.2f}")
