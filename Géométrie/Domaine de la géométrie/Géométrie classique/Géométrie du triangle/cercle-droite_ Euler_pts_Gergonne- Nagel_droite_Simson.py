#-*- coding: utf-8 -*-

# Python version 2.4.2
# Tk version 8.4
# IDLE version 1.1.2

# <<< DROITE et CERCLE d' EULER >>>

# f : facteur d'échelle lié à la résolution de l'écran du PC : on peut l'augmenter ou le diminuer

#########################################################
#   version 11

#Ce script a été vu, corrigé et amélioré par XEOLIN :
#  avec notamment :
#     - l' ajout d' un menu_bouton au clic droit de la souris
#     - l' ajout d'une fonction "who create it ?"
#     - l' ajout d'un widget "Scale" permettant de redimensionner la fenêtre à l'écran

#########################################################
#  PRESENTATION

# On considère le triangle quelconque ABC avec les points remarquables suivants :
#        G : centre de gravité
#        H : orthocentre
#        O : centre du cercle circonscrit
#        I   : centre du cercle inscrit
#        E : centre du  cercle d'Euler
#        Ge : point de Gergonne
#       N : point de Nagel

#  Le cercle d'Euler passe par les neufs points suivants :
#        les milieux des trois côtés du triangle :  mA, mB, mC
#        les pieds des hauteurs issues des trois sommets : hA, hB, hC
#        les milieux des segments joignant les trois sommets à l'orthocentre : aA, bB, cC
#  La droite d'Euler passe par les quatre points O, E, G, H :qui forment une division harmonique : EO / EG  =  HO / OG  ( = 3)
#  Les trois points G, I , N  sont alignés, avec la relation : GN =2*GI (on a aussi HN = 2*OI)

from tkinter import*
from math import *
from tkinter import messagebox
import os

def pop_up(event=None) :
            frame = Frame(root, relief=RIDGE)
            entry = Entry(frame, width = '21')
            menu = Menu(entry, tearoff = 0)
            menu.add_command(label ='Présentation du script', underline =0,command = rahxephon)
            menu.add_separator()
            menu.add_command(label ='Triangle', underline =0,command = animation_triangle)
            menu.add_separator()
            menu.add_command(label ='Centre de gravité', underline =0,command = centre_de_gravite)
            menu.add_command(label ='Orthocentre', underline =0,command = ortho_centre)
            menu.add_command(label ='Cercle circonscrit', underline =0,command = cercle_circonscrit)
            menu.add_command(label ='Cercle et droite d\' Euler', underline =0,command = Euler)
            menu.add_command(label ='Cercle inscrit', underline =0,command = cercle_inscrit)
            menu.add_command(label ='Points de Gergonne et de Nagel', underline =0,command = Gergonne_Nagel)
            menu.add_command(label ='Droite de Simpson', underline =0,command = Simpson)
            menu.add_command(label ='Figure de synthèse', underline =0,command = synthese)
            menu.add_separator()
            menu.add_command(label ='Stop !', underline =0,command = stop)
            menu.add_command(label ='Quitter le jeu !', underline =0,command = quitter)
            menu.add_separator()
            menu.add_command(label ='A propos', underline =0,command = hack_sing)
            ycoord = entry.winfo_pointery()
            xcoord = entry.winfo_pointerx()
            menu.tk_popup(xcoord, ycoord)

def naruto(event=None) :
    global f,L,H,xA,yA,xB,yB,xC,yC,dxA,dyA,dxB,dyB,dxC,dyC
    n=ss.get()
    f=int(n)
    L,H=120.*f,80.*f
    xA,yA,xB,yB,xC,yC=10*f,10*f,5*f,50*f,70*f,70*f
    dxA,dyA,dxB,dyB,dxC,dyC=0.2*f,0.2*f,0.2*f,0.2*f,0.2*f,-0.2*f
    can.configure(height=H,width=L)

def rahxephon():
    global fen1
    fen1=Tk()
    fen1.configure (bg='grey100')
    fen1.geometry("%sx%s+0+0"%(root.winfo_screenwidth(),root.winfo_screenheight()))
    fen1.overrideredirect(TRUE)
    Label(fen1,text="""\n
Les propriétés du triangle ont intéressé de nombreux mathématiciens au cours  des siècles.
Tous se sont attachés à repérer des points remarquables dans le triangle et à mettre en lumière les relations qui pouvaient exister entre ces points.
Il en est ainsi de la droite d'EULER qui relie le centre de gravité, l'orthocentre, le centre du cercle circonscrit et le centre du cercle d'Euler.\n
On trouvera un excellent document sur ce sujet sur le site suivant :\n
http://www.reunion.iufm.fr/dep/mathematiques/abracadabri/geoplane/cocyclik/CInsEx3.htm

On considère le triangle quelconque ABC avec les points remarquables suivants :
        G : centre de gravité
        H : orthocentre
        O : centre du cercle circonscrit
        I   : centre du cercle inscrit
        E : centre du  cercle d'Euler
        Ge : point de Gergonne
        N : point de Nagel

  Le cercle d'Euler passe par les neufs points suivants :
        les milieux des trois côtés du triangle :  mA, mB, mC
        les pieds des hauteurs issues des trois sommets : hA, hB, hC
        les milieux des segments joignant les trois sommets à l'orthocentre : aA, bB, cC
  La droite d'Euler passe par les quatre points O, E, G, H :qui forment une division harmonique : EO / EG  =  HO / OG  ( = 3)
  Les trois points G, I , N  sont alignés, avec la relation : GN =2*GI (on a aussi HN = 2*OI)
""",bg='grey100',fg='grey0',font='Arial 15 bold',justify=LEFT).pack()
    Button(fen1,text='OK',command=fen1.destroy).pack()
    fen1.mainloop()

def hack_sing():
    global fen
    fen=Tk()
    fen.configure (bg='grey0')
    fen.geometry("%sx%s+0+0"%(root.winfo_screenwidth(),root.winfo_screenheight()))
    fen.overrideredirect(TRUE)
    Label(fen,text="""\n\n\n\n\n\n\n\n\n\n\n\n
By HCD avec le concours de XEOLIN""",bg='grey0',fg='grey100',font='Arial 20 bold').pack()
    Button(fen,text='OK',font='Arial 10 bold',command=fen.destroy).pack()
    fen.mainloop()

def vitesse(a):
    "récupération de la valeur (a) choisie sur l'échelle"
    global k
    k=0.1*int(a) #affectation à la variable <k>

def animer():
    "résolution du triangle et animation "

    global xA,yA,xB,yB,xC,yC # coordonnées des sommets A, B, C
    global dxA,dyA,dxB,dyB,dxC,dyC # coordonnées des vecteurs vitesses des sommets A, B, C
    global a,b,c,p # longueur des côtés BC,CA,AB et demi périmètre
    global A,B,C #angles aux sommets A,B,C
    global xmA,ymA,xmB,ymB,xmC,ymC # coordonnées des milieux des côtés BC, CA, AB
    global xG,yG # coordonnées du centre de gravité (G)
    global xhA,yhA,xhB,yhB,xhC,yhC # coordonnées des pieds des hauteurs issues des trois sommets A, B, C
    global xH,yH # coordonnées de l'orthocentre (H)
    global  xO,yO,RO # coordonnées du centre (O) et rayon (RO) du cercle circonscrit
    global xE,yE,RE # coordonnées du centre (E) et rayon (RE) du cercle d'Euler
    global xaA,yaA,xbB,ybB,xcC,ycC # coordonnées des milieux des segments joignant les trois sommets à l'orthocentre
    global xGergonne,yGergonne,xNagel,yNagel # coordonnées des points de Gergonne et de Nagel
    global xI,yI,RI # coordonnées du centre (I) et rayon (RI) du cercle inscrit
    global xiA,yiA,xiB,yiB,xiC,yiC # coordonnées des points de contact entre le cercle inscrit et les côtés du triangle
    global xeA,yeA,xeB,yeB,xeC,yeC # coordonnées des points de contact entre les cercles exinscrits et les côtés du triangle
    global xM,yM,xMA,yMA,xMB,yMB,xMC,yMC
    global k
    k=0.9999*k
    if flag==1 :
        can.delete(ALL)
        # animation
        xA,yA,xB,yB,xC,yC=xA+k*dxA,yA+k*dyA,xB+k*dxB,yB+k*dyB,xC+k*dxC,yC+k*dyC

        # résolution du triangle
        a,b,c=hypot(xC-xB,yC-yB),hypot(xA-xC,yA-yC),hypot(xA-xB,yA-yB)
        p=(a+b+c)/2 # demi périmètre (p)
        RI=sqrt((p-a)*(p-b)*(p-c)/p)#  rayon (RI) du cercle inscrit
        if p==a:A=0
        if p==b:B=0
        if p==c:C=0
        if p==a or p==b or p==c:RI,RO=0,infini
        else:
            A,B,C=2*atan(RI/(p-a)),2*atan(RI/(p-b)),2*atan(RI/(p-c))# angles aux sommets
            RO=a*b*c/RI/p/4#  rayon (RO) du cercle circonscrit
        RE=RO/2 # rayon (RE) du cercle d'Euler

        # coordonnées des milieux des côtés BC, CA, AB et du centre de gravité G ( isobarycentre : A[1], B[1], C[1] )
        barycentre(0,1,1);xmA,ymA=x,y
        barycentre(1,0,1);xmB,ymB=x,y
        barycentre(1,1,0);xmC,ymC=x,y
        barycentre(1,1,1);xG,yG=x,y

        # coordonnées des pieds des hauteurs issues des trois sommets A, B, C et de l'orthocentre H : barycentre de A[tan(A)], B[tan(B)], C[tan(C)]
        barycentre(0,tan(B),tan(C));xhA,yhA=x,y
        barycentre(tan(A),0,tan(C));xhB,yhB=x,y
        barycentre(tan(A),tan(B),0);xhC,yhC=x,y
        barycentre(tan(A),tan(B),tan(C));xH,yH=x,y

        # coordonnées du centre (O)  du cercle circonscrit  : barycentre de A[sin(2*A)], B[sin(2*B)], C[sin(2*C)]
        barycentre(sin(2*A),sin(2*B),sin(2*C));xO,yO=x,y

        # coordonnées du centre (E) du cercle d'Euler
        xE,yE=(xO+xH)/2,(yO+yH)/2

        # coordonnées des milieux des segments joignant les trois sommets à l'orthocentre
        xaA,yaA= (xH+xA)/2,(yH+yA)/2
        xbB,ybB= (xH+xB)/2,(yH+yB)/2
        xcC,ycC= (xH+xC)/2,(yH+yC)/2

        # coordonnées du point de Gergonne : barycentre de A[(p-b)*(p-c)], B[(p-c)*(p-a)], C[(p-a)*(p-b)]
        barycentre((p-b)*(p-c),(p-c)*(p-a),(p-a)*(p-b));xGergonne,yGergonne=x,y

        # coordonnées du point de Nagel : barycentre de A[p-a], B[p-b], C[p-c]
        barycentre(p-a,p-b,p-c);xNagel,yNagel=x,y

        # coordonnées du centre (I) du cercle inscrit : barycentre de A[a], B[b], C[c]
        barycentre(a,b,c);xI,yI=x,y

        # coordonnées des points de contact entre le cercle inscrit et les côtés du triangle
        if p==a:xiA,yiA=0,0
        else:barycentre(0,(p-c)*(p-a),(p-a)*(p-b));xiA,yiA=x,y
        if p==b:xiB,yiB=0,0
        else:barycentre((p-b)*(p-c),0,(p-a)*(p-b));xiB,yiB=x,y
        if p==c:xiC,yiC=0,0
        else:barycentre((p-b)*(p-c),(p-c)*(p-a),0);xiC,yiC=x,y

        # coordonnées des points de contact entre les cercles exinscrit et les côtés du triangle
        xeA,yeA=2*xmA+-xiA,2*ymA+-yiA
        xeB,yeB=2*xmB+-xiB,2*ymB+-yiB
        xeC,yeC=2*xmC+-xiC,2*ymC+-yiC

        #  droite de Simpson
        xM=xO-RO/2
        yM=yO-sqrt(RO*RO-(xM-xO)*(xM-xO))
        if xB==xA:pC=infini
        else:pC=(yB-yA)/(xB-xA)
        if xC==xB:pA=infini
        else:pA=(yC-yB)/(xC-xB)
        if xA==xC:pB=infini
        else:pB=(yA-yC)/(xA-xC)
        xMC=(pC*(yM-yA)+xM+pC*pC*xA)/(1+pC*pC)
        yMC=(pC*(xM-xA)+yA+pC*pC*yM)/(1+pC*pC)
        xMA=(pA*(yM-yB)+xM+pA*pA*xB)/(1+pA*pA)
        yMA=(pA*(xM-xB)+yB+pA*pA*yM)/(1+pA*pA)
        xMB=(pB*(yM-yC)+xM+pB*pB*xC)/(1+pB*pB)
        yMB=(pB*(xM-xC)+yC+pB*pB*yM)/(1+pB*pB)

        # maintien du triangle dans le plan de jeu
        if xA<8 or xA>L-8:dxA,dxB,dxC=-dxA,-dxB,-dxC
        if xB<8 or xB>L-8:dxA,dxB,dxC=-dxA,-dxB,-dxC
        if xC<8 or xC>L-8:dxA,dxB,dxC=-dxA,-dxB,-dxC
        if yA<8 or yA>H-8:dyA,dyB,dyC=-dyA,dyB,dyC
        if yB<8 or yB>H-8:dyA,dyB,dyC=-dyA,-dyB,-dyC
        if yC<8 or yC>H-8:dyA,dyB,dyC=dyA,dyB,-dyC

        #lancement de l'animation des différentes figures
        if tt==1 and gg==0 and hh==0 and oo==0 and ee==0 and ii==0 and gn==0:animation_triangle()
        if tt==0 and gg==1 and hh==0 and oo==0 and ee==0 and ii==0 and gn==0:centre_de_gravite()
        if tt==0 and gg==0 and hh==1 and oo==0 and ee==0 and ii==0 and gn==0:ortho_centre()
        if tt==0 and gg==0 and hh==0 and oo==1 and ee==0 and ii==0 and gn==0:cercle_circonscrit()
        if tt==0 and gg==0 and hh==0 and oo==0 and ee==1 and ii==0 and gn==0:Euler()
        if tt==0 and gg==0 and hh==0 and oo==0 and ee==0 and ii==1 and gn==0:cercle_inscrit()
        if tt==0 and gg==0 and hh==0 and oo==0 and ee==0 and ii==0 and gn==1:Gergonne_Nagel()
        if tt==0 and gg==0 and hh==0 and oo==0 and ee==0 and ii==0 and gn==0 and ss==1:synthese()
        if tt==0 and gg==0 and hh==0 and oo==0 and ee==0 and ii==0 and gn==0 and ss==0 and sm==1:Simpson()

def barycentre(k1,k2,k3):
        " cette fonction donne les coordonnées x et y du barycentre des points A, B, C auxquels sont affectés les coefficients k1, k2, k3"
        global x,y
        m,n,o=k1,k2,k3
        x,y=(m*xA+n*xB+o*xC)/(m+n+o),(m*yA+n*yB+o*yC)/(m+n+o)

def animation_triangle():
    " A,B,C sont les sommets du triangle"
    global flag,tt,gg,hh,oo,ee,ii,gn
    flag,tt,gg,hh,oo,ee,ii,gn=1,1,0,0,0,0,0,0
    texte="A,B,C     sommets"
    information.config(text=texte)
    can.create_text(150,500,text="Le triangle a pour sommets A, B, C",fill="white")
    triangle()
    root.after(10,animer)

def triangle():
    "dessin du triangle"
    cote_AB=can.create_line(xA,yA,xB,yB,fill="red",width=2)
    cote_BC=can. create_line(xB,yB,xC,yC,fill="red",width=2)
    cote_CA=can. create_line(xC,yC,xA,yA,fill="red",width=2)
    sommet_A=can.create_oval(xA-8,yA-8,xA+8,yA+8,fill="red",width=1)
    sommet_B=can.create_oval(xB-8,yB-8,xB+8,yB+8,fill="red",width=1)
    sommet_C=can.create_oval(xC-8,yC-8,xC+8,yC+8,fill="red",width=1)
    lettre_A=can.create_text(xA,yA,text="A",fill="white")
    lettre_B=can.create_text(xB,yB,text="B",fill="white")
    lettre_C=can.create_text(xC,yC,text="C",fill="white")

def centre_de_gravite():
    " mA,mB,mC sont les milieux des côtés du triangle et G le centre de gravité"
    global flag,tt,gg,hh,oo,ee,ii
    flag,tt,gg,hh,oo,ee,ii,gn=1,0,1,0,0,0,0,0
    texte="A,B,C     sommets\nG     Centre de gravité"
    information.config(text=texte)
    can.create_text(150,500,text="Le centre de gravité G est à l' intersection \ndes droites issues des sommets A, B, C et \npassant par les milieux des côtés BC, CA, AB",fill="white")
    ligne_mA_A=can.create_line(xA,yA,xmA,ymA,fill='#007030',width=2)
    ligne_mB_B=can.create_line(xB,yB,xmB,ymB,fill='#007030',width=2)
    ligne_mC_C=can.create_line(xC,yC,xmC,ymC,fill='#007030',width=2)
    triangle()
    mA=can.create_oval(xmA-3,ymA-3,xmA+3,ymA+3,fill="pink",width=1)
    mB=can.create_oval(xmB-3,ymB-3,xmB+3,ymB+3,fill="pink",width=1)
    mC=can.create_oval(xmC-3,ymC-3,xmC+3,ymC+3,fill="pink",width=1)
    marqueur_G=can.create_oval(xG-8,yG-8,xG+8,yG+8,fill="pink",width=1)
    lettre_G=can.create_text(xG,yG,text="G",fill="black")
    root.after(10,animer)

def ortho_centre():
    " hA,hB,hC sont les pieds des hauteurs issues des sommets du triangle et H l'orthocentre"
    global flag,tt,gg,hh,oo,ee,ii,gn
    flag,tt,gg,hh,oo,ee,ii,gn=1,0,0,1,0,0,0,0
    texte="A,B,C     sommets\nH    orthocentre"
    information.config(text=texte)
    can.create_text(150,500,text="L' orthocentre H est à l' intersection \ndes hauteurs issues des sommets A, B, C",fill="white")
    ligne_hA_A=can.create_line(xA,yA,xhA,yhA,fill='#007030',width=2)
    ligne_hB_B=can.create_line(xB,yB,xhB,yhB,fill='#007030',width=2)
    ligne_hC_C=can.create_line(xC,yC,xhC,yhC,fill='#007030',width=2)
    ligne_hA_H=can.create_line(xH,yH,xhA,yhA,fill='#007030',width=2)
    ligne_hB_H=can.create_line(xH,yH,xhB,yhB,fill='#007030',width=2)
    ligne_hC_H=can.create_line(xH,yH,xhC,yhC,fill='#007030',width=2)
    triangle()
    hA=can.create_oval(xhA-3,yhA-3,xhA+3,yhA+3,fill="light blue",width=1)
    hB=can.create_oval(xhB-3,yhB-3,xhB+3,yhB+3,fill="light blue",width=1)
    hC=can.create_oval(xhC-3,yhC-3,xhC+3,yhC+3,fill="light blue",width=1)
    marqueur_H=can.create_oval(xH-8,yH-8,xH+8,yH+8,fill="light blue",width=1)
    lettre_H=can.create_text(xH,yH,text="H",fill="black")
    root.after(10,animer)

def cercle_circonscrit():
    "centre (O) et rayon (RO) du cercle circonscrit "
    global flag,tt,gg,hh,oo,ee,ii,gn
    flag,tt,gg,hh,oo,ee,ii,gn=1,0,0,0,1,0,0,0
    texte='''A,B,C     sommets\nO     centre du cercle circonscrit'''
    information.config(text=texte)
    can.create_text(150,500,text="Le centre (O) du cercle circonscrit est à  \nl' intersection des médiatrices des\ncôtés BC, CA, AB",fill="white")
    cercle_circonscrit=can.create_oval(xO-RO,yO-RO,xO+RO,yO+RO,outline='gold',width=1)
    ligne_mA_CT=can.create_line(xO,yO,xmA,ymA,fill='#007030',width=2)
    ligne_mB_CT=can.create_line(xO,yO,xmB,ymB,fill='#007030',width=2)
    ligne_mC_CT=can.create_line(xO,yO,xmC,ymC,fill='#007030',width=2)
    triangle()
    mA=can.create_oval(xmA-3,ymA-3,xmA+3,ymA+3,fill="gold",width=1)
    mB=can.create_oval(xmB-3,ymB-3,xmB+3,ymB+3,fill="gold",width=1)
    mC=can.create_oval(xmC-3,ymC-3,xmC+3,ymC+3,fill="gold",width=1)
    centre_cercle_circonscrit=can.create_oval(xO-8,yO-8,xO+8,yO+8,fill="gold",width=1)
    lettre_O=can.create_text(xO,yO,text="O",fill="black")
    root.after(10,animer)

def Euler():
    "centre (E) et rayon (RE) du cercle d'Euler et droite d'Euler"
    global flag,tt,gg,hh,oo,ee,ii,gn
    flag,tt,gg,hh,oo,ee,ii,gn=1,0,0,0,0,1,0,0
    texte="A,B,C     sommets\nG     Centre de gravité\nH    orthocentre\nO     centre du cercle circonscrit\nE     centre du cercle d' Euler"
    information.config(text=texte)
    can.create_text(250,500,text= '''Le cercle d' Euler passe par les 9 points suivants :
        - les milieux des trois côtés du triangle
        - les pieds des hauteurs issues des trois sommets
        - les milieux des segments joignant les trois sommets à l'orthocentre

La droite d' Euler relie les 4 points suivants:   G, H, O, E
        avec la relation    EO / EG = HO / OG ( = 3)''',fill="white")
    triangle()
    droite_Euler_1=can.create_line(xO,yO,xG,yG,fill="white",width=1)
    droite_Euler_2=can.create_line(xH,yH,xG,yG,fill="white",width=1)
    centre_cercle_Euler=can.create_oval(xE-8,yE-8,xE+8,yE+8,fill="white",width=1)
    cercle_Euler=can.create_oval(xE-RE,yE-RE,xE+RE,yE+RE,outline="white",width=1)
    lettre_E=can.create_text(xE,yE,text="E",fill="black")
    centre_cercle_circonscrit=can.create_oval(xO-8,yO-8,xO+8,yO+8,fill="gold",width=1)
    lettre_O=can.create_text(xO,yO,text="O",fill="black")
    marqueur_G=can.create_oval(xG-8,yG-8,xG+8,yG+8,fill="pink",width=1)
    lettre_G=can.create_text(xG,yG,text="G",fill="black")
    marqueur_H=can.create_oval(xH-8,yH-8,xH+8,yH+8,fill="light blue",width=1)
    lettre_H=can.create_text(xH,yH,text="H",fill="black")
    aA=can.create_oval(xaA-3,yaA-3,xaA+3,yaA+3,fill="green",width=1)
    bB=can.create_oval(xbB-3,ybB-3,xbB+3,ybB+3,fill="green",width=1)
    cC=can.create_oval(xcC-3,ycC-3,xcC+3,ycC+3,fill="green",width=1)
    mA=can.create_oval(xmA-3,ymA-3,xmA+3,ymA+3,fill="pink",width=1)
    mB=can.create_oval(xmB-3,ymB-3,xmB+3,ymB+3,fill="pink",width=1)
    mC=can.create_oval(xmC-3,ymC-3,xmC+3,ymC+3,fill="pink",width=1)
    hA=can.create_oval(xhA-3,yhA-3,xhA+3,yhA+3,fill="light blue",width=1)
    hB=can.create_oval(xhB-3,yhB-3,xhB+3,yhB+3,fill="light blue",width=1)
    hC=can.create_oval(xhC-3,yhC-3,xhC+3,yhC+3,fill="light blue",width=1)
    root.after(10,animer)

def cercle_inscrit():
    "centre (I) et rayon (RI) du cercle inscrit et droite reliant les points de Gergonne et de Nagel"
    global flag,tt,gg,hh,oo,ee,ii,gn
    flag,tt,gg,hh,oo,ee,ii,gn=1,0,0,0,0,0,1,0
    texte="A,B,C     sommets\nG     Centre de gravité\nI     centre du Cercle inscrit\nN     point de Nagel\nGe     point de Gergonne"
    information.config(text=texte)
    can.create_text(150,500,text="Le centre (I) du cercle inscrit est à l' intersection\ndes bissectrices issues des sommets    A, B, C",fill="white")
    ligne_A_I=can.create_line(xI,yI,xA,yA,fill='#007030',width=2)
    ligne_B_I=can.create_line(xI,yI,xB,yB,fill='#007030',width=2)
    ligne_C_I=can.create_line(xI,yI,xC,yC,fill='#007030',width=2)
    ligne_iA_I=can.create_line(xI,yI,xiA,yiA,fill='#007030',width=1)
    ligne_iB_I=can.create_line(xI,yI,xiB,yiB,fill='#007030',width=1)
    ligne_iC_I=can.create_line(xI,yI,xiC,yiC,fill='#007030',width=1)
    cercle_inscrit=can.create_oval(xI-RI,yI-RI,xI+RI,yI+RI,outline='yellow',width=1)
    triangle()
    centre_cercle_inscrit=can.create_oval(xI-8,yI-8,xI+8,yI+8,fill="yellow",width=1)
    lettre_I=can.create_text(xI,yI,text="I",fill="black")
    marqueur_iA=can.create_oval(xiA-3,yiA-3,xiA+3,yiA+3,fill="yellow",width=1)
    marqueur_iB=can.create_oval(xiB-3,yiB-3,xiB+3,yiB+3,fill="yellow",width=1)
    marqueur_iC=can.create_oval(xiC-3,yiC-3,xiC+3,yiC+3,fill="yellow",width=1)
    root.after(10,animer)

def Gergonne_Nagel():
    "centre (I) et rayon (RI) du cercle inscrit et droite reliant les points de Gergonne et de Nagel"
    global flag,tt,gg,hh,oo,ee,ii,gn
    flag,tt,gg,hh,oo,ee,ii,gn=1,0,0,0,0,0,0,1
    texte="A,B,C     sommets\nN     point de Nagel\nGe     point de Gergonne"
    information.config(text=texte)
    can.create_text(250,500,text= '''Le point de Gergonne est à l'intersection des droites issues des sommets et passant
par les points de contact du cercle inscrit avec les côtés du triangle

Le point de Nagel est à l'intersection des droites issues des sommets et passant par
les points de contact des cercles exinscrits avec les côtés du triangle

La droite de Nagel relie les 3 points suivants : N, G, I
        avec  la relation    IG = GN / 2''',fill="white")
    cercle_inscrit=can.create_oval(xI-RI,yI-RI,xI+RI,yI+RI,outline='#007030',width=1)
    ligne_iA_A=can.create_line(xA,yA,xiA,yiA,fill='#007030',width=2)
    ligne_iB_B=can.create_line(xB,yB,xiB,yiB,fill='#007030',width=2)
    ligne_iC_C=can.create_line(xC,yC,xiC,yiC,fill='#007030',width=2)
    ligne_eA_A=can.create_line(xA,yA,xeA,yeA,fill='#007030',width=2)
    ligne_eB_B=can.create_line(xB,yB,xeB,yeB,fill='#007030',width=2)
    ligne_eC_C=can.create_line(xC,yC,xeC,yeC,fill='#007030',width=2)
    triangle()
    droite_Nagel=can.create_line(xI,yI,xNagel,yNagel,fill="white",width=1)
    centre_cercle_inscrit=can.create_oval(xI-8,yI-8,xI+8,yI+8,fill="yellow",width=1)
    lettre_I=can.create_text(xI,yI,text="I",fill="black")
    point_de_Gergonne=can.create_oval(xGergonne-8,yGergonne-8,xGergonne+8,yGergonne+8,fill="light blue",width=1)
    lettre_Ge=can.create_text(xGergonne,yGergonne,text="Ge",fill="black")
    point_de_Nagel=can.create_oval(xNagel-8,yNagel-8,xNagel+8,yNagel+8,fill="orange",width=1)
    lettre_N=can.create_text(xNagel,yNagel,text="N",fill="black")
    marqueur_G=can.create_oval(xG-8,yG-8,xG+8,yG+8,fill="pink",width=1)
    lettre_G=can.create_text(xG,yG,text="G",fill="black")
    marqueur_iA=can.create_oval(xiA-3,yiA-3,xiA+3,yiA+3,fill="light blue",width=1)
    marqueur_iB=can.create_oval(xiB-3,yiB-3,xiB+3,yiB+3,fill="light blue",width=1)
    marqueur_iC=can.create_oval(xiC-3,yiC-3,xiC+3,yiC+3,fill="light blue",width=1)
    marqueur_eA=can.create_oval(xeA-3,yeA-3,xeA+3,yeA+3,fill="orange",width=1)
    marqueur_eB=can.create_oval(xeB-3,yeB-3,xeB+3,yeB+3,fill="orange",width=1)
    marqueur_eC=can.create_oval(xeC-3,yeC-3,xeC+3,yeC+3,fill="orange",width=1)
    root.after(10,animer)

def Simpson():
    " droite de Simpson"
    global flag,tt,gg,hh,oo,ee,ii,gn,ss,sm
    flag,tt,gg,hh,oo,ee,ii,gn,ss,sm=1,0,0,0,0,0,0,0,0,1
    texte="A,B,C     sommets\nM     est sur le cercle circonscrit\nsA,sB,sC     pieds des hauteurs issues de M"
    information.config(text=texte)
    can.create_text(150,500,text="La droite de Simpson relie \nles pieds des hauteurs issues de M",fill="white")
    triangle()
    ligne_sA_M=can.create_line(xM,yM,xMA,yMA,fill='#007030',width=2)
    ligne_sB_M=can.create_line(xM,yM,xMB,yMB,fill='#007030',width=2)
    ligne_sC_M=can.create_line(xM,yM,xMC,yMC,fill='#007030',width=2)
    ligne_sA_sB=can.create_line(xMB,yMB,xMA,yMA,fill='white',width=1)
    ligne_sB_sC=can.create_line(xMC,yMC,xMB,yMB,fill='white',width=1)
    ligne_sC_sA=can.create_line(xMA,yMA,xMC,yMC,fill='white',width=1)
    cercle_circonscrit=can.create_oval(xO-RO,yO-RO,xO+RO,yO+RO,outline='gold',width=1)
    marqueur_M=can.create_oval(xM-8,yM-8,xM+8,yM+8,fill="brown",width=1)
    lettre_M=can.create_text(xM,yM,text="M",fill="white")
    marqueur_sA=can.create_oval(xMA-8,yMA-8,xMA+8,yMA+8,fill="brown",width=1)
    lettre_sA=can.create_text(xMA,yMA,text="sA",fill="white")
    marqueur_sB=can.create_oval(xMB-8,yMB-8,xMB+8,yMB+8,fill="brown",width=1)
    lettre_sB=can.create_text(xMB,yMB,text="sB",fill="white")
    marqueur_sC=can.create_oval(xMC-8,yMC-8,xMC+8,yMC+8,fill="brown",width=1)
    lettre_sC=can.create_text(xMC,yMC,text="sC",fill="white")
    root.after(10,animer)

def synthese():
    " figure de synthèse"
    global flag,tt,gg,hh,oo,ee,ii,gn,ss
    flag,tt,gg,hh,oo,ee,ii,gn,ss=1,0,0,0,0,0,0,0,1
    texte="A,B,C     sommets\nG     Centre de gravité\nH    orthocentre\nO     centre du cercle circonscrit\nE     centre du cercle d' Euler\nI     centre du cercle inscrit\nN     point de Nagel\nGe     point de Gergonne"
    information.config(text=texte)
    can.create_text(150,500,text="Le centre (O) du cercle circonscrit est à  \nl' intersection des médiatrices des\ncôtés BC, CA, AB",fill="white")
    triangle()
    droite_Euler_1=can.create_line(xO,yO,xG,yG,fill="white",width=1)
    droite_Euler_2=can.create_line(xH,yH,xG,yG,fill="white",width=1)
    droite_Nagel=can.create_line(xI,yI,xNagel,yNagel,fill="white",width=1)
    marqueur_G=can.create_oval(xG-8,yG-8,xG+8,yG+8,fill="pink",width=1)
    lettre_G=can.create_text(xG,yG,text="G",fill="black")
    marqueur_H=can.create_oval(xH-8,yH-8,xH+8,yH+8,fill="light blue",width=1)
    lettre_H=can.create_text(xH,yH,text="H",fill="black")
    centre_cercle_circonscrit=can.create_oval(xO-8,yO-8,xO+8,yO+8,fill="gold",width=1)
    lettre_O=can.create_text(xO,yO,text="O",fill="black")
    centre_cercle_Euler=can.create_oval(xE-8,yE-8,xE+8,yE+8,fill="white",width=1)
    lettre_E=can.create_text(xE,yE,text="E",fill="black")
    centre_cercle_inscrit=can.create_oval(xI-8,yI-8,xI+8,yI+8,fill="yellow",width=1)
    lettre_I=can.create_text(xI,yI,text="I",fill="black")
    point_de_Gergonne=can.create_oval(xGergonne-8,yGergonne-8,xGergonne+8,yGergonne+8,fill="light blue",width=1)
    lettre_Ge=can.create_text(xGergonne,yGergonne,text="Ge",fill="black")
    point_de_Nagel=can.create_oval(xNagel-8,yNagel-8,xNagel+8,yNagel+8,fill="orange",width=1)
    lettre_N=can.create_text(xNagel,yNagel,text="N",fill="black")
    root.after(10,animer)

def stop():
    global flag
    flag=0
    dxA,dyA,dxB,dyB,dxC,dyC=0,0,0,0,0,0

def quitter():
    ans=messagebox.askyesno('',"Voulez-vous réellement quitter ?")
    if ans:root.quit()

######## Programme principal ############################################

root = Tk()
root.title("#>>>>>>>| DROITE et CERCLE d' EULER |<<<<<<<# By HCD and XEOLIN")

root.bind('<Button-3>',pop_up)
root.bind('<Alt-F12>',pop_up)# commande au clavier du menu pop-up

# Données initiales:
f=1  # facteur d'échelle lié à la résolution de l'écran du PC : on peut l'augmenter ou le diminuer
L,H=1200*f,800*f # largeur  et hauteur du plan
flag,tt,gg,hh,oo,ee,ii,gn,ss,sm=0,0,0,0,0,0,0,0,0,0
infini=tan(pi/2)
xA,yA,xB,yB,xC,yC=100*f,100*f,50.,500*f,700*f,700*f
dxA,dyA,dxB,dyB,dxC,dyC=0.1*f,0.1*f,0.1*f,0.1*f,0.1*f,-0.1*f

can=Canvas(root,bg='dark green',height=H,width=L)
can.grid(row=1,column=1,rowspan=2)
can2=Canvas(root,bg='brown',highlightbackground='brown')
can2.grid(row=1,column=2,sticky=N)

information=Label(can2,text="",height=16,width=36,relief=GROOVE,bg="brown",fg="white",justify=LEFT,command=None)
information.pack(padx=4,pady=4,side=BOTTOM,anchor=SW)
Button(can2,text='Quitter le jeu !',height=1,width=35,relief=GROOVE,bg="white",command=quitter).pack(padx=5,pady=5,side=BOTTOM,anchor=SW)
Button(can2,text='Stop !',height=1,width=35,relief=GROOVE,bg="white",activebackground="dark green",activeforeground="white",command=stop).pack(padx=4,pady=4,side=BOTTOM,anchor=SW)
Button(can2,text='Figure de synthèse',height=1,width=35,relief=GROOVE,bg="white",activebackground="dark green",activeforeground="white",command=synthese).pack(padx=4,pady=4,side=BOTTOM,anchor=SW)
Button(can2,text='Droite de Simpson',height=1,width=35,relief=GROOVE,bg="white",activebackground="dark green",activeforeground="white",command=Simpson).pack(padx=4,pady=4,side=BOTTOM,anchor=SW)
Button(can2,text='Points de Gergonne et de Nagel',height=1,width=35,relief=GROOVE,bg="white",activebackground="dark green",activeforeground="white",command=Gergonne_Nagel).pack(padx=4,pady=4,side=BOTTOM,anchor=SW)
Button(can2,text='Cercle inscrit',height=1,width=35,relief=GROOVE,bg="white",activebackground="dark green",activeforeground="white",command=cercle_inscrit).pack(padx=4,pady=4,side=BOTTOM,anchor=SW)
Button(can2,text='''Cercle et droite d' Euler''',height=1,width=35,relief=GROOVE,bg="white",activebackground="dark green",activeforeground="white",command=Euler).pack(padx=4,pady=4,side=BOTTOM,anchor=SW)
Button(can2,text='Cercle circonscrit',height=1,width=35,relief=GROOVE,bg="white",activebackground="dark green",activeforeground="white",command=cercle_circonscrit).pack(padx=4,pady=4,side=BOTTOM,anchor=SW)
Button(can2,text='Orthocentre',height=1,width=35,relief=GROOVE,bg="white",activebackground="dark green",activeforeground="white",command=ortho_centre).pack(padx=4,pady=4,side=BOTTOM,anchor=SW)
Button(can2,text='Centre de gravité',height=1,width=35,relief=GROOVE,bg="white",activebackground="dark green",activeforeground="white",command=centre_de_gravite).pack(padx=4,pady=4,side=BOTTOM,anchor=SW)
Button(can2,text='Triangle',height=1,width=35,relief=GROOVE,bg="white",activebackground="dark green",activeforeground="white",command=animation_triangle).pack(padx=4,pady=4,side=BOTTOM,anchor=SW)
kmin,kmax,kdef=0,10,1
vitesse_jeu=Scale(can2,length=215,orient=HORIZONTAL,sliderlength=11,label="Vitesse de l'animation    (entre 0 et 10)", from_ =kmin, to =kmax, troughcolor ='white',command =vitesse)
vitesse_jeu.pack(padx=1,pady=1,side=BOTTOM,anchor=SW)
vitesse_jeu.set(kdef)
ss=Scale(can2,length=215,orient=HORIZONTAL,sliderlength=11,label="Dimensionner la fenêtre    (entre 1 et 10)",from_ =1,to=10,showvalue=10,command=naruto)
ss.pack(padx=1,pady=1,side=BOTTOM,anchor=SW)
ss.set(7)
root.config(bg="brown")
root.mainloop()
root.destroy()

os.system("pause")
