import numpy as np

A, B, D = map(float, input().split())

rad = np.radians(D)

rotate = np.array([[np.cos(rad), - np.sin(rad)],
                  [np.sin(rad), np.cos(rad)]])

result = np.dot(rotate, np.array([A, B]))

print(result[0], result[1])
