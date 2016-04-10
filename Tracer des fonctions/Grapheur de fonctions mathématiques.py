# -*- coding:utf-8 -*-

# http://codes-sources.commentcamarche.net/source/47096-grapheur-de-fonctions-mathematiques

# Grapheur mathématique
# Ecrit et immaginé par Amaury

from math import *
from tkinter import *
from tkinter import messagebox, filedialog
import sys, string, os
ux=0
global select,h,m,fen,root,lst1,a,can
save=[]
compteur=0
h=30
m=100
select="black"
cadre,selected,integer=False,False,False
croix=[]

def onInit():                                                                           #Création des axes de la fenêtre de traçage
    global xmin,xmax,ymin,ymax,pasx,pasy,save,lst1,a,compteur,uxx,ymin,uyy,selected,xo  #Trace la courbe entrée en effaçant les autres
    selected=False
    a=0
    h=30
    m=100
    lst1.delete(0,compteur)
    compteur=0
    can.create_rectangle(0,0,700,700,fill="white",outline="white")
    try:
        ent1.delete(0,len(str(xmin)))
        ent2.delete(0,len(str(xmax)))
        ent3.delete(0,len(str(pasx)))
        ent4.delete(0,len(str(ymin)))
        ent5.delete(0,len(str(ymax)))
        ent6.delete(0,len(str(pasy)))
    except:
        pass
    ent1.insert(0,str(-10))
    ent2.insert(0,str(10))
    ent3.insert(0,str(1))
    ent4.insert(0,str(-10))
    ent5.insert(0,str(10))
    ent6.insert(0,str(1))
    try:
            xmin=float(eval(ent1.get()))
    except SyntaxError:
            xmin=-10
    try:
            xmax=float(eval(ent2.get()))
    except SyntaxError:
            xmax=10
    try:
            pasx=float(eval(ent3.get()))
    except SyntaxError:
            pasx=1
    try:
            ymin=float(eval(ent4.get()))
    except SyntaxError:
            ymin=-10
    try:
            ymax=float(eval(ent5.get()))
    except SyntaxError:
            ymax=10
    try:
            pasy=float(eval(ent6.get()))
    except SyntaxError:
            pasy=1

    dx=float(xmax-xmin)
    dy=float(ymax-ymin)
    ux=700/dx
    uy=700/dy
    uxx=(dx/700)
    uyy=(dy/700)
    #Coordonnées du O(0,0):
    xo=ux*(-xmin)
    yo=uy*ymax
    # Axes:
    can.create_line(0,yo,700,yo,fill="red")
    can.create_line(xo,0,xo,700,fill="red")
    i=xo
    j=yo
    while i>-1:
        can.create_line(i,yo-2,i,yo+2,fill="red")
        i=i-(ux*pasx)
    while j>-1:
        can.create_line(xo-2,j,xo+2,j,fill="red")
        j=j-(uy*pasy)
    i=xo
    j=yo
    while i<701:
        can.create_line(i,yo-2,i,yo+2,fill="red")
        i=i+(ux*pasx)
    while j<701:
        can.create_line(xo-2,j,xo+2,j,fill="red")
        j=j+(uy*pasy)

    try:
        onCalc(str(ent10.get()),select,xo,yo,uy,uxx,xmin,1)
        save=list(ent10.get()),select
        lst1.insert(END,"f  (x)=  "+str(ent10.get())+"  "+str(select))
        compteur=compteur+1
    except SyntaxError:
        pass

def onAdd():                                                            #Ajoute la courbe entrée
    global select,h,xmin,xmax,ymin,ymax,pasx,pasy,lst1,compteur,uxx,yo,uy,ymin,uyy,selected,xo
    selected=False

    dx=float(xmax-xmin)
    dy=float(ymax-ymin)
    ux=700/dx
    uy=700/dy
    uxx=(dx/700)
    uyy=(dy/700)
    #Coordonnées du O(0,0):
    xo=ux*(-xmin)
    yo=uy*ymax
    # Axes:
    can.create_line(0,yo,700,yo,fill="red")
    can.create_line(xo,0,xo,700,fill="red")
    i=xo
    j=yo
    while i>-1:
        can.create_line(i,yo-2,i,yo+2,fill="red")
        i=i-(ux*pasx)
    while j>-1:
        can.create_line(xo-2,j,xo+2,j,fill="red")
        j=j-(uy*pasy)
    i=xo
    j=yo
    while i<701:
        can.create_line(i,yo-2,i,yo+2,fill="red")
        i=i+(ux*pasx)
    while j<701:
        can.create_line(xo-2,j,xo+2,j,fill="red")
        j=j+(uy*pasy)

    try:
        onCalc(str(ent10.get()),select,xo,yo,uy,uxx,xmin,1)
        save.append([str(ent10.get()),select])

        lst1.insert(END,"f  (x)=  " + str(ent10.get()) +"  "+str(select))
        compteur=compteur+1


    except SyntaxError:
        pass
    except NameError:
        onCalc(str(ent10.get()),"black",xo,yo,uy,uxx,xmin,1)
        lst1.insert(END,"dy/dx  (" + str(ent10.get()) + ")  "+str(select))


def Add(event):
    onAdd()


def onCalc(fonction,couleur,xo,yo,uy,uxx,xmin,e):                           #Créé la table de valeur de l'enssemble des points de la courbe
    global courbe,selected
    valeurs=[]
    a=0
    while a<701:
        x=float(xmin+(a*uxx))
        try:
            y=-eval(fonction)
            valeurs.append([x,y])
            a=a+1
        except ValueError:
            y=0
            valeurs.append([x,y])
            a=a+1
        except OverflowError:
            y=0
            valeurs.append([x,y])
            a=a+1
        except ZeroDivisionError:
            y=0
            valeurs.append([x,y])
            a=a+1
        except NameError:
            messagebox.showerror(title="Erreur de Syntaxe",message="""Fonction " """ + str(fonction) + """" inconnue""")
            break

    if e==2:
        courbe={}
        selected=True
    a=0
    while a<700:
        local0=valeurs[a]
        local1=valeurs[a+1]
        x1=a
        x2=a+1
        y1=int((local0[1]*uy)+yo)
        y2=int((local1[1]*uy)+yo)
        can.create_line(x1,y1,x2,y2,width=e,fill=couleur)
        if e==2:
            courbe[x1] = y1
        a=a+1
    can.create_line(0,yo,700,yo,fill="red")
    can.create_line(xo,0,xo,700,fill="red")


def onSelect(e):
    global select,liste,lbl

    select=listb.get(listb.curselection())
    if select == "black":
        lab.configure(text=select)
        listb.configure(bg="ivory")

    elif select=="autres":
        pop=Tk()
        liste=Listbox(pop)
        for  coul in  ["AliceBlue","AntiqueWhite","Aqua","Aquamarine","Azure","Beige","Bisque","BlanchedAlmond","Blue","BlueViolet","Brown","BurlyWood","CadetBlue","Chartreuse","Chocolate","Coral","CornflowerBlue","Cornsilk","Crimson","Cyan","DarkBlue","DarkCyan","DarkGoldenrod","DarkGray","DarkGreen","DarkKhaki","DarkMagenta","DarkOliveGreen","DarkOrange","DarkOrchid","DarkRed","DarkSalmon","DarkSeaGreen","DarkSlateBlue","DarkSlateGray","DarkTurquoise","DarkViolet","DeepPink","DeepSkyBlue","DimGray","DodgerBlue","FireBrick","FloralWhite","ForestGreen","Fuchsia","Gainsboro","Gold","Goldenrod","Gray","Green","GreenYellow","Honeydew","HotPink","IndianRed","Indigo","Khaki","Lavender","LavenderBlush","LawnGreen","LemonChiffon","LightBlue","LightCoral","LightCyan","LightGoldenrodYellow","LightGreen","LightSeaGreen","LightSkyBlue","LightSteelBlue","LightYellow","Lime","LimeGreen","Linen","Magenta","Maroon","MediumAquamarine","MediumBlue","MediumOrchid","MediumPurple","MediumSeaGreen","MediumSlateBlue","MediumSpringGreen","MediumTurquoise","MediumVioletRed","MidnightBlue","MintCream","MistyRose","Moccasin","NavajoWhite","Navy","OldLace","Olive","OliveDrab","Orange","OrangeRed","Orchid","PaleGoldenrod","PaleGreen","PaleTurquoise","PaleVioletRed","PapayaWhip","PeachPuff","Peru","Pink","Plum","PowderBlue","Purple","Red","RosyBrown","RoyalBlue","SaddleBrown","Salmon","SandyBrown","SeaGreen","Seashell","Sienna","Silver","SkyBlue","SlateBlue","SlateGray","SpringGreen","SteelBlue","Tan","Teal","Thistle","Tomato","Turquoise","Violet","Wheat","Yellow","YellowGreen"]:
            liste.insert(END,coul)

        scrollbar = Scrollbar(pop)
        liste.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=liste.yview)
        liste.bind('<Double-1>',onColor)
        liste.grid(row=0,column=0)
        scrollbar.grid(row=0,column=1)
        lbl=Button(pop,text="-",command=pop.destroy)
        lbl.grid(row=1,column=0)
        pop.mainloop()

    else:
        lab.configure(text=select)
        listb.configure(bg=select)

def onDerive():                                                         #Créé la table de valeur de la dérivée de la courbe
    global select,h,m,xmin,xmax,ymin,ymax,pasx,pasy,choix,compteur
    try:
            xmin=float(eval(ent1.get()))
    except SyntaxError:
            xmin=-10
    try:
            xmax=float(eval(ent2.get()))
    except SyntaxError:
            xmax=10
    try:
            pasx=float(eval(ent3.get()))
    except SyntaxError:
            pasx=1
    try:
            ymin=float(eval(ent4.get()))
    except SyntaxError:
            ymin=-10
    try:
            ymax=float(eval(ent5.get()))
    except SyntaxError:
            ymax=10
    try:
            pasy=float(eval(ent6.get()))
    except SyntaxError:
            pasy=1

    if len(choix)==2:
            messagebox.showerror(title="Erreur de Syntaxe",message="""Fonction invalide""")
    elif len(choix)==3:
            messagebox.showerror(title="Erreur de Syntaxe",message="""Fonction invalide""")
    elif len(choix)==4:
        onDeriv(choix[2],select,1)
        save.append(["derive",str(choix[2]),select])
        try:
            lst1.insert(END,"dy/dx  ("+str(choix[2])+")  " + str(select))
            compteur=compteur+1
        except:
            lst1.insert(END,"dy/dx  ("+str(ent10.get())+")  " + str(select))
            compteur=compteur+1

def onDeriv(fonction,couleur,e):
    global select,h,m,selected,courbe
    valeurs=[]
    a=0

    dx=float(xmax-xmin)
    dy=float(ymax-ymin)
    ux=700/dx
    uy=700/dy
    uxx=(dx/700)
    #Coordonnées du O(0,0):
    xo=ux*(-xmin)
    yo=uy*ymax
    i=xo
    j=yo
    while a<701:
        x=float(xmin+(a*uxx))
        try:
            y=-eval(fonction)
            valeurs.append([x,y])
            a=a+1
        except ValueError:
            y=0
            valeurs.append([x,y])
            a=a+1
        except OverflowError:
            y=0
            valeurs.append([x,y])
            a=a+1
        except ZeroDivisionError:
            y=0
            valeurs.append([x,y])
            a=a+1
        except NameError:
            messagebox.showerror(title="Erreur de Syntaxe",message="""Fonction " """ + str(fonction) + """" inconnue""")
            break
        a=a+1
    a=0
    if e==2:
        courbe={}
        selected=True
    while a<350:
        try:
            y4=y3
        except NameError:
            y4=0
        local0=valeurs[a]
        local1=valeurs[a+1]
        dy=local1[1]-local0[1]
        dx=local1[0]-local0[0]
        y3=dy/dx
        y1=int((y4*uy)+yo)
        y2=int((y3*uy)+yo)
        can.create_line(2*a,y1,2*(a+1),y2,width=e,fill=couleur)
        if e==2:
            courbe[2*a] = y1
            courbe[2*a+1] = y1
        a=a+1
    can.create_line(0,yo,700,yo,fill="red")
    can.create_line(xo,0,xo,700,fill="red")

def onHelp():
    messagebox.showinfo(title="Aide",message="""Syntaxe des fonctions usuelles pour Python:

- log(x)<=> log(x,base)
- Racine(x) <=> sqrt(x)
- x^n <=> x**n
- E(x) <=> int(x)
- H(x) Trace un échelon d'Heaviside
- sin(x), cos(x) et tan(x) n'ont pas de syntaxe particulière,
  de même que asin(x), acos(x) et atan(x).
- SH(x), CH(x) et TH(x) définissentles fonctions trigo hyperboliques
- aSH(x), aCH(x) et aTH(x) sont les réciproques de SH, CH et TH

Perdu une courbe? Un double clic dans l'historique surligne la courbe!!!""")

def onRefresh():
    global save,xmin,xmax,pasx,ymin,ymax,pasy,uxx,yo,uy,ymin,uyy,selected,xo
    can.create_rectangle(0,0,700,700,fill="white",outline="white")
    selected=False

    try:
            xmin=float(eval(ent1.get()))
    except SyntaxError:
            xmin=-10
    try:
            xmax=float(eval(ent2.get()))
    except SyntaxError:
            xmax=10
    try:
            pasx=float(eval(ent3.get()))
    except SyntaxError:
            pasx=1
    try:
            ymin=float(eval(ent4.get()))
    except SyntaxError:
            ymin=-10
    try:
            ymax=float(eval(ent5.get()))
    except SyntaxError:
            ymax=10
    try:
            pasy=float(eval(ent6.get()))
    except SyntaxError:
            pasy=1

    dx=float(xmax-xmin)
    dy=float(ymax-ymin)
    ux=700/dx
    uy=700/dy
    uxx=(dx/700)
    uyy=(dy/700)
    #Coordonnées du O(0,0):
    xo=ux*(-xmin)
    yo=uy*ymax
    # Axes:
    can.create_line(0,yo,700,yo,fill="red")
    can.create_line(xo,0,xo,700,fill="red")
    i=xo
    j=yo
    while i>-1:
        can.create_line(i,yo-2,i,yo+2,fill="red")
        i=i-(ux*pasx)
    while j>-1:
        can.create_line(xo-2,j,xo+2,j,fill="red")
        j=j-(uy*pasy)
    i=xo
    j=yo
    while i<701:
        can.create_line(i,yo-2,i,yo+2,fill="red")
        i=i+(ux*pasx)
    while j<701:
        can.create_line(xo-2,j,xo+2,j,fill="red")
        j=j+(uy*pasy)
    a=0
    g=len(save)
    while a<g:
        local=save[a]
        if len(local)==3:
            onDeriv(local[1],local[2],1)
        elif len(local)==2:
            onCalc(local[0],local[1],xo,yo,uy,uxx,xmin,1)
        elif len(local)==4:
            oncourbe(local[2],local[3],1)
        a=a+1

def Refresh(event):
    onRefresh()

def onZoom(facteur):
    global save,xmin,xmax,pasx,ymin,ymax,pasy,ent1,ent2,ent3,ent4,ent5,ent6,uxx,uyy
    try:
            xmin=float(eval(ent1.get()))
    except SyntaxError:
            xmin=-10
    try:
            xmax=float(eval(ent2.get()))
    except SyntaxError:
            xmax=10
    try:
            pasx=float(eval(ent3.get()))
    except SyntaxError:
            pasx=1
    try:
            ymin=float(eval(ent4.get()))
    except SyntaxError:
            ymin=-10
    try:
            ymax=float(eval(ent5.get()))
    except SyntaxError:
            ymax=10
    try:
            pasy=float(eval(ent6.get()))
    except SyntaxError:
            pasy=1
    ent1.delete(0,len(str(xmin)))
    ent2.delete(0,len(str(xmax)))
    ent3.delete(0,len(str(pasx)))
    ent4.delete(0,len(str(ymin)))
    ent5.delete(0,len(str(ymax)))
    ent6.delete(0,len(str(pasy)))
    if facteur=="init":
        ent1.delete(0,len(str(xmin)))
        ent2.delete(0,len(str(xmax)))
        ent3.delete(0,len(str(pasx)))
        ent4.delete(0,len(str(ymin)))
        ent5.delete(0,len(str(ymax)))
        ent6.delete(0,len(str(pasy)))
        ent1.insert(0,str(-10))
        ent2.insert(0,str(10))
        ent3.insert(0,str(1))
        ent4.insert(0,str(-10))
        ent5.insert(0,str(10))
        ent6.insert(0,str(1))
        onRefresh()
    else:
        xmin,xmax,ymin,ymax,pasx,pasy=xmin/facteur,xmax/facteur,ymin/facteur,ymax/facteur,pasx/facteur,pasy/facteur

        ent1.insert(0,str(xmin))
        ent2.insert(0,str(xmax))
        ent3.insert(0,str(pasx))
        ent4.insert(0,str(ymin))
        ent5.insert(0,str(ymax))
        ent6.insert(0,str(pasy))
        can.create_rectangle(0,0,700,700,fill="white",outline="white")
        dx=float(xmax-xmin)
        dy=float(ymax-ymin)
        ux=700/dx
        uy=700/dy
        uxx=(dx/700)
        #Coordonnées du O(0,0):
        xo=ux*(-xmin)
        yo=uy*ymax
        # Axes:
        can.create_line(0,yo,700,yo,fill="red")
        can.create_line(xo,0,xo,700,fill="red")
        i=xo
        j=yo
        while i>-1:
            can.create_line(i,yo-2,i,yo+2,fill="red")
            i=i-(ux*pasx)
        while j>-1:
            can.create_line(xo-2,j,xo+2,j,fill="red")
            j=j-(uy*pasy)
        i=xo
        j=yo
        while i<701:
            can.create_line(i,yo-2,i,yo+2,fill="red")
            i=i+(ux*pasx)
        while j<701:
            can.create_line(xo-2,j,xo+2,j,fill="red")
            j=j+(uy*pasy)
        a=0
        g=len(save)
        while a<g:
            local=save[a]
            if len(local)==3:
                onDeriv(local[1],local[2],1)
            elif len(local)==2:
                onCalc(local[0],local[1],xo,yo,uy,uxx,xmin,1)
            a=a+1

def onFact():
    try:
        facteur=float(ent11.get())
    except ValueError:
        facteur=1.
    onZoom(facteur)

def Fact(event):
    try:
        facteur=float(ent11.get())
    except ValueError:
        facteur=1.
    onZoom(facteur)

def oncourbe(fichier,couleur,e):
    global can,flag,select,ent1,ent2,en3,ent4,ent5,ent6,col,lst1,a
    flag=0
    try:
            xmin=float(eval(ent1.get()))
    except SyntaxError:
            xmin=-10
    try:
            xmax=float(eval(ent2.get()))
    except SyntaxError:
            xmax=10
    try:
            pasx=float(eval(ent3.get()))
    except SyntaxError:
            pasx=1
    try:
            ymin=float(eval(ent4.get()))
    except SyntaxError:
            ymin=-10
    try:
            ymax=float(eval(ent5.get()))
    except SyntaxError:
            ymax=10
    try:
            pasy=float(eval(ent6.get()))
    except SyntaxError:
            pasy=1

    dx=float(xmax-xmin)
    dy=float(ymax-ymin)
    ux=700/dx
    uy=700/dy
    uxx=(dx/700)
    #Coordonnées du O(0,0):
    xo=ux*(-xmin)
    yo=uy*ymax
    i=xo
    j=yo

    file = open(fichier,"r")
    temp=str(file.read())
    temp=temp.replace(",",".")
    file.close()
    file=open(fichier,"w")
    file.write(temp)
    file.close()
    file=open(fichier,"r")
    a=0
    liste=[]
    try:
        while a<700:
            liste.append((file.readline().split(";")))
            try:
                liste[a][0]=float(liste[a][0])
            except:
                liste[a][0]=0
            try:
                liste[a][1]=float(liste[a][1])
            except IndexError:
                liste[a].append(0)

            a=a+1
        a=0
        while a<699:
            x1=int((liste[a][0]*uxx)+xo)
            y1=int(yo-(liste[a][1]*uy))
            x2=int((liste[a+1][0]*uxx)+xo)
            y2=int(yo-(liste[a+1][1]*uy))
            can.create_line(int(x1),int(y1),int(x2),int(y2),width=e,fill=col)
            a=a+1
    except :
        flag=1

def onCol(e):
    global col,fen,listd,labd,liste,lbl

    col=listd.get(listd.curselection())
    if col == "black":
        labd.configure(text=select)
        listd.configure(bg="ivory")

    else:
        labd.configure(text=col)
        listd.configure(bg=col)


def onColor(e):
    global pop,liste,lbl,select,listb,lab
    col=liste.get(liste.curselection())
    try:
        if col == "black":
            liste.configure(bg="ivory")
            lbl.configure(text=col)
            lab.configure(text=col)

        else:
            liste.configure(bg=col)
            lbl.configure(text=col)
            lab.configure(text=col)
        select=col
        listb.configure(bg=col)
    except :
        pass

def quitter(e):
    global fen
    fen.destroy()


def onImport():
    global fen,ent100,root,col,listd,labd,ent1,ent2,en3,ent4,ent5,ent6,ent101,ent102,ent103,ent104
    fen=Tk()
    fen.bind('<Escape>',quitter)
    lbl1=Label(fen,text="Importer un classeur au format .csv:")
    lbl2=Label(fen,text="Emplacement:")
    lbl3=Label(fen,text="Couleur :")
    lbl4=Label(fen,text="Xmin=")
    lbl5=Label(fen,text="Xmax=")
    lbl6=Label(fen,text="Ymin=")
    lbl7=Label(fen,text="Ymax=")
    ent100=Entry(fen)
    ent101=Entry(fen)
    ent102=Entry(fen)
    ent103=Entry(fen)
    ent104=Entry(fen)
    bou1=Button(fen,text="Parcourir",command=onSearch)
    bou2=Button(fen,text="Ok",command=Importer)
    bou3=Button(fen,text="Annuler",command=fen.destroy)

    listd=Listbox(fen)
    scrollbar = Scrollbar(fen)

    labd=Label(fen,text="_")
    listd.grid(row=2,column=1,rowspan=2)
    scrollbar.grid(row=2,column=2,rowspan=2)
    labd.grid(row=2,column=3,rowspan=2)
    # Insertion des éléments dans la liste:
    for  coul in  ["gray", "blue", "orange", "yellow", "green", "cyan", "red", "pink", "gold","green","purple","brown","black","beige","autres"]:
            listd.insert(END,coul)

    # Un double click dans la liste appellera la fonction onSelect:
    listd.bind('<Double-1>',onCol)
    listd.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listd.yview)

    lbl1.grid(row=0,column=0,columnspan=3)
    lbl2.grid(row=1,column=0)
    lbl3.grid(row=2,column=0)
    lbl4.grid(row=4,column=0)
    lbl5.grid(row=4,column=2)
    lbl6.grid(row=5,column=0)
    lbl7.grid(row=5,column=2)
    ent101.grid(row=4,column=1)
    ent102.grid(row=4,column=3)
    ent103.grid(row=5,column=1)
    ent104.grid(row=5,column=3)
    ent100.grid(row=1,column=1,columnspan=2)
    bou1.grid(row=1,column=3)
    bou2.grid(row=6,column=2)
    bou3.grid(row=6,column=3)
    fen.title("Importation de données")
    fen.mainloop()

def onSearch():
    global fen,file,ent100
    file = tkFileDialog.askopenfilename(parent=fen,title='Choisissez le fichier .csv à importer:',filetypes = [("Tpus les fichiers", "*"),("Fichiers Excel","*.csv;*.prn")])
    ent100.insert(0,str(file))

def Importer():
    global fen,ent100,file,select,flag,ent101,ent102,ent103,ent104,save,root,compteur
    fichier=ent100.get()
    oncourbe(file,select,1)
    save.append([0,0,str(fichier),str(select)])
    lst1.insert(END,str(file)+" "+str(select))
    compteur=compteur+1

    try:
            xmin=float(eval(ent101.get()))
    except SyntaxError:
            xmin=-10
    try:
            xmax=float(eval(ent102.get()))
    except SyntaxError:
            xmax=10

    try:
            ymin=float(eval(ent103.get()))
    except SyntaxError:
            ymin=-10
    try:
            ymax=float(eval(ent104.get()))
    except SyntaxError:
            ymax=10

    ent1.insert(0,str(xmin))
    ent2.insert(0,str(xmax))
    ent4.insert(0,str(ymin))
    ent5.insert(0,str(ymax))
    onRefresh()

    fen.destroy()
    if flag==0:
        file = open(fichier,"r")
        temp=str(file.read())
        temp=temp.replace(".",",")
        file.close()
        file=open(fichier,"w")
        file.write(temp)
        file.close()
        messagebox.showinfo(title="Importation",message="""Le classeur " """ + str(fichier) + """" a bien été importé.""")
        root.update()
    elif flag==1:
        messagebox.showerror(title="Importation",message="""Une erreur est survenue lors de l'importation de " """ + str(fichier) + """" .""")


def onSurligne(e):
    global lst1,xmin,xmax,pasx,ymin,ymax,pasy,surline,choix

    dx=float(xmax-xmin)
    dy=float(ymax-ymin)
    ux=700/dx
    uy=700/dy
    uxx=(dx/700)
    #Coordonnées du O(0,0):
    xo=ux*(-xmin)
    yo=uy*ymax

    choix=lst1.get(lst1.curselection())
    choix=choix.split("  ")
    onRefresh()
    if len(choix)==2:
        oncourbe(choix[0],choix[1],2)
    elif len(choix)==3:
        onDeriv(choix[1],choix[2],2)
    elif len(choix)==4:
        onCalc(choix[2],choix[3],xo,yo,uy,uxx,xmin,2)

def pointeur(event):
    x=event.x
    y=event.y
    global chaine,uxx,xmin,ymin,xmax,ymax,pasx,pasy,uyy,coins,cadre,croix,selected,courbe,integer,bornes,borne1,borne2,lst1,choix

    erreur=False
    try:
        can.delete(croix[0],croix[1])
    except:
        pass

    if cadre==False and selected==False and integer==False:
        chaine.configure(text = "Clic détecté en X =" + str(xmin+(x)*uxx) +", Y =" + str(ymin+(700-y)*uyy))
        croix=[can.create_line(x-5,y,x+5,y,fill="red"),can.create_line(x,y-5,x,y+5,fill="red")]

    elif cadre==False and selected==True and integer==False:
        chaine.configure(text = "Point de la courbe en X =" + str(xmin+(x)*uxx) +", Y =" + str(ymin+(700-courbe[x])*uyy))
        croix=[can.create_line(x-5,courbe[x],x+5,courbe[x],fill="red"),can.create_line(x,courbe[x]-5,x,courbe[x]+5,fill="red")]

    elif cadre==False and selected==True and integer==True and len(bornes)==0:
        chaine.configure(text = "Calcul d'intégrale: Borne inférieure=" + str(xmin+(x)*uxx) +", Borne Supérieure")
        croix=[can.create_line(x-5,courbe[x],x+5,courbe[x],fill="red"),can.create_line(x,courbe[x]-5,x,courbe[x]+5,fill="red")]
        borne1=can.create_line(x,0,x,700,fill="Gray")
        bornes.append(x)

    elif cadre==False and selected==True and integer==True and len(bornes)==1:
        chaine.configure(text = "Calcul d'intégrale: Borne inférieure=" + str(xmin+(bornes[0])*uxx) +", Borne Supérieure=" + str(xmin+(x)*uxx))
        croix=[can.create_line(x-5,courbe[x],x+5,courbe[x],fill="red"),can.create_line(x,courbe[x]-5,x,courbe[x]+5,fill="red")]
        borne2=can.create_line(x,0,x,700,fill="Gray")
        bornes.append(x)

        if messagebox.askokcancel('Confirmer','La borne inférieure est ' + str(xmin+(bornes[0])*uxx) + '\nLa borne supérieure est ' + str(xmin+(bornes[1])*uxx)):

            if len(choix)==2:
                couleur=choix[1]
            elif len(choix)==3:
                couleur=choix[2]
            elif len(choix)==4:
                couleur=choix[3]
            chaine.configure(text = "Calcul d'intégrale: Aire="+ str(integrale(courbe,bornes[0],bornes[1],couleur)) +" Borne inférieure=" + str(xmin+(bornes[0])*uxx) +", Borne Supérieure=" + str(xmin+(x)*uxx))

        else:
            chaine.configure(text = "Cliquez sur le graphique pour afficher les coordonnées d'un point.")
            onRefresh()

        can.delete(borne1,borne2)


    elif len(coins)==0 and selected==False and integer==False:
        coins.append([xmin+x*uxx , ymin+(700-y)*uyy])
        croix=[can.create_line(x-5,y,x+5,y,fill="red"),can.create_line(x,y-5,x,y+5,fill="red")]

    elif len(coins)==1 and selected==False and integer==False:
        coins.append([xmin+x*uxx , ymin+(700-y)*uyy])

        ent1.delete(0,len(str(xmin)))
        ent2.delete(0,len(str(xmax)))
        ent4.delete(0,len(str(ymin)))
        ent5.delete(0,len(str(ymax)))

        x1,y1,x2,y2=coins[0][0],coins[0][1],coins[1][0],coins[1][1]

        if x1<x2:
            ent1.insert(0,str(x1))
            ent2.insert(0,str(x2))

        elif x2<x1:
            ent1.insert(0,str(x2))
            ent2.insert(0,str(x1))

        else:
            erreur=True
            messagebox.showerror(title="Erreur",message="""Cadre d'épaisseur nulle. \n Les coordonnées d'origine seront restaurées""")
            ent1.delete(0,len(str(xmin)))
            ent2.delete(0,len(str(xmax)))
            ent3.delete(0,len(str(pasx)))
            ent4.delete(0,len(str(ymin)))
            ent5.delete(0,len(str(ymax)))
            ent6.delete(0,len(str(pasy)))
            ent1.insert(0,str(-10))
            ent2.insert(0,str(10))
            ent3.insert(0,str(1))
            ent4.insert(0,str(-10))
            ent5.insert(0,str(10))
            ent6.insert(0,str(1))

        if y1<y2:
            ent4.insert(0,str(y1))
            ent5.insert(0,str(y2))

        elif y2<y1:
            ent4.insert(0,str(y2))
            ent5.insert(0,str(y1))

        elif erreur!=True:
            messagebox.showerror(title="Erreur",message="""Cadre d'épaisseur nulle. \n Les coordonnées d'origine seront restaurées""")
            ent1.delete(0,len(str(xmin)))
            ent2.delete(0,len(str(xmax)))
            ent3.delete(0,len(str(pasx)))
            ent4.delete(0,len(str(ymin)))
            ent5.delete(0,len(str(ymax)))
            ent6.delete(0,len(str(pasy)))
            ent1.insert(0,str(-10))
            ent2.insert(0,str(10))
            ent3.insert(0,str(1))
            ent4.insert(0,str(-10))
            ent5.insert(0,str(10))
            ent6.insert(0,str(1))

        coins=[]
        erreur=False
        cadre=False
        chaine.configure(text = "Clic détecté en X =" + str(xmin+(x)*uxx) +", Y =" + str(ymin+(700-y)*uyy))
        onRefresh()

    else:
        chaine.configure(text = "Choisir une courbe")

def onCadre():
    global chaine,cadre,coins,croix
    chaine.configure(text = "Zoom par Cadre: définissez les deux coins du cadre")
    cadre=True
    try:
        can.delete(croix[0],croix[1])
    except:
        croix=[can.create_line(0,350,700,350,fill="red"),can.create_line(350,0,350,700,fill="red")]
    coins=[]

def integrale(courbe,inff,supp,couleur):
    global uxx,uyy,ymin,xo
    aire=0
    largeur=abs(supp-inff)
    if inff<supp:
        positif,erreur=True,False
        inf,sup=inff,supp

    elif inff>supp:
        inf,sup=supp,inff
        positif,erreur=False,False

    else:
        erreur,positif=True,True

    if erreur==False:
        a=inf
        while a<sup+1:
            try:
                can.create_line(a,xo,a,courbe[a],fill=couleur)
                aire=aire+(ymin+(700-courbe[a])*uyy)*uxx
            except:
                pass
            a=a+1

    if positif==True:
        return aire

    elif positif==False:
        return -aire

    elif erreur==True:
        return 0

def onInteger():
    global chaine,integer,bornes,coins,pop,inff,supp
    if messagebox.askyesno('Information','Voulez-vous entrer les bornes au clavier ?'):
        pop=Tk()
        lbl1=Label(pop,text="Borne inférieure =")
        lbl2=Label(pop,text="Borne supérieure =")
        inff=Entry(pop)
        supp=Entry(pop)
        inff.bind("<Return>",Take)
        supp.bind("<Return>",Take)
        bou=Button(pop,text="Ok",command=onTake)
        lbl1.grid(row=0,column=0)
        lbl2.grid(row=1,column=0)
        inff.grid(row=0,column=1)
        supp.grid(row=1,column=1)
        bou.grid(row=2,column=0,columnspan=2)

    else:
        chaine.configure(text = "Calcul d'intégrale: Borne inférieure")
        integer=True
    bornes=[]
    coins=[]

def Take(e):
    onTake()

def onTake():
    global pop,lst1,chaine,inff,supp,choix,xmin,uxx
    try:
        bornes=[int((eval(inff.get())*uy)+yo),int((eval(supp.get())*uy)+yo)]

    except:
        messagebox.showerror(title="Erreur",message="""Champs incomplets""")

    try:
        if len(choix)==2:
            couleur=choix[1]
        elif len(choix)==3:
            couleur=choix[2]
        elif len(choix)==4:
            couleur=choix[3]
    except:
        messagebox.showerror(title="Erreur",message="""Veuillez choisir une courbe""")

    chaine.configure(text = "Calcul d'intégrale: Aire=" + str(integrale(courbe,bornes[0],bornes[1],couleur)) + ", Borne inférieure=" + str(xmin+(bornes[0])*uxx) +", Borne Supérieure=" + str(xmin+(bornes[1])*uxx))
    pop.destroy()

def onClose():
    try:
        root.destroy()
    except:
        pass
    try:
        divide.destroy()
    except:
        pass

############################### Fonctions Mathématiques ###############################

def H(x):
    return (atan(x)+atan(1/x)+(pi/2))/pi

def SH(x):
    return (exp(x)-exp(-x))/2

def CH(x):
    return (exp(x)+exp(-x))/2

def TH(x):
    return SH(x)/CH(x)

def aSH(x):
    return log((x+sqrt(1+x**2)),exp(1))

def aCH(x):
    return log((x+sqrt(-1+x**2)),exp(1))

def aTH(x):
    return (-1+x**2)/(1+x**2)

def h(x):
    return (atan(x)+atan(1/x)+(pi/2))/pi

def sh(x):
    return (exp(x)-exp(-x))/2

def ch(x):
    return (exp(x)+exp(-x))/2

def th(x):
    return SH(x)/CH(x)

def ash(x):
    return log((x+sqrt(1+x**2)),exp(1))

def ach(x):
    return log((x+sqrt(-1+x**2)),exp(1))

def ath(x):
    return (-1+x**2)/(1+x**2)

def ln(x):
    return log(x,exp(1))

#######################################################################################

################################# Interface Graphique #################################
root=Tk()

if root.winfo_screenwidth()>1024:           #Ajuste la présentation du programme à la résolution de l'écran
    divide=root
    can=Canvas(divide,width=700,height=700)
else:
    self=Tk()
    divide=self
    can=Canvas(divide,width=700,height=700)

can.bind("<Button-1>", pointeur)
can.create_rectangle(0,0,700,700,fill="white",outline="black")
can.grid (row=0,column=0,rowspan=30)

chaine=Label(divide,text="Cliquez sur le graphique pour afficher les coordonnées d'un point.")
chaine.grid(row=30,column=0)

lbl1=Label(root,text="Configuration de la fenètre de traçage:")
lbl2=Label(root,text="Xmin =")
lbl3=Label(root,text="Xmax =")
lbl4=Label(root,text="Ymin =")
lbl5=Label(root,text="Ymax =")
lbl6=Label(root,text="Pas =")
lbl7=Label(root,text="Pas =")

listb=Listbox(root)
scrollbar = Scrollbar(root)

lab=Label(root,text="_")
listb.grid(row=10,column=2,rowspan=5)
scrollbar.grid(row=10,column=3,rowspan=5)
lab.grid(row=10,column=1)
# Insertion des éléments dans la liste:
for  coul in  ["gray", "blue", "orange", "yellow", "green", "cyan", "red", "pink", "gold","green","purple","brown","black","autres"]:
        listb.insert(END,coul)

# Un double click dans la liste appellera la fonction onSelect:
listb.bind('<Double-1>',onSelect)
listb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listb.yview)

ent1=Entry(root)
ent2=Entry(root)
ent3=Entry(root)
ent4=Entry(root)
ent5=Entry(root)
ent6=Entry(root)
bou1=Button(root,text="Nouvelle trace",command=onInit)
bou2=Button(root,text="Quitter",command=onClose)
bou3=Button(root,text="Ajouter trace",command=onAdd)
bou4=Button(root,text="Tracer dérivée",command=onDerive)
bou5=Button(root,text="Aide",command=onHelp)
bou6=Button(root,text="Rafraichir",command=onRefresh)
bou7=Button(root,text="Importer des Données",command=onImport)
bou8=Button(root,text="Calcul d'intégrale",command=onInteger)

bou1.grid(row=28,column=1)
bou2.grid(row=29,column=2)
bou3.grid(row=27,column=1)
bou4.grid(row=27,column=2)
bou5.grid(row=29,column=1)
bou6.grid(row=28,column=2)
bou7.grid(row=26,column=2)
bou8.grid(row=26,column=1)
lbl1.grid(row=0,column=1,columnspan=2)
lbl2.grid(row=1,column=1)
lbl3.grid(row=2,column=1)
lbl4.grid(row=4,column=1)
lbl5.grid(row=5,column=1)
lbl6.grid(row=3,column=1)
lbl7.grid(row=6,column=1)

ent1.grid(row=1,column=2)
ent2.grid(row=2,column=2)
ent3.grid(row=3,column=2)
ent4.grid(row=4,column=2)
ent5.grid(row=5,column=2)
ent6.grid(row=6,column=2)

ent1.bind ("<Return>",Refresh)
ent2.bind ("<Return>",Refresh)
ent3.bind ("<Return>",Refresh)
ent4.bind ("<Return>",Refresh)
ent5.bind ("<Return>",Refresh)
ent6.bind ("<Return>",Refresh)

lbl10=Label(root,text="Configuration du Grapheur:")
lbl11=Label(root,text="f(x)=")

ent10=Entry(root)
ent10.bind("<Return>",Add)

lbl10.grid(row=8,column=1,columnspan=2)
lbl11.grid(row=9,column=1)
ent10.grid(row=9,column=2)
ent11=Entry(root)
bou10=Button(root,text="Zoom x2",command=lambda arg=2.:onZoom(arg))
bou11=Button(root,text="Zoom x4",command=lambda arg=4.:onZoom(arg))
bou12=Button(root,text="Zoom /2",command=lambda arg=0.5:onZoom(arg))
bou13=Button(root,text="Zoom /4",command=lambda arg=0.25:onZoom(arg))
bou14=Button(root,text="Zoom par facteur",command=onFact)
bou15=Button(root,text="Zoom Initial",command=lambda arg="init":onZoom(arg))
bou16=Button(root,text="Zoom par Cadre",command=onCadre)
bou10.grid(row=20,column=1)
bou11.grid(row=20,column=2)
bou12.grid(row=21,column=1)
bou13.grid(row=21,column=2)
bou14.grid(row=22,column=1)
bou15.grid(row=23,column=1)
bou16.grid(row=23,column=2)

ent11.grid(row=22,column=2)
ent11.bind("<Return>",Fact)

lst1=Listbox(root)
bar = Scrollbar(root)
bar2 = Scrollbar(root,orient = HORIZONTAL)

bar.grid(row=1,column=5,rowspan=5)
bar2.grid(row=6,column=4)

lst1.bind('<Double-1>',onSurligne)
lst1.config(yscrollcommand=bar.set)
lst1.config(xscrollcommand=bar2.set)
bar.config(command=lst1.yview)
bar2.config(command=lst1.xview)

title=Label(root,text="Historique :")
title.grid(row=0,column=4)
lst1.grid(row=1,column=4,rowspan=5)

onInit()

root.resizable(False,False)
divide.resizable(False,False)
root.title("Paramètres Grapheur")
divide.title("Tracés Grapheur")
divide.protocol("WM_DELETE_WINDOW", onClose)
root.protocol("WM_DELETE_WINDOW", onClose)

root.mainloop()
divide.mainloop()

os.system("pause")
#######################################################################################
