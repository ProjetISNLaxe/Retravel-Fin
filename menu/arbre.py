#!/usr/bin/env python
# -*- coding: utf-8 -*-

import menu.closemenu as closemenu
import pygame
from pygame.locals import *
from shooter.shooter_fonction import *
from classes.perso_classes import *
from map import *
from pygame import *
from options import *
from sys import exit
from menu.imageinterfacetoload import *
from battle.save import *

with open("options\\fullscreen", "r") as fullscreen:
    fullscreenread = fullscreen.read()

if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else:
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)

def arbre_compet():
    bouclier = pygame.image.load("menu/competance/compdef.png").convert_alpha()
    boucliermask = pygame.mask.from_surface(bouclier)
    coeur = pygame.image.load("menu/competance/compvie.png").convert_alpha()
    coeurmask = pygame.mask.from_surface(coeur)
    degat = pygame.image.load("menu/competance/compatk.png").convert_alpha()
    degatmask = pygame.mask.from_surface(degat)
    coeur1 = pygame.image.load("menu/competance/compvie.png").convert_alpha()
    coeurmask1 = pygame.mask.from_surface(coeur1)
    degat1 = pygame.image.load("menu/competance/compatk.png").convert_alpha()
    degatmask1 = pygame.mask.from_surface(degat1)
    coeur2 = pygame.image.load("menu/competance/compvie.png").convert_alpha()
    coeurmask2 = pygame.mask.from_surface(coeur2)
    degat2 = pygame.image.load("menu/competance/compatk.png").convert_alpha()
    degatmask2 = pygame.mask.from_surface(degat2)
    mana = pygame.image.load("menu/competance/compfire.png").convert_alpha()
    manamask = pygame.mask.from_surface(mana)
    poison = pygame.image.load("menu/competance/compdodge.png").convert_alpha()
    poisonmask = pygame.mask.from_surface(poison)
    perso0 = pygame.image.load("menu/competance/teteperso0.png").convert_alpha()
    perso1 = pygame.image.load("menu/competance/teteperso1.png").convert_alpha()
    perso2 = pygame.image.load("menu/competance/teteperso2.png").convert_alpha()

    test = pygame.image.load("launcher/pixelgitan.png").convert_alpha()
    mask = pygame.mask.from_surface(test)
    clock = pygame.time.Clock()
    perso="joueur"
    fond = pygame.image.load("menu/competance/arbrecomp.png").convert_alpha()
    fond2=pygame.image.load("menu/inventory/fond.jpg").convert()
    x=0
    y=0
    with open("save1/activation/perso3", "r") as active:
        sinatra.active = bool(int(active.read()))

    while 1:
        save = open("save1/save", "r")
        save.close()
        for event in pygame.event.get():
            if event.type == QUIT:  # pour pouvoir quitter le jeux
                closemenu.closemenu()
            if event.type == KEYDOWN:  # les deplacements
                if event.key == K_ESCAPE:
                    return
                if event.key == K_TAB:
                    savetpt()
                    return
            if event.type == MOUSEMOTION:  # Si mouvement de souris
                x = event.pos[0]
                y = event.pos[1]
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if clique == 1 and perso_joueur.ptdecompetance>=1:
                    perso_joueur.ptdecompetance -= 1
                    perso_joueur.ptvie += 1
                    perso_joueur.viemax += 20
                    perso_joueur.vie += 20
                if clique == 2 and perso_joueur.ptdecompetance>=3:
                    perso_joueur.ptdecompetance -= 3
                    perso_joueur.ptmana += 1
                    perso_joueur.sortdefeu = True
                if clique == 3 and perso_joueur.ptdecompetance>=1:
                    perso_joueur.ptdecompetance -= 1
                    perso_joueur.ptforce += 1
                if clique == 4 and david.ptdecompetance>=1:
                    david.ptdecompetance -= 1
                    david.ptvie +=1
                    david.viemax += 20
                    david.vie += 20
                if clique == 5 and david.ptdecompetance>=1:
                    david.ptdecompetance -= 1
                    david.ptforce += 1
                if clique == 6 and david.ptdecompetance>=3:
                    david.ptdecompetance -= 3
                    david.ptbouclier += 1
                if clique == 7 and sinatra.active==True and sinatra.ptdecompetance>=1:
                    sinatra.ptdecompetance -= 1
                    sinatra.ptvie += 1
                    sinatra.viemax += 20
                    sinatra.vie += 20
                if clique == 8 and sinatra.active==True and sinatra.ptdecompetance>=3:
                    sinatra.ptdecompetance -= 3
                    sinatra.ptdodge += 1
                if clique == 9 and sinatra.active == True and sinatra.ptdecompetance>=1:
                    sinatra.ptdecompetance -= 1
                    sinatra.ptforce += 1
        fenetre.blit(fond2, (0,0))
        fenetre.blit(fond, (0, 0))
        fenetre.blit(mana, (360, 312))
        fenetre.blit(coeur, (237, 220))
        fenetre.blit(degat, (483, 220))
        fenetre.blit(coeur1, (29, 53))
        fenetre.blit(degat1, (29, 481))
        fenetre.blit(coeur2, (691, 53))
        fenetre.blit(degat2, (691, 481))
        fenetre.blit(bouclier, (243, 437))
        fenetre.blit(poison, (477, 437))
        fenetre.blit(perso1, (95,311))
        fenetre.blit(perso0, (356, 79))
        fenetre.blit(perso2, (617,311))
        fenetre.blit(police.render(str(perso_joueur.ptmana), False, (0, 0, 188)), (360, 297))
        fenetre.blit(police.render(str(perso_joueur.ptvie), False, (0, 0, 188)), (237, 205))
        fenetre.blit(police.render(str(perso_joueur.ptforce), False, (0, 0, 188)), (483, 205))
        fenetre.blit(police.render(str(david.ptbouclier), False, (0, 0, 188)), (243, 422))
        fenetre.blit(police.render(str(david.ptvie), False, (0, 0, 188)), (29, 38))
        fenetre.blit(police.render(str(david.ptforce), False, (0, 0, 188)), (29, 466))
        fenetre.blit(police.render(str(sinatra.ptdodge), False, (0, 0, 188)), (477, 422))
        fenetre.blit(police.render(str(sinatra.ptvie), False, (0, 0, 188)), (691, 38))
        fenetre.blit(police.render(str(sinatra.ptforce), False, (0, 0, 188)), (691, 466))
        lior = list(str(perso_joueur.ptdecompetance))
        lior.reverse()
        for i in range(len(lior)):
            fenetre.blit(listechiffre[int(lior[i])], (400-20*i, 30))
        lior = list(str(david.ptdecompetance))
        lior.reverse()
        for i in range(len(lior)):
            fenetre.blit(listechiffre[int(lior[i])], (80 - 20 * i, 325))
        lior = list(str(sinatra.ptdecompetance))
        lior.reverse()
        for i in range(len(lior)):
            fenetre.blit(listechiffre[int(lior[i])], (730 - 20 * i, 325))

        if mask.overlap(coeurmask, (237-x, 220-y)):
                clique=1
        elif mask.overlap(manamask, (360-x, 312-y)):
                clique = 2
        elif mask.overlap(degatmask, (483-x, 220-y)):
                clique = 3
        elif mask.overlap(coeurmask1, (29-x, 53-y)):
                clique = 4
        elif mask.overlap(degatmask1, (29-x, 481-y)):
                clique = 5
        elif mask.overlap(boucliermask, (243-x, 437-y)):
                clique=6
        elif mask.overlap(coeurmask2, (691-x, 53-y)):
                clique = 7
        elif mask.overlap(poisonmask, (477-x, 437-y)):
                clique = 8
        elif mask.overlap(degatmask2, (691-x, 481-y)):
                clique = 9
        else:
                clique = 0




        clock.tick(60)
        pygame.display.flip()
