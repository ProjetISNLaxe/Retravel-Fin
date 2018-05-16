#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
import options.defkey as defkey
from options.aff import affichetouche
import sys
import quete
from battle.save import resetsauvegarde


def option():
    with open("options/fullscreen", "r") as fullscreen:
        fullscreenread = fullscreen.read()

    if fullscreenread == "0":
        fenetre = pygame.display.set_mode((800, 600))
    else:
        fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)

    clock = pygame.time.Clock()
    fond = []
    for i in range(0, 19):
        if i < 10:
            nomimage = "launcher/sprite_menuanimation0" + str(i) + ".png"
        else:
            nomimage = "launcher/sprite_menuanimation" + str(i) + ".png"
        fond.append(pygame.image.load(nomimage).convert())
    nfond = 0
    x = 0
    y = 0
    fullscreen = open("options/fullscreen", "r")
    fullscreenread = fullscreen.read()
    fullscreen.close()
    test = pygame.image.load("launcher/pixelgitan.png").convert_alpha()
    mask = pygame.mask.from_surface(test)
    testrect = test.get_rect()
    fullscreenimage = pygame.image.load("options/option/FULLSCREEN.png").convert_alpha()
    fullscreenrect = fullscreenimage.get_rect()
    fullscreenrect.x = 180
    fullscreenrect.y = 315
    casecoche = pygame.image.load("options/option/rectangle.png").convert_alpha()
    casecochemask = pygame.mask.from_surface(casecoche)
    casecocherect = casecoche.get_rect()
    casecocherect.x = 363
    casecocherect.y = 318
    casecochex = pygame.image.load("options/option/x.png").convert_alpha()
    casecochexrect = casecochex.get_rect()
    casecochexrect.x = 373
    casecochexrect.y = 318
    bouton1 = pygame.image.load("options/option/KEYS.png").convert_alpha()
    bouton1mask = pygame.mask.from_surface(bouton1)
    bouton1rect = bouton1.get_rect()
    bouton1rect.x = 180
    bouton1rect.y = 377
    bouton2 = pygame.image.load("options/option/RESET.png").convert_alpha()
    bouton2mask = pygame.mask.from_surface(bouton2)
    bouton2rect = bouton2.get_rect()
    bouton2rect.x = 180
    bouton2rect.y = 435
    bouton3 = pygame.image.load("options/RETURN.png").convert_alpha()
    bouton3mask = pygame.mask.from_surface(bouton3)
    bouton3rect = bouton3.get_rect()
    bouton3rect.x = 491
    bouton3rect.y = 481
    clique = 0

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # pour pouvoir quitter le jeux
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # les deplacements
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_BACKSPACE:
                    return
            if event.type == MOUSEMOTION:  # Si mouvement de souris
                x = event.pos[0]
                y = event.pos[1]
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 1:
                    fullscreen = open("options/fullscreen", "w")

                    if fullscreenread == "0":
                        fullscreen.write("1")
                        fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)
                        fullscreen.close()
                        fullscreenread = "1"

                    else:

                        fullscreen.write("0")
                        fenetre = pygame.display.set_mode((800, 600))
                        fullscreen.close()
                        fullscreenread = "0"

            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 2:
                    menukeys()

            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 3:
                    quete.reset()
                    resetsauvegarde()
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 4:
                    return

        fullscreen = open("options/fullscreen", "r")
        fullscreenread = fullscreen.read()
        fullscreen.close()
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
        nfond += 1
        if nfond == 571:
            nfond = 0

        fenetre.blit(fullscreenimage, fullscreenrect)
        fenetre.blit(casecoche, casecocherect)
        fenetre.blit(bouton1, bouton1rect)
        fenetre.blit(bouton2, bouton2rect)
        fenetre.blit(bouton3, bouton3rect)
        if fullscreenread == "1":
            fenetre.blit(casecochex, casecochexrect)
        testrect.x = x
        testrect.y = y
        if mask.overlap(casecochemask, (casecocherect.x - testrect.x, casecocherect.y - testrect.y)):
            clique = 1
        elif mask.overlap(bouton1mask, (bouton1rect.x - testrect.x, bouton1rect.y - testrect.y)):
            clique = 2
        elif mask.overlap(bouton2mask, (bouton2rect.x - testrect.x, bouton2rect.y - testrect.y)):
            clique = 3
        elif mask.overlap(bouton3mask, (bouton3rect.x - testrect.x, bouton3rect.y - testrect.y)):
            clique = 4
        else:
            clique = 0

        clock.tick(60)
        pygame.display.flip()
    return


def menukeys():
    with open("options/fullscreen", "r") as fullscreen:
        fullscreenread = fullscreen.read()

    if fullscreenread == "0":
        fenetre = pygame.display.set_mode((800, 600))
    else:
        fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)

    clock = pygame.time.Clock()
    fond = []
    for i in range(0, 19):
        if i < 10:
            nomimage = "launcher/sprite_menuanimation0" + str(i) + ".png"
        else:
            nomimage = "launcher/sprite_menuanimation" + str(i) + ".png"
        fond.append(pygame.image.load(nomimage).convert())
    nfond = 0
    x = 0
    y = 0
    test = pygame.image.load("launcher/pixelgitan.png").convert_alpha()
    mask = pygame.mask.from_surface(test)
    testrect = test.get_rect()
    shooterimage = pygame.image.load("options/keys/SHOOTER.png").convert_alpha()
    shootermask = pygame.mask.from_surface(shooterimage)
    shooterrect = shooterimage.get_rect()
    shooterrect.x = 180
    shooterrect.y = 315
    rpgimage = pygame.image.load("options/keys/RPG.png").convert_alpha()
    rpgmask = pygame.mask.from_surface(rpgimage)
    rpgrect = rpgimage.get_rect()
    rpgrect.x = 180
    rpgrect.y = 377
    platformerimage = pygame.image.load("options/keys/PLATFORMER.png").convert_alpha()
    platformerrect = platformerimage.get_rect()
    platformermask = pygame.mask.from_surface(platformerimage)
    platformerrect.x = 180
    platformerrect.y = 435
    returnimage = pygame.image.load("options/RETURN.png").convert_alpha()
    returnmask = pygame.mask.from_surface(returnimage)
    returnrect = returnimage.get_rect()
    returnrect.x = 491
    returnrect.y = 481
    clique = 0

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # pour pouvoir quitter le jeux
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # les deplacements
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_BACKSPACE:
                    return
            if event.type == MOUSEMOTION:  # Si mouvement de souris
                x = event.pos[0]
                y = event.pos[1]
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 1:
                    keyshooter()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if clique == 2:
                    0

            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 3:
                    0
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 4:
                    return

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
        nfond += 1
        if nfond == 571:
            nfond = 0

        fenetre.blit(shooterimage, shooterrect)
        fenetre.blit(rpgimage, rpgrect)
        fenetre.blit(platformerimage, platformerrect)
        fenetre.blit(returnimage, returnrect)

        testrect.x = x
        testrect.y = y
        if mask.overlap(shootermask, (shooterrect.x - testrect.x, shooterrect.y - testrect.y)):
            clique = 1
        elif mask.overlap(rpgmask, (rpgrect.x - testrect.x, rpgrect.y - testrect.y)):
            clique = 2
        elif mask.overlap(platformermask, (platformerrect.x - testrect.x, platformerrect.y - testrect.y)):
            clique = 3
        elif mask.overlap(returnmask, (returnrect.x - testrect.x, returnrect.y - testrect.y)):
            clique = 4
        else:
            clique = 0

        clock.tick(60)
        pygame.display.flip()
    return


def keyshooter():
    with open("options/fullscreen", "r") as fullscreen:
        fullscreenread = fullscreen.read()

    if fullscreenread == "0":
        fenetre = pygame.display.set_mode((800, 600))
    else:
        fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)

    clock = pygame.time.Clock()
    fond = []
    for i in range(0, 19):
        if i < 10:
            nomimage = "launcher/sprite_menuanimation0" + str(i) + ".png"
        else:
            nomimage = "launcher/sprite_menuanimation" + str(i) + ".png"
        fond.append(pygame.image.load(nomimage).convert())
    nfond = 0
    x = 0
    y = 0
    test = pygame.image.load("launcher/pixelgitan.png").convert_alpha()
    mask = pygame.mask.from_surface(test)
    testrect = test.get_rect()
    shooterimage = pygame.image.load("options/keys/FORWARD.png").convert_alpha()
    shootermask = pygame.mask.from_surface(shooterimage)
    shooterrect = shooterimage.get_rect()
    shooterrect.x = 180
    shooterrect.y = 315
    rpgimage = pygame.image.load("options/keys/RIGHT.png").convert_alpha()
    rpgmask = pygame.mask.from_surface(rpgimage)
    rpgrect = rpgimage.get_rect()
    rpgrect.x = 180
    rpgrect.y = 377
    platformerimage = pygame.image.load("options/keys/LEFT.png").convert_alpha()
    platformerrect = platformerimage.get_rect()
    platformermask = pygame.mask.from_surface(platformerimage)
    platformerrect.x = 180
    platformerrect.y = 435
    backimage = pygame.image.load("options/keys/BACKWARD.png").convert_alpha()
    backrect = backimage.get_rect()
    backmask = pygame.mask.from_surface(backimage)
    backrect.x = 180
    backrect.y = 493
    shootimage = pygame.image.load("options/keys/SHOOT.png").convert_alpha()
    shootmask = pygame.mask.from_surface(shootimage)
    shootrect = shootimage.get_rect()
    shootrect.x = 491
    shootrect.y = 315
    returnimage = pygame.image.load("options/RETURN.png").convert_alpha()
    returnmask = pygame.mask.from_surface(returnimage)
    returnrect = returnimage.get_rect()
    returnrect.x = 491
    returnrect.y = 481
    clique = 0
    style = pygame.font.SysFont("monospace", 12)
    style2 = pygame.font.SysFont("monospace", 40)
    icoright = affichetouche("rght")
    icoleft = affichetouche("lft")
    icofw = affichetouche("fw")
    icobw = affichetouche("bw")
    icoshoot = affichetouche("shtt")
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # pour pouvoir quitter le jeux
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # les deplacements
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_BACKSPACE:
                    return
            if event.type == MOUSEMOTION:  # Si mouvement de souris
                x = event.pos[0]
                y = event.pos[1]
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 1:
                    nm = defkey.defkey()
                    fichier = open("options/keys/fw", "w")
                    fichier.write(nm)
                    fichier.close()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if clique == 2:
                    nm = defkey.defkey()
                    fichier = open("options/keys/rght", "w")
                    fichier.write(nm)
                    fichier.close()

            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 3:
                    nm = defkey.defkey()
                    fichier = open("options/keys/lft", "w")
                    fichier.write(nm)
                    fichier.close()
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 4:
                    return
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 5:
                    nm = defkey.defkey()
                    fichier = open("options/keys/bw", "w")
                    fichier.write(nm)
                    fichier.close()
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if clique == 6:
                    nm = defkey.defkey()
                    fichier = open("options/keys/shtt", "w")
                    fichier.write(nm)
                    fichier.close()

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
        nfond += 1
        if nfond == 571:
            nfond = 0

        fenetre.blit(shooterimage, shooterrect)
        fenetre.blit(rpgimage, rpgrect)
        fenetre.blit(platformerimage, platformerrect)
        fenetre.blit(backimage, backrect)
        fenetre.blit(shootimage, shootrect)
        fenetre.blit(returnimage, returnrect)
        fenetre.blit(style.render("need to restart the game once the keys have been changed", False, (80, 201, 22)),
                     (167, 283))
        fenetre.blit(style2.render(icobw, False, (80, 201, 22)), (350, 480))
        fenetre.blit(style2.render(icofw, False, (80, 201, 22)), (324, 300))
        fenetre.blit(style2.render(icoright, False, (80, 201, 22)), (300, 360))
        fenetre.blit(style2.render(icoleft, False, (80, 201, 22)), (300, 420))
        fenetre.blit(style2.render(icoshoot, False, (80, 201, 22)), (450, 350))

        testrect.x = x
        testrect.y = y
        if mask.overlap(shootermask, (shooterrect.x - testrect.x, shooterrect.y - testrect.y)):
            clique = 1
        elif mask.overlap(rpgmask, (rpgrect.x - testrect.x, rpgrect.y - testrect.y)):
            clique = 2
        elif mask.overlap(platformermask, (platformerrect.x - testrect.x, platformerrect.y - testrect.y)):
            clique = 3
        elif mask.overlap(returnmask, (returnrect.x - testrect.x, returnrect.y - testrect.y)):
            clique = 4
        elif mask.overlap(backmask, (backrect.x - testrect.x, backrect.y - testrect.y)):
            clique = 5
        elif mask.overlap(shootmask, (shootrect.x - testrect.x, shootrect.y - testrect.y)):
            clique = 6
        else:
            clique = 0
        clock.tick(60)
        pygame.display.flip()
    return
