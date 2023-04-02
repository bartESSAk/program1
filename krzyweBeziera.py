import matplotlib.pyplot as plt

punkty = [  (97, 358),
            (97, 373), (110, 137), (95, 137),
            (80, 137), (172, 134), (184, 135),
            (199, 136), (226, 138), (228, 166),
            (229, 181), (207, 197), (192, 206),
            (179, 214), (119, 226), (104, 222),
            (100, 218), (231, 254), (238, 257),
            (252, 263), (261, 265), (264, 298),
            (265, 313), (262, 323), (240, 336),
            (227, 344), (119, 363), (104, 362),
            (89, 361), (333, 359), (332, 374),
            (331, 389), (329, 138), (314, 138),
            (299, 138), (394, 134), (402, 136),
            (417, 140), (439, 139), (448, 166),
            (453, 180), (444, 190), (419, 209),
            (407, 218), (346, 225), (331, 222),
            (316, 219), (429, 234), (444, 244),
            (456, 252), (493, 277), (497, 304),
            (499, 319), (466, 344), (450, 354),
            (329, 380), (353, 379), (339, 374),
         ]

def krzywaBezier(punkty, t):
    punkt0, punkt1, punkt2, punkt3 = punkty
    return (1 - t) ** 3 * punkt0 + 3 * (1 - t) ** 2 * t * punkt1 + 3 * (1 - t) * t ** 2 * punkt2 + t ** 3 * punkt3

punktyKrzywej = []
for i in range(0, len(punkty), 4):
    pozostalePunkty = len(punkty) - i
    if pozostalePunkty >= 4:
        punkt0, punkt1, punkt2, punkt3 = punkty[i:i + 4]
        for t in range(101):
            x = krzywaBezier((punkt0[0], punkt1[0], punkt2[0], punkt3[0]), t / 100)
            y = krzywaBezier((punkt0[1], punkt1[1], punkt2[1], punkt3[1]), t / 100)
            punktyKrzywej.append((x, y))

def rysuj():
    plt.gca().invert_yaxis()
    wspolX = [point[0] for point in punktyKrzywej]
    wspolY = [point[1] for point in punktyKrzywej]
    plt.plot(wspolX, wspolY)
    plt.show()