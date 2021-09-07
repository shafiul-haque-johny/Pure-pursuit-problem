# Task-01

import math
import matplotlib.pyplot as plt

xA = int(input("Position of A1 : "))  # 0
yA = int(input("Position of A2 : "))  # 0
xB = int(input("Position of B1 : "))  # 10000
yB = int(input("Position of B2 : "))  # 10000
Da = int(input("Attack Distance : "))  # 1000
Va = int(input("Velocity of Va : "))  # 60
Vb = int(input("Velocity of Vb : "))  # 50
t = int(input("Time Limit : "))  # 300
deltaT = int(input("Value of deltaT : "))  # 2

deltaS = Va * deltaT
new_xA = []
new_yA = []
new_xB = []
new_yB = []

for i in range(1, t+1, deltaT):
    xA = xA + ((xB - xA) / math.dist((xA, yA), (xB, yB)) * Va * deltaT)
    new_xA.append(xA)
    yA = yA + ((yB - yA) / math.dist((xA, yA), (xB, yB)) * Va * deltaT)
    new_yA.append(yA)
    xB = xB - Vb * deltaT
    new_xB.append(xB)
    new_yB.append(yB)

    if math.dist((xA, yA), (xB, yB)) > Da:
        temp = 0
    else:
        temp = 1
        D = math.dist((xA, yA), (xB, yB))
        break

if temp != 0:
    print("Defense A attacked enemy B with distance = ", D, "m")
else:
    print("Defense A didn't attack enemy B\n")

plt.scatter(xA, yA, color='red')
plt.scatter(xB, yB, color='green')
plt.plot(new_xA, new_yA, marker='o', label='Fighter A')
plt.plot(new_xB, new_yB, marker='o', label='Enemy B')
plt.legend()
plt.show()
