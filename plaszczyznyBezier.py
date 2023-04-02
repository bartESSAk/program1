import math
import numpy as np
import matplotlib.pyplot as plt

def czytajPlik(name):
    with open(name, "r") as file:
        punkty = []
        b = int(file.readline())
        for i in range(b):
            for line in file:
                if "3 3" in line:
                    break
                else:
                    x, y, z = line.split()
                    punkty.append((float(x), float(y), float(z)))
                    if len(punkty) == 16:
                        break
    file.close()
    return punkty

def Bezier(Punkty):
    krzywa = []
    for x in range(0, 1001):
        t = x / 1000
        PunktX = 0
        PunktY = 0
        PunktZ = 0
        for i in range(0, 4):
            for j in range(0, 4):
                B = Bernstein(i, 3, t) * Bernstein(j, 3, t)
                PunktX += Punkty[i * 4 + j][0] * B
                PunktY += Punkty[i * 4 + j][1] * B
                PunktZ += Punkty[i * 4 + j][2] * B
        krzywa.append((PunktX, PunktY, PunktZ))
    return krzywa

def Bernstein(i, n, t):
    return math.comb(n, i) * (t ** i) * ((1 - t) ** (n - i))

def plot(punkty):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    patches = []
    for i in range(4):
        for j in range(4):
            patch = Bezier([punkty[k] for k in range(i * 4 + j * 4 * 14, i * 4 + j * 4 * 14 + 16)])
            patches.append(patch)

    for patch in patches:
        x, y, z = zip(*patch)
        ax.plot(x, y, z)
    xx, yy, zz = np.array(patches).T
    ax.plot_surface(xx, yy, zz, cmap='Blues', alpha=0.5)
    plt.show()

def rysuj(name):
    punkty = czytajPlik(name)
    plot(punkty)