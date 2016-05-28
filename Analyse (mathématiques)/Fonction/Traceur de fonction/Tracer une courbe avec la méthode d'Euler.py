# -*- coding:utf-8 -*-

# http://codes-sources.commentcamarche.net/source/view/27916/946973#browser

"""
La méthode d'Euler permet, en sachant par quel point passe une courbe, et sa dérivée, trace une approximation affine de la courbe.
Commencer par écrire et tracer l'équation avec un pas de 0.01. Ensuite remplir 'la méthode d'Euler' puis mettre un pas de 0.01.
Tout les trous doivent être remplit pour que cela fonctionne. Pour ne tracer qu'une courbe remplir le reste par des 0.
"""

from tkinter import *
from math import *
import os


def euler(mini, maxi, pas, x, y, deriv, echelleX, echelleY, offX, offY):
    enreg, absc, fonction, echelleY = x, x, y, -echelleY
    if deriv == 'Fx':
        bDeriv = True
    else:
        bDeriv = False

    tmp = []

    tmp.append((x * echelleX + offX, fonction * echelleY + offY))
    #Partie inférieure#
    while absc > mini:
        absc = absc - pas

        if bDeriv == True:
            deriv = str(fonction)

        try:
            fonction = (fonction - pas * eval(deriv))
            tmp.append((absc * echelleX + offX, fonction * echelleY + offY))
            x = x - pas

        except:
            break

    #Partie supérieure#
    absc, fonction, x = enreg, y, enreg
    while absc < maxi:
        absc = absc + pas

        if bDeriv == True:
            deriv = str(fonction)

        try:
            fonction = fonction + pas * eval(deriv)
            tmp.append((absc * echelleX + offX, fonction * echelleY + offY))
            x = x + pas
        except:
            break

    tmp.sort()

    #tracage#

    tmpO = []
    for i in tmp:
        tmpO.append(i[0])

        tmpO.append(i[1])

    img.coords(dxT, tuple(tmpO))


def return_Pos(self):

    tmpX, tmpY = str((self.x - curroffX) * 1.0 /
                     currscaleX), str(-(self.y - curroffY) * 1.0 / currscaleY)

    fen.title('f(' + tmpX[:tmpX.find('.') + 3] + ')=' +
              tmpY[:tmpY.find('.') + 3])


def trace_Org(offX, offY, scaleX, scaleY):
    img.delete('org')
    n = 0
    absc = img.create_line(0, offY, tX, offY, tag='org')
    while n < tX:
        n = n + scaleX
        img.create_line(n, offY - 5, n, offY + 5, tag='org')
        if (n - offX) / scaleX != 0:
            img.create_text(
                n, offY + 10, text=str((n - offX) / scaleX), tag='org')

    img.create_line(offX, 0, offX, tY, tag='org')

    n = 0

    while n < tY:
        n = n + scaleY
        img.create_line(offX - 5, n, offX + 5, n, tag='org')
        if (n - offY) / scaleY != 0:
            img.create_text(
                offX - 10, n, text=str(-(n - offY) / scaleY), tag='org')
        else:
            img.create_text(offX - 10, n + 10,
                            text=str((n - offY) / scaleY), tag='org')


def trace_M(miniX, maxiX, miniY, maxiY, fonction, x, y, deriv, pas, pasF):
    global curroffX, curroffY, currscaleX, currscaleY

    echelleX, echelleY = tX / (maxiX - miniX), tY / (maxiY - miniY)

    offX, offY = echelleX * -miniX, echelleY * maxiY

    curroffX = offX
    curroffY = offY
    currscaleX = echelleX
    currscaleY = echelleY

    trace_Org(offX, offY, echelleX, echelleY)

    traceFx(str(fonction), miniX - 1, maxiX + 1,
            offX, offY, echelleX, echelleY, pasF)
    euler(miniX - 1, maxiX + 1, pas, x, y,
          deriv, echelleX, echelleY, offX, offY)


def traceFx(expression, mini, maxi, offX, offY, scaleX, scaleY, pasF):
    x = mini
    out = []
    while x <= maxi:
        out.append(x * scaleX + offX)
        try:

            out.append((eval(expression) * -scaleY) + offY)
        except:
            out.append(offY)

        x = x + pasF

    img.coords(fxT, tuple(out))


def run_T():

    if pase.get() == '':
        pase.insert(0, 0.5)
    if xDe.get() == '':
        xDe.insert(0, 0)
    if yDe.get() == '':
        yDe.insert(0, 0)

    try:
        trace_M(int(minXe.get()), int(maxXe.get()), int(minYe.get()), int(maxYe.get()), Fxe.get(
        ), float(xDe.get()), float(yDe.get()), derive.get(), float(pase.get()), float(pasFxe.get()))
    except:
        print('Erreur dans le domaine de définition')


curroffX, curroffY, currscaleX, currscaleY = 0, 0, 1, 1

tX, tY = 700, 700
fen = Tk()
fen.configure(width=1022, height=768)
fen.resizable(False, True)

img = Canvas(fen, bg='white')
fxT = img.create_line(0, 0, 0, 0, fill='blue', width=1, smooth=True)
dxT = img.create_line(0, 0, 0, 0, fill='red', width=1, smooth=True)

img.tag_bind(fxT, '<Button-1>', func=return_Pos)

minXe = Entry(fen)
minXe.insert(0, -10)

maxXe = Entry(fen)
maxXe.insert(0, 10)

minYe = Entry(fen)
minYe.insert(0, -10)

maxYe = Entry(fen)
maxYe.insert(0, 10)

minXc = Label(fen, text="Minimum sur l'axe des abscisses : ")
maxXc = Label(fen, text="Maximum sur l'axe des abscisses : ")
minYc = Label(fen, text="Minimum sur l'axe des ordonnées")
maxYc = Label(fen, text="Maximum sur l'axe des ordonnées")

Fxc = Label(fen, text='F(x)=')
Fxe = Entry(fen)
pasFxe, pasFxc = Entry(fen), Label(fen, text='pas :')

cmdTrace = Button(fen, text='Tracer les courbes', command=run_T)

xDc, xDe, yDc, yDe, derive, derivc, pasc, pase = Label(fen, text="F  ("), Entry(fen), Label(
    fen, text=') = '), Entry(fen), Entry(fen), Label(fen, text="F ' (x) ="), Label(fen, text='Pas = '), Entry(fen)


# Bloc 1
debB = 50
Label(fen, text='=' * 15 + "Equation d'une courbe" +
      '=' * 15).place(x=tX + 10, y=debB - 25)
Fxc.place(x=tX + 10, y=debB)
Fxe.place(x=tX + 50, y=debB)
pasFxc.place(x=tX + 10, y=debB + 20)
pasFxe.place(x=tX + 50, y=debB + 20, width=30)

# Bloc 2
debB = 250

Label(fen, text="=" * 15 + "Méthode d'Euler" +
      "=" * 15).place(x=tX + 10, y=debB - 25)

xDc.place(x=tX + 10, y=debB)
xDe.place(x=tX + 32, y=debB, width=25)
yDc.place(x=tX + 57, y=debB)
yDe.place(x=tX + 80, y=debB, width=25)


derivc.place(x=tX + 10, y=debB + 30)
derive.place(x=tX + 53, y=debB + 30)

pasc.place(x=tX + 200, y=debB + 30)
pase.place(x=tX + 235, y=debB + 30, width=28)


# Bloc 3
debB = 450
Label(fen, text="=" * 15 + 'Traçage des courbes' +
      "=" * 15).place(x=tX + 10, y=debB - 25)
img.place(x=0, y=0, width=tX, height=tY)
minXc.place(x=tX + 10, y=debB)
minXe.place(x=tX + 190, y=debB, width=40)
maxXc.place(x=tX + 10, y=debB + 25)
maxXe.place(x=tX + 190, y=debB + 25, width=40)
minYc.place(x=tX + 10, y=debB + 50)
minYe.place(x=tX + 190, y=debB + 50, width=40)
maxYc.place(x=tX + 10, y=debB + 75)
maxYe.place(x=tX + 190, y=debB + 75, width=40)
cmdTrace.place(x=tX + 10, y=550, width=300, height=150)


mainloop()

os.system("pause")
