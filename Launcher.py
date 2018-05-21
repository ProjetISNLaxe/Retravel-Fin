#!/usr/bin/env python
# -*- coding: utf-8 -*-



import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("son/Sound/launcher.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
with open("options\\fullscreen", "r") as fullscreen:
    fullscreenread = fullscreen.read()
if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else :
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)
pygamelogo = pygame.image.load("launcher/pygame_logo.png").convert_alpha()
for i in range (255):
    fenetre.fill((255-i,255-i,255-i))
    fenetre.blit(pygamelogo, (0,0))
    pygame.display.flip()

pygame.display.set_caption("Retravel")
icon = pygame.image.load("logo.png").convert_alpha()
pygame.display.set_icon(icon)
from pygame.locals import *
from shooter.shooter_fonction import *
from maps import *
from pygame import *
from options.option import *
import sys, quete, respawn, escapemenu
from Runner.Principal import *
from Endlesss import Endless
from classes.classes_tpt import *
from mapimage import imagemap


def launcher():
    clock = pygame.time.Clock()
    fond = []
    for i in range(0, 19):
        if i < 10:
            nomimage = "launcher\sprite_menuanimation0" + str(i) + ".png"
        else:
            nomimage = "launcher\sprite_menuanimation" + str(i) + ".png"
        fond.append(pygame.image.load(nomimage).convert())
    nfond = 0
    x = 0
    y = 0
    hardcoremod = pygame.image.load("launcher\hardcore.png").convert_alpha()
    retravel = pygame.image.load("launcher/retravel_logo.png").convert()
    retravels = pygame.Surface((800, 700))
    retravels.blit(retravel, (15,0))
    test = pygame.image.load("launcher\pixelgitan.png").convert_alpha()
    mask = pygame.mask.from_surface(test)
    rect = test.get_rect()
    for i in range (99):
        fenetre.fill((0,0,0))
        fenetre.blit(retravels, (0,0-i))
        pygame.display.flip()
    bouton0 = pygame.image.load("launcher\sprite_boutons0.png").convert_alpha()
    bouton0mask = pygame.mask.from_surface(bouton0)
    bouton1 = pygame.image.load("launcher\sprite_boutons1.png").convert_alpha()
    bouton1mask = pygame.mask.from_surface(bouton1)
    bouton2 = pygame.image.load("launcher\sprite_boutons2.png").convert_alpha()
    bouton2mask = pygame.mask.from_surface(bouton2)
    boutonvierge = pygame.image.load("launcher\sprite_bouton vierge.png").convert_alpha()
    lisere = pygame.image.load("launcher\sprite_boutonliseret.png").convert_alpha()
    clique = 0
    k=0
    save = open("save1\\save", "r")
    passshooter = int(save.read())
    save.close()
    save = open("save1\\runner", "r")
    runner = bool(int(save.read()))
    save.close()

    while 1:

        for event in pygame.event.get():
            if event.type == QUIT:  # pour pouvoir quitter le jeux
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # les deplacements
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == K_h:
                    if combat.hardcore==False:
                        combat.hardcore=True
                    else:
                        combat.hardcore=False
            if event.type == MOUSEMOTION:  # Si mouvement de souris
                x = event.pos[0]
                y = event.pos[1]
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if clique == 1:
                    fenetre.fill((0,0,0))
                    fenetre.blit(retravel, (15, -99))
                    pygame.display.flip()
                    if passshooter == 0:
                        ok = shooter(fenetre)
                        if ok == 1:


                            selecmap()
                    if passshooter == 1 and not runner:
                        selecmap()
                    if runner:
                        g = Jeu()
                        g.start_screen()
                        while g.running:
                            g.new()
                            g.game_over_screen()

                        pygame.quit()
                        sys.exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if clique == 2:
                    pygame.mixer.music.set_volume(1)
                    endle= Endless()
                    endle.interface()
                    save = open("save1\\save", "r")
                    passshooter = int(save.read())
                    save.close()
                    save = open("save1\\runner", "r")
                    runner = bool(int(save.read()))
                    save.close()
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 3:
                    option()
                    save = open("save1\\save", "r")
                    passshooter = int(save.read())
                    save.close()
                    save = open("save1\\runner", "r")
                    runner = bool(int(save.read()))
                    save.close()




        if nfond < 30: 
            fenetre.blit(fond[0], (0, 0))
        elif nfond < 60:
            fenetre.blit(fond[1], (0, 0))
        elif nfond < 90:
            fenetre.blit(fond[2], (0, 0))
        elif nfond < 120:
            fenetre.blit(fond[3], (0, 0))
        elif nfond < 150:
            fenetre.blit(fond[4], (0, 0))
        elif nfond < 180:
            fenetre.blit(fond[5], (0, 0))
        elif nfond < 210:
            fenetre.blit(fond[6], (0, 0))
        elif nfond < 240:
            fenetre.blit(fond[7], (0, 0))
        elif nfond < 270:
            fenetre.blit(fond[8], (0, 0))
        elif nfond < 300:
            fenetre.blit(fond[9], (0, 0))
        elif nfond < 330:
            fenetre.blit(fond[10], (0, 0))
        elif nfond < 360:
            fenetre.blit(fond[11], (0, 0))
        elif nfond < 390:
            fenetre.blit(fond[12], (0, 0))
        elif nfond < 420:
            fenetre.blit(fond[13], (0, 0))
        elif nfond < 450:
            fenetre.blit(fond[14], (0, 0))
        elif nfond < 480:
            fenetre.blit(fond[15], (0, 0))
        elif nfond < 510:
            fenetre.blit(fond[16], (0, 0))
        elif nfond < 540:
            fenetre.blit(fond[17], (0, 0))
        elif nfond < 570:
            fenetre.blit(fond[18], (0, 0))
        if combat.hardcore==True:
            nfond += 2
        nfond += 1
        if nfond > 570:
            nfond = 0
        fenetre.blit(bouton0, (250, 300))
        fenetre.blit(bouton1, (250, 400))
        fenetre.blit(bouton2, (250, 500))
        if combat.hardcore == True:
            fenetre.blit(hardcoremod, (0, 0))

        rect = (x, y)
        offset_x = 250 - x
        offset_y0 = 300 - y
        offset_y1 = 400 - y
        offset_y2 = 500 - y
        if mask.overlap(bouton0mask, (offset_x, offset_y0)):
            fenetre.blit(lisere, (246, 297))
            clique = 1
        elif mask.overlap(bouton1mask, (offset_x, offset_y1)):
            fenetre.blit(lisere, (246, 397))
            clique = 2
        elif mask.overlap(bouton2mask, (offset_x, offset_y2)):
            fenetre.blit(lisere, (246, 497))
            clique = 3
        else:
            clique = 0
        k+=1
        if 255-k>=0:
            retravels.set_alpha(255 - k)
            fenetre.blit(retravels, (0,-99))
        clock.tick(60)
        pygame.display.flip()

launcher()
