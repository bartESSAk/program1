import subprocess
import krzyweBeziera
import plaszczyznyBezier
from tkinter import *

def obiekty3D():
    if var.get() == 1:
        plaszczyznyBezier.rysuj("teapot")
    elif var.get() == 2:
        plaszczyznyBezier.rysuj("spoon")
    elif var.get() == 3:
        plaszczyznyBezier.rysuj("cup")

def uruchomGre():
    try:
        process = subprocess.Popen(['python', 'graKangurkowySkok.py'], shell=False)
    except OSError as e:
        print("Błąd: ", e)


okno = Tk()
var = IntVar()
okno.title("MENU")
okno.geometry("500x300")

    # TEKST POWITALNY
tekst1 = Label(okno, text = "Witaj w menu! Wybierz zadanie!", width = 40)
tekst1.grid(row = 1, column = 1)

    # KRZYWE BEZIER - INICJAŁY
tekst2 = Label(okno, text= "Krzywe Bezier:", width = 20)
tekst2.grid(row= 2, column = 1)

przycisk1 = Button(okno, text="INICJAŁY", width=20, command=krzyweBeziera.rysuj)
przycisk1.grid(row=2, column=2)
    # KONIEC KRZYWYCH BEZIER

    # PŁASZCZYZNY BEZIER
tekst3 = Label(okno, text= "Krzywe Bezier:", width = 20)
tekst3.grid(row= 3, column = 1)

przycisk3 = Button(okno, text="OBIEKT 3D", width=20, command=obiekty3D)
przycisk3.grid(row=3, column=2)

r1 = Radiobutton(okno, text="teapot", variable=var, value=1)
r1.grid(row=4, column=2)
r1.select()

r2 = Radiobutton(okno, text="spoon", variable=var, value=2)
r2.grid(row=5, column=2)

r3 = Radiobutton(okno, text="cup", variable=var, value=3)
r3.grid(row=6, column=2)
    # KONIEC PŁASZCZYZN BEZIER

    # GRA PYGAME
tekst4 = Label(okno, text = "Gra PyGame:", width = 20)
tekst4.grid(row = 7, column = 1)

przycisk4 = Button(okno, text="GRA", width=20, command=uruchomGre)
przycisk4.grid(row=7, column=2)
    #KONIEC GRY PYGAME

okno.mainloop()