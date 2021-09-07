# Task-02

import math
import matplotlib.pyplot as plt

xA = int(input("Position of A1 : "))  # 0
yA = int(input("Position of A2 : "))  # 1000
xB = int(input("Position of B1 : "))  # 12000
yB = int(input("Position of B2 : "))  # 2000
xC = int(input("Position of C1 : "))  # 10000
yC = int(input("Position of C2 : "))  # 10000
xD = int(input("Position of D1 : "))  # 5000
yD = int(input("Position of D2 : "))  # 15000
Da = int(input("Attack Distance : "))  # 1000
Va = int(input("Velocity of Va : "))  # 60
Vb = int(input("Velocity of Vb : "))  # 60
Vc = int(input("Velocity of Vc : "))  # 60
Vd = int(input("Velocity of Vd : "))  # 60
t = int(input("Time Limit : "))  # 300
deltaT = int(input("Value of deltaT : "))  # 2

deltaS = Vc * deltaT
new_xA = []
new_yA = []
new_xB = []
new_yB = []
new_xC = []
new_yC = []
new_xD = []
new_yD = []

for i in range(1, t+1, deltaT):

    xA = xA + ((xB - xA) / math.dist((xA, yA), (xB, yB)) * Va * deltaT)
    new_xA.append(xA)
    yA = yA + ((yB - yA) / math.dist((xA, yA), (xB, yB)) * Va * deltaT)
    new_yA.append(yA)

    xB = xB + ((xC - xB) / math.dist((xB, yB), (xC, yC)) * Vb * deltaT)
    new_xB.append(xB)
    yB = yB + ((yC - yB) / math.dist((xB, yB), (xC, yC)) * Vb * deltaT)
    new_yB.append(yB)

    xC = xC + ((xD - xC) / math.dist((xC, yC), (xD, yD)) * Vc * deltaT)
    new_xC.append(xC)
    yC = yC + ((yD - yC) / math.dist((xC, yC), (xD, yD)) * Vc * deltaT)
    new_yC.append(yC)

    xD = xD - Vd * deltaT
    new_xD.append(xD)
    new_yD.append(yD)

    if math.dist((xA, yA), (xB, yB)) > Da:
        temp = 0
    elif math.dist((xB, yB), (xC, yC)) > Da:
        temp = 0
    elif math.dist((xC, yC), (xD, yD)) > Da:
        temp = 0
    else:
        temp = 1
        D1 = math.dist((xA, yA), (xB, yB))
        D2 = math.dist((xB, yB), (xC, yC))
        D3 = math.dist((xC, yC), (xD, yD))
        break

if temp != 0:
    print("Defense A attacked enemy B with distance = ", D1, "m")
    print("Defense B attacked enemy C with distance = ", D2, "m")
    print("Defense C attacked enemy D with distance = ", D3, "m")
else:
    print("No attack occurred….\n")

plt.scatter(xA, yA, color='red')
plt.scatter(xB, yB, color='green')
plt.scatter(xC, yC, color='blue')
plt.scatter(xD, yD, color='yellow')
plt.plot(new_xA, new_yA, marker='o', label='Fighter A')
plt.plot(new_xB, new_yB, marker='o', label='Enemy B')
plt.plot(new_xB, new_yB, marker='o', label='Fighter B')
plt.plot(new_xC, new_yC, marker='o', label='Enemy C')
plt.plot(new_xC, new_yC, marker='o', label='Fighter C')
plt.plot(new_xD, new_yD, marker='o', label='Enemy D')
plt.legend()
plt.show()


