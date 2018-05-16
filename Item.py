import pygame
import classes.classes_tpt as tpt
item = {}

def pomme():
    print(tpt.perso_joueur.vie)
    if tpt.perso_joueur.vie+10<=tpt.perso_joueur.viemax:
        tpt.perso_joueur.vie+=10
        return True
    elif tpt.perso_joueur.vie!=tpt.perso_joueur.viemax:
        tpt.perso_joueur.vie=tpt.perso_joueur.viemax
        return True
    else : return False

def nbsoin():
    if tpt.perso_joueur.vie+50<tpt.perso_joueur.viemax:
        tpt.perso_joueur.vie += 50
        return True
    elif tpt.perso_joueur.vie!=tpt.perso_joueur.viemax:
        tpt.perso_joueur.vie=tpt.perso_joueur.viemax
        return True
    else:
        return False

def nbresurect():
    if tpt.david.vie==0:
        tpt.david.vie=tpt.david.viemax
    elif tpt.sinatra.vie==0:
        tpt.sinatra.vie=tpt.sinatra.viemax

def mana():
    if tpt.perso_joueur.mana+50<=100:
        tpt.perso_joueur.mana+=50
    elif tpt.perso_joueur.mana!=100:
        tpt.perso_joueur.mana=100


item = {}
item["pomme"]=pomme
item["nbsoin"]=nbsoin
item["nbresurect"]=nbresurect
item["mana"]=mana