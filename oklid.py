# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 09:22:11 2024

@author: 90551
"""
points = [(1, 2), (4, 6), (5, 1), (7, 8), (9, 3)]

# Öklid mesafesi hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1  # İlk nokta koordinatları
    x2, y2 = point2  # İkinci nokta koordinatları
    a = (x2 - x1) ** 2
    b = (y2 - y1) ** 2
    distance = (a + b) ** 0.5
    return distance

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonuçları yazdırma
print(f"Tüm mesafeler: {distances}")
print(f"Minimum mesafe: {min_distance}")