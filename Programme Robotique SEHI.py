"""
Auteur : SEHI Lizie De Lima Ingénieur en Télécommunication
Programme : Simulateur robotique 2D
Description : Le programme permet de construire une interface pour la 
simulation du mouvement d'un robot manipulateur dans une dimension 2D.

"""
from tkinter import*
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math
from math import sqrt,cos,sin,degrees,radians,atan
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import numpy as np
from numpy import pi, sin, cos, sqrt
from random import randint, choice
import time
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation
from celluloid import Camera
import matplotlib.lines as mlines

#Création de la fenetre
global fenetre
fenetre=Tk()

#Personnalisation de la fenetre
largeur=1080
hauteur=620
fenetre.title("SIMULATEUR DE ROBOT MANIPULATEUR 2D")
fenetre.maxsize(largeur,hauteur)
fenetre.minsize(largeur,hauteur)
fenetre.config(background='white')

def mouvement() :
    
    #Definition du graphe
    fig = plt.figure(figsize=(5,4),dpi=100)
    ax = fig.add_subplot(1,1,1)
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.yaxis.set_ticks_position('right')
    ax.grid()
    ax.patch.set_facecolor('#E0E0E0')
    ax.set_xlabel("L'axe des Y")
    ax.set_ylabel("L'axe des X")
    ax.axis([8,-1,-1,8])
    chart = FigureCanvasTkAgg(fig,fenetre)
    chart.get_tk_widget().place(x=238, y=30)

    #Recuperation des valeurs des champs
    efface()
    #Tracé de graph
    L0=float(L0_LienChamp.get())
    L1=float(L1_LienChamp.get())
    L2=float(L2_LienChamp.get())
    th1=float(angle1_Champ.get())
    th2=float(angle2_Champ.get())
    by=float(Bx_Champ.get())
    bx=float(By_Champ.get())
    nbrpas=float(nbrpas_Champ.get())
    nbrpas=int(nbrpas)
    point_A=repereA3_A2_A1(L0,L1,L2,th1,th2)
    a3x=point_A[2][1]
    a3y=point_A[2][0]
    a2x=point_A[1][1]
    a2y=point_A[1][0]
    varx=a3x-bx
    vary=a3y-by
    xpoint_seg=[]
    ypoint_seg=[]
    angles_theta1_point=[]
    angles_theta2_point=[]
    A3pointx_graph=[]
    A3pointy_graph=[]
    A2pointx_graph=[]
    A2pointy_graph=[]
    
    #Ajout du point final à la liste
    angle=cal_theta(L0,L1,L2,by,bx)
    coordonne=repereA3_A2_A1(L0,L1,L2,angle[0],angle[1])
    A3pointx_graph.append(coordonne[2][1])
    A3pointy_graph.append(coordonne[2][0])
    A2pointx_graph.append(coordonne[1][1])
    A2pointy_graph.append(coordonne[1][0])
    
    #Fixation du repere
    fig = plt.figure(figsize=(5,4),dpi=100)
    ax = fig.add_subplot(1,1,1)
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.yaxis.set_ticks_position('right')
    ax.grid()
    ax.patch.set_facecolor('#E0E0E0')
    ax.set_xlabel("L'axe des Y")
    ax.set_ylabel("L'axe des X")
    ax.axis([8,-1,-1,8])
    chart = FigureCanvasTkAgg(fig,fenetre)
    chart.get_tk_widget().place(x=238, y=30)
    camp=Label(fenetre,text="Nombre",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=770, y=464)
    camp2=Label(fenetre,text="No",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=820, y=434)

    #Segmentation en nombre de pas
    for i in range(nbrpas-1) :
        xpoint_seg.append((i+1)*varx/(nbrpas)+bx)
        ypoint_seg.append((i+1)*vary/(nbrpas)+by)
    for i in range(nbrpas-1) :
        angle=cal_theta(L0,L1,L2,ypoint_seg[i],xpoint_seg[i])
        angles_theta1_point.append(angle[0])
        angles_theta2_point.append(angle[1])
    for i in range(nbrpas-1) :
        coordonne=repereA3_A2_A1(L0,L1,L2,angles_theta1_point[i],angles_theta2_point[i])
        A3pointx_graph.append(coordonne[2][1])
        A3pointy_graph.append(coordonne[2][0])
        A2pointx_graph.append(coordonne[1][1])
        A2pointy_graph.append(coordonne[1][0])
        
    # Animation
    ax.clear()
    ax.yaxis.set_ticks_position('right')
    ax.grid()
    ax.patch.set_facecolor('#E0E0E0')
    ax.set_xlabel("L'axe des Y")
    ax.set_ylabel("L'axe des X")
    ax.axis([8,-1,-1,8])
    chart = FigureCanvasTkAgg(fig,fenetre)
    chart.get_tk_widget().place(x=238, y=30)
    camp=Label(fenetre,text="Nombre",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=770, y=464)
    camp2=Label(fenetre,text="No",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=820, y=434)
    coordonne=repereA3_A2_A1(L0,L1,L2,th1,th2)
    ax.plot([bx,a3x],[by,a3y], '--', lw=2, color='black')

    for i in range(nbrpas-1) :
        ax.plot(xpoint_seg[i],ypoint_seg[i],'x', lw=5, color='red')
    ax.plot(bx,by,'o-', lw=5, color='green')
    ax.plot([0,0],[0,L0], lw=5, color='blue')
    x_points = [coordonne[0][0],coordonne[1][1],coordonne[2][1]]
    y_points = [coordonne[0][1],coordonne[1][0],coordonne[2][0]]
    tige, = ax.plot(x_points, y_points, 'o-', lw=5, color='blue')
    ax.plot(coordonne[2][1],coordonne[2][0],'o-', lw=5, color='black')
    tige.set_markevery(0.3)
    tige.set_mec('black')
    tige.set_mew('2.5')
    org, = ax.plot(coordonne[2][1], coordonne[2][0],marker=t,markersize=18,color="black")
    
    #ajout du point initiale a la liste
    pointfinal=repereA3_A2_A1(L0,L1,L2,th1,th2)
    A3pointx_graph.append(pointfinal[2][1])
    A3pointy_graph.append(pointfinal[2][0])
    A2pointx_graph.append(pointfinal[1][1])
    A2pointy_graph.append(pointfinal[1][0])    
    k=nbrpas
    #Tracage du sol
    ax.plot([-0.25,0.25], [0,0],'-', lw=5,color="black")
    ax.plot([0.45,6.85], [0,0],'--', lw=2,color="black")
    ax.text(7.5,-0.15, r'Sol', fontsize=15,fontfamily='Arial',style='italic',fontweight='bold')

    #Legend du graphe
    ax.plot([],[], "o",color='red',label="HORS DE SA PORTEE")
    ax.plot([],[], "o",color='green',label="A SA PORTEE")
    legend = ax.legend(fontsize=8)
    legend.get_frame().set_facecolor('#E0E0E0')
    print(len(A2pointx_graph))    

    for p in range(k+1):
        #Mise à jours des valeur
        x_points =[0,A2pointx_graph[k-p],A3pointx_graph[k-p]]
        y_points =[L0,A2pointy_graph[k-p],A3pointy_graph[k-p]] 
        tige.set_data(x_points,y_points)
        org.set_data(A3pointx_graph[k-p],A3pointy_graph[k-p])
        #Rafraichissement de la figure
        ax.axis([8,-1,-1,8])
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(1)

def dessiner() :
    efface()
    #Tracé de graph
    L0=float(L0_LienChamp.get())
    L1=float(L1_LienChamp.get())
    L2=float(L2_LienChamp.get())
    th1=float(angle1_Champ.get())
    th2=float(angle2_Champ.get())
    by=float(Bx_Champ.get())
    bx=float(By_Champ.get())
    nbrpas=float(nbrpas_Champ.get())
    nbrpas=int(nbrpas)
    ax.plot([0,0],[0,L0], lw=5, color='blue')
    ax.plot(float(By_Champ.get()),float(Bx_Champ.get()),'o-', lw=5, color='green')
    coordonne=repereA3_A2_A1(L0,L1,L2,th1,th2)
    L0_LienChamp.config(state=DISABLED)
    L1_LienChamp.config(state=DISABLED)
    L2_LienChamp.config(state=DISABLED)
    angle1_Champ.config(state=DISABLED)
    angle2_Champ.config(state=DISABLED)
    By_Champ.config(state=DISABLED)
    Bx_Champ.config(state=DISABLED)    
    bpdessiner.config(fg='black',bg='white',state=DISABLED)
    x_points = [coordonne[0][0],coordonne[1][1],coordonne[2][1]]
    y_points = [coordonne[0][1],coordonne[1][0],coordonne[2][0]]
    org, = ax.plot(coordonne[2][1], coordonne[2][0],marker=t,markersize=18,color="black")
    tige, = ax.plot(x_points, y_points, 'o-', lw=5, color='blue')
    tige.set_markevery(0.3)
    tige.set_mec('black')
    tige.set_mew('2.5')
    org, = ax.plot(coordonne[2][1], coordonne[2][0],marker=t,markersize=18,color="black")
    #Tracage du sol
    ax.plot([-0.25,0.25], [0,0],'-', lw=5,color="black")
    ax.plot([0.45,6.85], [0,0],'--', lw=2,color="black")
    ax.text(7.5,-0.15, r'Sol', fontsize=15,fontfamily='Arial',style='italic',fontweight='bold')
    #Legend du graphe
    ax.plot([],[], "o",color='red',label="HORS DE SA PORTEE")
    ax.plot([],[], "o",color='green',label="A SA PORTEE")
    legend = ax.legend(fontsize=8)
    legend.get_frame().set_facecolor('#E0E0E0')
    chart = FigureCanvasTkAgg(fig,fenetre)
    chart.get_tk_widget().place(x=238, y=30)
    camp=Label(fenetre,text="Nombre",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=770, y=464)
    camp2=Label(fenetre,text="No",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=820, y=434)

def sauver_img():
    #Tracé de graph
    L0=float(L0_LienChamp.get())
    L1=float(L1_LienChamp.get())
    L2=float(L2_LienChamp.get())
    th1=float(angle1_Champ.get())
    th2=float(angle2_Champ.get())
    ax.plot([0,0],[0,L0], lw=5, color='blue')
    ax.plot(float(By_Champ.get()),float(Bx_Champ.get()),'o-', lw=5, color='green')
    coordonne=repereA3_A2_A1(L0,L1,L2,th1,th2)
    L0_LienChamp.config(state=DISABLED)
    L1_LienChamp.config(state=DISABLED)
    L2_LienChamp.config(state=DISABLED)
    angle1_Champ.config(state=DISABLED)
    angle2_Champ.config(state=DISABLED)
    By_Champ.config(state=DISABLED)
    Bx_Champ.config(state=DISABLED)    
    bpdessiner.config(fg='black',bg='white',state=DISABLED)
    x_points = [coordonne[0][0],coordonne[1][1],coordonne[2][1]]
    y_points = [coordonne[0][1],coordonne[1][0],coordonne[2][0]]
    org, = ax.plot(coordonne[2][1], coordonne[2][0],marker=t,markersize=18,color="black")
    tige, = ax.plot(x_points, y_points, 'o-', lw=5, color='blue')
    tige.set_markevery(0.3)
    tige.set_mec('black')
    tige.set_mew('2.5')
    org, = ax.plot(coordonne[2][1], coordonne[2][0],marker=t,markersize=18,color="black")
    #Tracage du sol
    ax.plot([-0.25,0.25], [0,0],'-', lw=5,color="black")
    ax.plot([0.45,6.85], [0,0],'--', lw=2,color="black")
    ax.text(7.5,-0.15, r'Sol', fontsize=15,fontfamily='Arial',style='italic',fontweight='bold')

    #Legend du graphe
    ax.plot([],[], "o",color='red',label="HORS DE SA PORTEE")
    ax.plot([],[], "o",color='green',label="A SA PORTEE")
    legend = ax.legend(fontsize=8)
    legend.get_frame().set_facecolor('#E0E0E0')    
    camera = Camera(fig)
    plt.savefig("RobotoManipulateur.jpeg")
    chart = FigureCanvasTkAgg(fig,fenetre)
    chart.get_tk_widget().place(x=238, y=30)
    camp=Label(fenetre,text="Nombre",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=770, y=464)
    camp2=Label(fenetre,text="No",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=820, y=434)
    
def imprimer_pdf() :
    efface()
    #Tracé de graph
    L0=float(L0_LienChamp.get())
    L1=float(L1_LienChamp.get())
    L2=float(L2_LienChamp.get())
    th1=float(angle1_Champ.get())
    th2=float(angle2_Champ.get())
    by=float(Bx_Champ.get())
    bx=float(By_Champ.get())
    nbrpas=float(nbrpas_Champ.get())
    nbrpas=int(nbrpas)
    ax.plot([0,0],[0,L0], lw=5, color='blue')
    coordonne=repereA3_A2_A1(L0,L1,L2,th1,th2)
    L0_LienChamp.config(state=DISABLED)
    L1_LienChamp.config(state=DISABLED)
    L2_LienChamp.config(state=DISABLED)
    angle1_Champ.config(state=DISABLED)
    angle2_Champ.config(state=DISABLED)
    By_Champ.config(state=DISABLED)
    Bx_Champ.config(state=DISABLED)    
    bpdessiner.config(fg='black',bg='white',state=DISABLED)
    x_points = [coordonne[0][0],coordonne[1][1],coordonne[2][1]]
    y_points = [coordonne[0][1],coordonne[1][0],coordonne[2][0]]

    point_A=repereA3_A2_A1(L0,L1,L2,th1,th2)
    a3x=point_A[2][1]
    a3y=point_A[2][0]
    a2x=point_A[1][1]
    a2y=point_A[1][0]
    varx=a3x-bx
    vary=a3y-by
    xpoint_seg=[]
    ypoint_seg=[]
    angles_theta1_point=[]
    angles_theta2_point=[]
    A3pointx_graph=[]
    A3pointy_graph=[]
    A2pointx_graph=[]
    A2pointy_graph=[]    
    tige, = ax.plot(x_points, y_points, 'o-', lw=5, color='blue')
    tige.set_markevery(0.3)
    tige.set_mec('black')
    tige.set_mew('2.5')
    org, = ax.plot(coordonne[2][1], coordonne[2][0],marker=t,markersize=18,color="black")
    #Ajout du point final à la liste
    angle=cal_theta(L0,L1,L2,by,bx)
    coordonne=repereA3_A2_A1(L0,L1,L2,angle[0],angle[1])
    A3pointx_graph.append(coordonne[2][1])
    A3pointy_graph.append(coordonne[2][0])
    A2pointx_graph.append(coordonne[1][1])
    A2pointy_graph.append(coordonne[1][0])
    #Segmentation en nombre de pas
    for i in range(nbrpas-1) :
        xpoint_seg.append((i+1)*varx/(nbrpas)+bx)
        ypoint_seg.append((i+1)*vary/(nbrpas)+by)
    for i in range(nbrpas-1) :
        angle=cal_theta(L0,L1,L2,ypoint_seg[i],xpoint_seg[i])
        angles_theta1_point.append(angle[0])
        angles_theta2_point.append(angle[1])
    for i in range(nbrpas-1) :
        coordonne=repereA3_A2_A1(L0,L1,L2,angles_theta1_point[i],angles_theta2_point[i])
        A3pointx_graph.append(coordonne[2][1])
        A3pointy_graph.append(coordonne[2][0])
        A2pointx_graph.append(coordonne[1][1])
        A2pointy_graph.append(coordonne[1][0])    
    coordonne=repereA3_A2_A1(L0,L1,L2,th1,th2)
    ax.plot([bx,a3x],[by,a3y], '--', lw=2, color='black')
    for i in range(nbrpas-1) :
        ax.plot(xpoint_seg[i],ypoint_seg[i],'x', lw=5, color='red')
    #Tracage du sol
    ax.plot([-0.25,0.25], [0,0],'-', lw=5,color="black")
    ax.plot([0.45,6.85], [0,0],'--', lw=2,color="black")
    ax.text(7.5,-0.15, r'Sol', fontsize=15,fontfamily='Arial',style='italic',fontweight='bold')
    #Legend du graphe
    ax.plot([],[], "o",color='red',label="HORS DE SA PORTEE")
    ax.plot([],[], "o",color='green',label="A SA PORTEE")
    legend = ax.legend(fontsize=8)
    legend.get_frame().set_facecolor('#E0E0E0')
    ax.plot(float(By_Champ.get()),float(Bx_Champ.get()),'o-', lw=5, color='green')
    plt.savefig("RobotoManipulateur.pdf")    
    chart = FigureCanvasTkAgg(fig,fenetre)
    chart.get_tk_widget().place(x=238, y=30)
    camp=Label(fenetre,text="Nombre",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=770, y=464)
    camp2=Label(fenetre,text="No",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=820, y=434)

def efface() :
    L0_LienChamp.config(state=NORMAL)
    L1_LienChamp.config(state=NORMAL)
    L2_LienChamp.config(state=NORMAL)
    angle1_Champ.config(state=NORMAL)
    angle2_Champ.config(state=NORMAL)
    By_Champ.config(state=NORMAL)
    Bx_Champ.config(state=NORMAL)    
    bpdessiner.config(bg='black',fg='white',font=("Roboto",14),state=NORMAL)
    ax.clear()
    ax.yaxis.set_ticks_position('right')
    ax.grid()
    ax.patch.set_facecolor('#E0E0E0')
    ax.set_xlabel("L'axe des Y")
    ax.set_ylabel("L'axe des X")
    ax.axis([8,-1,-1,8])
    chart = FigureCanvasTkAgg(fig,fenetre)
    chart.get_tk_widget().place(x=238, y=30)
    camp=Label(fenetre,text="Nombre",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=770, y=464)
    camp2=Label(fenetre,text="No",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=820, y=434)

def nouveau():
    L0_LienChamp.delete(0,END)
    L1_LienChamp.delete(0,END)
    L2_LienChamp.delete(0,END)
    angle1_Champ.delete(0,END)
    angle2_Champ.delete(0,END)
    Bx_Champ.delete(0,END)
    By_Champ.delete(0,END)
    nbrpas_Champ.delete(0,END)
    
def quitter_fen():
    fenetre.quit()
    fenetre.destroy()
    
def sauverDeo():
    efface()    
    #Definition du graphe
    fig = plt.figure(figsize=(5,4),dpi=100)
    ax = fig.add_subplot(1,1,1)
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.yaxis.set_ticks_position('right')
    ax.grid()
    ax.patch.set_facecolor('#E0E0E0')
    ax.set_xlabel("L'axe des Y")
    ax.set_ylabel("L'axe des X")
    ax.axis([8,-1,-1,8])
    chart = FigureCanvasTkAgg(fig,fenetre)
    chart.get_tk_widget().place(x=238, y=30)
    camp=Label(fenetre,text="Nombre",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=770, y=464)
    camp2=Label(fenetre,text="No",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=820, y=434)    
    #Recuperation des valeurs des champs
    L0=float(L0_LienChamp.get())
    L1=float(L1_LienChamp.get())
    L2=float(L2_LienChamp.get())
    th1=float(angle1_Champ.get())
    th2=float(angle2_Champ.get())
    by=float(Bx_Champ.get())
    bx=float(By_Champ.get())
    nbrpas=float(nbrpas_Champ.get())
    nbrpas=int(nbrpas)
    point_A=repereA3_A2_A1(L0,L1,L2,th1,th2)
    a3x=point_A[2][1]
    a3y=point_A[2][0]
    a2x=point_A[1][1]
    a2y=point_A[1][0]
    varx=a3x-bx
    vary=a3y-by
    xpoint_seg=[]
    ypoint_seg=[]
    angles_theta1_point=[]
    angles_theta2_point=[]
    A3pointx_graph=[]
    A3pointy_graph=[]
    A2pointx_graph=[]
    A2pointy_graph=[]
    
    #Ajout du point final à la liste
    angle=cal_theta(L0,L1,L2,by,bx)
    coordonne=repereA3_A2_A1(L0,L1,L2,angle[0],angle[1])
    A3pointx_graph.append(coordonne[2][1])
    A3pointy_graph.append(coordonne[2][0])
    A2pointx_graph.append(coordonne[1][1])
    A2pointy_graph.append(coordonne[1][0])
    
    #Fixation du repere
    fig = plt.figure(figsize=(5,4),dpi=100)
    ax = fig.add_subplot(1,1,1)
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.yaxis.set_ticks_position('right')
    ax.grid()
    ax.patch.set_facecolor('#E0E0E0')
    ax.set_xlabel("L'axe des Y")
    ax.set_ylabel("L'axe des X")
    ax.axis([8,-1,-1,8])
    chart = FigureCanvasTkAgg(fig,fenetre)
    chart.get_tk_widget().place(x=238, y=30)
    camp=Label(fenetre,text="Nombre",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=770, y=464)
    camp2=Label(fenetre,text="No",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=820, y=434)

    #Segmentation en nombre de pas
    for i in range(nbrpas-1) :
        xpoint_seg.append((i+1)*varx/(nbrpas)+bx)
        ypoint_seg.append((i+1)*vary/(nbrpas)+by)
    for i in range(nbrpas-1) :
        angle=cal_theta(L0,L1,L2,ypoint_seg[i],xpoint_seg[i])
        angles_theta1_point.append(angle[0])
        angles_theta2_point.append(angle[1])
    for i in range(nbrpas-1) :
        coordonne=repereA3_A2_A1(L0,L1,L2,angles_theta1_point[i],angles_theta2_point[i])
        A3pointx_graph.append(coordonne[2][1])
        A3pointy_graph.append(coordonne[2][0])
        A2pointx_graph.append(coordonne[1][1])
        A2pointy_graph.append(coordonne[1][0])        
    # Animation
    ax.clear()
    ax.yaxis.set_ticks_position('right')
    ax.grid()
    ax.patch.set_facecolor('#E0E0E0')
    ax.set_xlabel("L'axe des Y")
    ax.set_ylabel("L'axe des X")
    ax.axis([8,-1,-1,8])
    chart = FigureCanvasTkAgg(fig,fenetre)
    chart.get_tk_widget().place(x=238, y=30)
    coordonne=repereA3_A2_A1(L0,L1,L2,th1,th2)
    ax.plot([bx,a3x],[by,a3y], '--', lw=2, color='black')
    for i in range(nbrpas-1) :
        ax.plot(xpoint_seg[i],ypoint_seg[i],'x', lw=5, color='red')
    ax.plot(bx,by,'o-', lw=5, color='green')
    ax.plot([0,0],[0,L0], lw=5, color='blue')
    x_points = [coordonne[0][0],coordonne[1][1],coordonne[2][1]]
    y_points = [coordonne[0][1],coordonne[1][0],coordonne[2][0]]
    tige, = ax.plot(x_points, y_points, 'o-', lw=5, color='blue')
    ax.plot(coordonne[2][1],coordonne[2][0],'o-', lw=5, color='black')
    tige.set_markevery(0.3)
    tige.set_mec('black')
    tige.set_mew('2.5')
    org, = ax.plot(coordonne[2][1], coordonne[2][0],marker=t,markersize=18,color="black")
    
    #ajout du point initiale a la liste
    pointfinal=repereA3_A2_A1(L0,L1,L2,th1,th2)
    A3pointx_graph.append(pointfinal[2][1])
    A3pointy_graph.append(pointfinal[2][0])
    A2pointx_graph.append(pointfinal[1][1])
    A2pointy_graph.append(pointfinal[1][0])
    k=nbrpas
    #Legend du graphe
    ax.plot([],[], "o",color='red',label="HORS DE SA PORTEE")
    ax.plot([],[], "o",color='green',label="A SA PORTEE")
    legend = ax.legend(fontsize=8)
    legend.get_frame().set_facecolor('#E0E0E0')    
    camera = Camera(fig)
    for p in range(k+1):
        ax.plot([bx,a3x],[by,a3y], '--', lw=2, color='black')
        for i in range(nbrpas-1) :
            ax.plot(xpoint_seg[i],ypoint_seg[i],'x', lw=5, color='red')        
        #Mise à jours des valeur
        x_points =[0,A2pointx_graph[k-p],A3pointx_graph[k-p]]
        y_points =[L0,A2pointy_graph[k-p],A3pointy_graph[k-p]]
        ax.plot(bx,by,'o-', lw=5, color='green')
        ax.plot([0,0],[0,L0], lw=5, color='blue')
        tg,=ax.plot(x_points,y_points,'o-', lw=5, color='blue')
        tg.set_markevery(0.3)
        tg.set_mec('black')
        tg.set_mew('2.5')
        ax.plot(coordonne[2][1],coordonne[2][0],'o-', lw=5, color='black')
        ax.plot(A3pointx_graph[k-p],A3pointy_graph[k-p],marker=t,markersize=18,color="black")
        print(A3pointx_graph[k-p])
        #Tracage du sol
        ax.plot([-0.25,0.25], [0,0],'-', lw=5,color="black")
        ax.plot([0.45,6.85], [0,0],'--', lw=2,color="black")
        ax.text(7.5,-0.15, r'Sol', fontsize=15,fontfamily='Arial',style='italic',fontweight='bold')
        #Rafraichissement de la figure
        ax.axis([8,-1,-1,8])
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(1)
        camera.snap()
    animation = camera.animate(interval=1500)
    animation.save('FIGURE.gif')

#Objets Conlonne 1
LienLabel=Label(fenetre,text="Valeurs des Liens",bg='white',fg='black',font=("Roboto",14)).place(height=50, x=40, y=24)
L0_LienLabel=Label(fenetre,text="L0",fg='black',bg='white',font=("Roboto",12)).place(x=2, y=125)
global L0_LienChamp
L0_LienChamp=Entry(fenetre,bg='#eeeeee')
L0_LienChamp.place(height=20,width=40, x=30, y=128)
L1_LienLabel=Label(fenetre,text="L1",fg='black',bg='white',font=("Roboto",12)).place(x=72, y=125)
global L1_LienChamp
L1_LienChamp=Entry(fenetre,bg='#eeeeee')
L1_LienChamp.place(height=20,width=40, x=100, y=128)
L2_LienLabel=Label(fenetre,text='L2',fg='black',bg='white',font=("Roboto",12)).place(x=142, y=125)
global L2_LienChamp
L2_LienChamp=Entry(fenetre,bg='#eeeeee')
L2_LienChamp.place(height=20,width=40, x=170, y=128)
angleLabel=Label(fenetre,text="Valeurs de θ1 et θ2",bg='white',fg='black',font=("Roboto",14)).place(height=50, x=40, y=224)
angle1_Label=Label(fenetre,text="θ1",fg='black',bg='white',font=("Roboto",12)).place(x=2, y=325)
global angle1_Champ
angle1_Champ=Entry(fenetre,bg='#eeeeee')
angle1_Champ.place(height=20,width=40, x=30, y=328)
angle2_Label=Label(fenetre,text="θ2",fg='black',bg='white',font=("Roboto",12)).place(x=72, y=325)
global angle2_Champ
angle2_Champ=Entry(fenetre,bg='#eeeeee')
angle2_Champ.place(height=20,width=40, x=100, y=328)

#Coordonnées de Bx By
cordBLabel=Label(fenetre,text="Coordonnées de B(x0,y0)",bg='white',fg='black',font=("Roboto",14))
cordBLabel.place(height=50, x=20, y=424)
Bx_Label=Label(fenetre,text="Xb",fg='black',bg='white',font=("Roboto",12)).place(x=2, y=525)
global Bx_Champ
Bx_Champ=Entry(fenetre,bg='#eeeeee')
Bx_Champ.place(height=20,width=40, x=30, y=528)
By_Label=Label(fenetre,text="Yb",fg='black',bg='white',font=("Roboto",12)).place(x=72, y=525)
global By_Champ 
By_Champ=Entry(fenetre,bg='#eeeeee')
By_Champ.place(height=20,width=40, x=100, y=528)

#Objet Colonne 3
global bpdessiner
bpdessiner=Button(fenetre,text="Dessiner",command=dessiner,bg='black',fg='white',font=("Roboto",14))
bpdessiner.place(height=30, x=900, y=24)
global bpMVT
bpMVT=Button(fenetre,text="Mouvement",bg='green',fg='white',font=("Roboto",14),command=mouvement)
bpMVT.place(height=30,x=890, y=125)
nbrpasLabel=Label(fenetre,text="Nombre de pas",bg='white',fg='black',font=("Roboto",14)).place(height=50, x=880, y=224)
global nbrpas_Champ
nbrpas_Champ=Entry(fenetre,bg='#eeeeee')
nbrpas_Champ.place(height=20,width=40, x=925, y=328)
global bpreprendre
bpreprendre=Button(fenetre,text="Reprendre",command=efface,bg='#aaaaaa',fg='black',font=("Roboto",14)).place(height=30, x=890, y=424)
global bpquiter
bpquiter=Button(fenetre,text="Quitter",command=quitter_fen,fg='black',bg='red',font=("Roboto",12))
bpquiter.place(x=910, y=525)

#------------------------------
####Menu de la fenetre
#-----------------------------
Fen_menu = Menu(fenetre)
fenetre.config(menu=Fen_menu)
fichier = Menu(Fen_menu,tearoff=0)
Fen_menu.add_cascade(label="Fichier",menu=fichier)
fichier.add_command(label="Nouveau",command=nouveau)
fichier.add_separator()
fichier.add_command(label="Sauvegarder en GIF",command=sauverDeo)
fichier.add_command(label="Sauvegarder en Image",command=sauver_img)
fichier.add_separator()
fichier.add_command(label="Imprimer",command=imprimer_pdf)
fichier.add_separator()
fichier.add_command(label="Quitter",command=quitter_fen)
aide = Menu(Fen_menu,tearoff=0)
Fen_menu.add_cascade(label="Aide",menu=aide)
aide.add_command(label="A propos")
aide.add_separator()
aide.add_command(label="Prise en Main")
aide.add_separator()
aide.add_command(label="Réference")

#---------------------------------
######Objet graphe Colonne 2
#---------------------------------
global fig
fig = plt.figure(figsize=(5,4),dpi=100) 
global ax
ax = fig.add_subplot(1,1,1)
fig = plt.figure()
ax = plt.subplot(111)
#ajout main robot : organe terminal
t = mpl.markers.MarkerStyle(marker='$\psi$')
t._transform = t.get_transform().rotate_deg(190)
#fixa des axes
ax.yaxis.set_ticks_position('right')
ax.grid()
ax.patch.set_facecolor('#E0E0E0')
ax.set_xlabel("L'axe des Y")
ax.set_ylabel("L'axe des X")
ax.axis([8,-1,-1,8])
ax.plot([],[], lw=5, color='blue')
chart = FigureCanvasTkAgg(fig,fenetre)
chart.get_tk_widget().place(x=238, y=30)
camp=Label(fenetre,text="Nombre",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=770, y=464)
camp2=Label(fenetre,text="No",bg='white',fg='white',font=("Roboto",14)).place(height=50, x=820, y=434)


######procedures MD et MI
def repereA3_A2_A1(l0,l1,l2,angle1,angle2) : 
    Lien_L0 = l0
    Lien_L1 = l1
    Lien_L2 = l2
    theta1 = angle1
    theta2 = angle2
    theta1=math.radians(theta1)
    theta2=math.radians(theta2)
    matrice_R1=np.array([[math.cos(theta1),-math.sin(theta1),0,Lien_L0],
                         [math.sin(theta1),math.cos(theta1),0,0],
                         [0,0,1,0],
                         [0,0,0,1]],dtype=np.float16)
    matrice_R2=np.array([[math.cos(theta2),-math.sin(theta2),0,Lien_L1],
                         [math.sin(theta2),math.cos(theta2),0,0],
                         [0,0,1,0],
                         [0,0,0,1]],dtype=np.float16)
    matrice_R0=np.dot(matrice_R1,matrice_R2)
    A_R2=np.array([[Lien_L2],[0],[0],[1]],dtype=np.float16)
    primA_R1=np.array([[Lien_L1],[0],[0],[1]],dtype=np.float16)
    primA_R0=np.dot(matrice_R1,primA_R1)
    A_R1=np.dot(matrice_R2,A_R2)
    A_R0=np.dot(matrice_R1,A_R1)
    A_0=np.array([[0],[Lien_L0],[0],[1]],dtype=np.float16)
    return A_0,primA_R0,A_R0
############fonction de calcul d'angle
def cal_theta(l0,l1,l2,bx,by) :
    w=l2
    x=by
    y=l0-bx
    z1=0
    z2=-l1
    b1=2*(y*z1+x*z2)
    b2=2*(x*z1-y*z2)
    b3=w**2-x**2-y**2-z1**2-z2**2
    X=b1
    Y=b2
    Z=b3
    if(Z==0) :
        Y=-Y
        if(X>0) :
            theta1=math.degrees(math.atan(Y/X))
        elif((X<0)&(Y>=0)):
            theta1=math.degrees(math.atan(Y/X))+180
        elif((X<0)&(Y<0)):
            theta1=math.degrees(math.atan(Y/X))-180
        elif((X==0)&(Y>0)):
            theta1=90
        elif((X==0)&(Y<0)):
            theta1=-90
        elif((X==0)&(Y==0)):
            theta1=0
    else :
        contenu=X*X+Y*Y-Z*Z
        racine = sqrt(contenu)
        numSin = Z*X+Y*racine
        numCos = Z*Y-X*racine
        denom = X**2+Y**2
        cosangle = numCos/denom
        sinangle = numSin/denom
        if(cosangle>0) :
            theta1 = degrees(atan(sinangle/cosangle))
        elif((cosangle<0)&(sinangle>=0)):
            theta1 = degrees(atan(sinangle/cosangle))+180
        elif((cosangle<0)&(sinangle<0)):
            theta1 = degrees(atan(sinangle/cosangle))-180
        elif((cosangle==0)&(sinangle>0)):
            theta1=90
        elif((cosangle==0)&(sinangle<0)):
            theta1=-90
        elif((cosangle==0)&(sinangle==0)):
            theta1=0
    Y1 = by*cos(radians(theta1))+y*sin(radians(theta1))+z1
    Y2 = by*sin(radians(theta1))-y*cos(radians(theta1))+z2
    ysin=Y1/l2
    xcos=Y2/l2
    if(xcos>0) :
        theta2 = degrees(atan(ysin/xcos))
    elif((xcos<0)&(ysin>=0)):
        theta2 = degrees(atan(ysin/xcos))+180
    elif((xcos<0)&(ysin<0)):
        theta2 = degrees(atan(ysin/xcos))-180
    elif((xcos == 0)&(ysin>0)):
        theta2 = 90
    elif((xcos == 0)&(ysin<0)):
        theta2 = -90
    elif((xcos ==0)&(ysin==0)):
        theta2=0
    return theta1,theta2

fenetre.mainloop()
