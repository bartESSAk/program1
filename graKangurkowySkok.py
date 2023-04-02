import pygame
import random
import os

pygame.init()

wysokoscEkranu = 370
szerokoscEkranu = 800
ekran = pygame.display.set_mode((szerokoscEkranu, wysokoscEkranu))
tytul = pygame.display.set_caption("KANGURKOWY SKOK")

bieganie = [pygame.image.load(os.path.join("img", "kangurBieg1.png")),
            pygame.image.load(os.path.join("img", "kangurBieg2.png"))]

skakanie = pygame.image.load(os.path.join("img", "kangurSkok.png"))

kaktusy = [pygame.image.load(os.path.join("img", "kaktus1.png")),
           pygame.image.load(os.path.join("img", "kaktus2.png")),
           pygame.image.load(os.path.join("img", "kaktus3.png"))]

tlo = pygame.image.load(os.path.join("img", "ziemia.png"))

class Kangur:
    pozycjaX = 80
    pozycjaY = 310
    odlegloscSkoku = 5

    def __init__(self):
        self.biegImg = bieganie
        self.skokImg = skakanie
        self.kangurBieg = True
        self.kangurSkok = False
        self.krok = 0
        self.odlSkok = self.odlegloscSkoku
        self.img = self.biegImg[0]
        self.kangurRect = self.img.get_rect()
        self.kangurRect.x = self.pozycjaX
        self.kangurRect.y = self.pozycjaY

    def ruchKangura(self, input):
        if self.kangurBieg:
            self.bieg()
        if self.kangurSkok:
            self.skok()
        if self.krok >= 10:
            self.krok = 0

        if input[pygame.K_UP] and not self.kangurSkok:
            self.kangurBieg = False
            self.kangurSkok = True
        elif input[pygame.K_DOWN] and not self.kangurSkok:
            self.kangurBieg = False
            self.kangurSkok = False
        elif not (self.kangurSkok or input[pygame.K_DOWN]):
            self.kangurBieg = True
            self.kangurSkok = False

    def bieg(self):
        self.img = self.biegImg[self.krok // 5]
        self.kangurRect = self.img.get_rect()
        self.kangurRect.x = self.pozycjaX
        self.kangurRect.y = self.pozycjaY
        self.krok += 1

    def skok(self):
        self.img = self.skokImg
        if self.kangurSkok:
            self.kangurRect.y -= self.odlSkok * 4
            self.odlSkok -= 0.8
        if self.odlSkok < - self.odlegloscSkoku:
            self.kangurSkok = False
            self.odlSkok = self.odlegloscSkoku

    def tworzenie(self, ekran):
       ekran.blit(self.img, (self.kangurRect.x, self.kangurRect.y))

class Przeszkoda:
    def __init__(self, img, typ):
        self.img = img
        self.typ = typ
        self.rect = self.img[self.typ].get_rect()
        self.rect.x = szerokoscEkranu

    def pozycjaPrzeszkody(self):
        self.rect.x -= predkoscGry
        if self.rect.x < -self.rect.width:
            przeszkody.pop()

    def tworzeniePrzeszkody(self, ekran):
        ekran.blit(self.img[self.typ], self.rect)


class Kaktus(Przeszkoda):
    def __init__(self, img):
        self.typ = random.randint(0, 2)
        super().__init__(img, self.typ)
        self.rect.y = 310

def main():
    global  pozycjaXtla, pozycjaYtla, punkty, predkoscGry, przeszkody
    graWlaczona = True
    gracz = Kangur()
    zegar = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 20)
    pozycjaXtla = 0
    pozycjaYtla = 340
    predkoscGry = 20
    punkty = 0
    przegrane = 0
    przeszkody = []

    def wynik():
        global punkty, predkoscGry
        punkty += 2
        if punkty % 100 == 0:
            predkoscGry += 1

        text = font.render("Punkty: " + str(punkty), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        ekran.blit(text, textRect)

    def tloGry():
        global pozycjaXtla, pozycjaYtla
        szerokoscImg = tlo.get_width()
        ekran.blit(tlo, (pozycjaXtla, pozycjaYtla))
        ekran.blit(tlo, (szerokoscImg + pozycjaXtla, pozycjaYtla))
        if pozycjaXtla <= -szerokoscImg:
            ekran.blit(tlo, (szerokoscImg + pozycjaXtla, pozycjaYtla))
            pozycjaXtla = 0
        pozycjaXtla -= predkoscGry

    while graWlaczona:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                graWlaczona = False

        ekran.fill((113, 215, 231))
        input = pygame.key.get_pressed()

        gracz.tworzenie(ekran)
        gracz.ruchKangura(input)

        if len(przeszkody) == 0:
            if random.randint(0, 2) == 0:
                przeszkody.append(Kaktus(kaktusy))

        for przeszkoda in przeszkody:
            przeszkoda.tworzeniePrzeszkody(ekran)
            przeszkoda.pozycjaPrzeszkody()
            if gracz.kangurRect.colliderect(przeszkoda.rect):
                pygame.time.delay(2000)
                przegrane += 1
                menu(przegrane)

        tloGry()
        wynik()
        zegar.tick(30)
        pygame.display.update()

def menu(przegrane):
    global punkty
    graWlaczona = True
    while graWlaczona:
        ekran.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 20)

        if przegrane == 0:
            text = font.render("Naciśnij dowolny przycisk, aby rozpocząć!", True, (0, 0, 0))
        elif przegrane > 0:
            text = font.render("Naciśnij dowolny przycisk, aby zrestartować!", True, (0, 0, 0))
            wynik = font.render("Wynik: " + str(punkty), True, (0, 0, 0))
            wynikRect = wynik.get_rect()
            wynikRect.center = (szerokoscEkranu // 2, wysokoscEkranu // 2 + 30)
            ekran.blit(wynik, wynikRect)
        textRect = text.get_rect()
        textRect.center = (szerokoscEkranu // 2, wysokoscEkranu // 2)
        ekran.blit(text, textRect)
        ekran.blit(bieganie[0], (szerokoscEkranu // 2 - 20, wysokoscEkranu // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                graWlaczona = False
            if event.type == pygame.KEYDOWN:
                main()

menu(przegrane=0)