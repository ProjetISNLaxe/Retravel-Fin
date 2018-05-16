import pygame
from pygame.locals import *
from menu.imageinterfacetoload import *
import menu.closemenu as closemenu

with open("options\\fullscreen", "r") as fullscreen:
    fullscreenread = fullscreen.read()
if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else :
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)

def shop():
    fond = pygame.image.load("menu/inventory/fond.jpg").convert()
    follow = False
    curseurrect.x = 769
    curseurrect.y = 145
    inventairefi = open("map/shop_potion/liste", "r")
    objetinventaireimage = []
    achatstr = inventairefi.read().split(",")
    prixfi = open("map/shop_potion/prix", "r")
    prix = []
    prixstr = prixfi.read().split(",")

    bandeauhaut = pygame.image.load("menu/inventory/bandeaumoney+quete.png").convert_alpha()
    inventairefi.close()
    prixfi.close()
    achat = []
    for i in range(len(achatstr)):
        achat.append([achatstr[i]])
        for j in range(len(achat)):
            fi = open("save1/objet/" + achat[i][0], "r")
            achat[i].append(int(fi.read()))
            fi.close()
    for i in range(len(achat)):
        objetinventaireimage.append(pygame.image.load("menu/inventory/objetinventaire.png").convert_alpha())
        objetinventairerect.append(Rect(287, 160 + 99 * i, 461, 98))
    for i in range(len(prixstr)):
        prix.append([prixstr[i]])

    for i in range(len(achat)):
        achat[i][0] = pygame.image.load("menu/inventory/objets/" + achat[i][0] + ".png").convert_alpha()
    quetefi = open("menu/quetes/active", "r")
    queteactive = quetefi.read()
    queteactive = queteactive.capitalize()
    inventairemask = []
    inventairerect = []
    for i in range(len(achat)):
        inventairemask.append(pygame.mask.from_surface(achat[i][0]))
    quetefi.close()
    if queteactive != "":
        missionfi = open("menu/quetes/" + queteactive + "/toprint")
        mission = missionfi.read()
        missionfi.close()
    orfi = open("save1/invent/cpic", "r")
    tune = orfi.read()

    orfi.close()
    lior = list(tune)
    tune = int(tune)
    while 1:

        for event in pygame.event.get():
            if event.type == QUIT:
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_e or event.key == K_ESCAPE:
                    return
                if event.key == K_DOWN and curseurrect.y < 558:
                    curseurrect.y += 99 / 1.5
                    for i in range(len(objetinventairerect)):
                        objetinventairerect[i][1] -= 98

                if event.key == K_UP and objetinventairerect[0][1] < 160:
                    curseurrect.y -= 98 / 1.5
                    for i in range(len(objetinventairerect)):
                        objetinventairerect[i][1] += 98
            if event.type == MOUSEMOTION:
                testrect.x = event.pos[0]
                testrect.y = event.pos[1]
            if event.type == MOUSEBUTTONDOWN:
                if testmask.overlap(curseurmask, (curseurrect.x - testrect.x, curseurrect.y - testrect.y)):
                    follow = True
                if event.button == 3:
                    if 287 <= testrect.x < 360:
                        for i in range(len(objetinventairerect)):
                            if testrect.colliderect(objetinventairerect[i]) and tune >= int(prix[i][0]):
                                achatfi = open("save1/inventaire", "r")
                                inventairestr = achatfi.read()
                                achatfi.close()
                                tune -= int(prix[i][0])
                                orfi = open("save1/invent/cpic", "w")
                                orfi.write(str(tune))
                                orfi.close()
                                bandeauhaut = pygame.image.load("menu/inventory/bandeaumoney+quete.png").convert_alpha()
                                achat[i][1] += 1
                                fi = open("save1/objet/" + achatstr[i], "w")
                                fi.write(str(achat[i][1]))
                                fi.close()
                                objetinventaireimage[i] = pygame.image.load("menu/inventory/objetinventaire.png").convert_alpha()
                                if achatstr[i] not in inventairestr:
                                    inventairestr+=","+str(achatstr[i])
                                    with open("save1/inventaire", "w") as fichier:
                                        fichier.write(inventairestr)
                if event.button == 5:
                    if 287 <= testrect.x and 160 <= testrect.y and curseurrect.y < 558:
                        curseurrect.y += (99 / 1.5)
                        for i in range(len(objetinventairerect)):
                            objetinventairerect[i][1] -= 98
                if event.button == 4:
                    if 287 <= testrect.x and testrect.y >= 160 > objetinventairerect[0][1]:
                        curseurrect.y -= (98 / 1.5)
                        for i in range(len(objetinventairerect)):
                            objetinventairerect[i][1] += 98

            if event.type == MOUSEBUTTONUP:
                follow = False

        fenetre.blit(fond, (0, 0))
        fenetre.blit(bandeauhaut, (0, 0))
        fenetre.blit(interfaceinvent, (288, 70))
        for i in range(len(achat)):
            if objetinventairerect[i][1] >= 150:
                fenetre.blit(objetinventaireimage[i], objetinventairerect[i])
        if follow:
            if 558 >= curseurrect.y >= 145:
                savecurseur = curseurrect.y
                curseurrect.y = testrect.y
            if 558 > curseurrect.y > 145:
                for i in range(len(objetinventairerect)):
                    objetinventairerect[i][1] += 1.5 * (savecurseur - curseurrect.y)
        if curseurrect.y <= 145:
            for i in range(len(objetinventairerect)):
                objetinventairerect[i][1] = 160 + 99 * i
        if curseurrect.y > 558:
            curseurrect.y = 558
        if curseurrect.y < 145:
            curseurrect.y = 145

        for i in range(len(achat)):
            objetinventaireimage[i].blit(inventaireimage, (0,0))
            objetinventaireimage[i].blit(achat[i][0], (10, 8))
            objetinventaireimage[i].blit(police.render("Quantitée sac : " + str(achat[i][1]), True, (0,0,0)),(195, 10))
            objetinventaireimage[i].blit(police.render("Prix : " + str(prix[i][0]), True, (0,0,0)), (95, 10))

        lior = list(str(tune))
        lior.reverse()
        for i in range(len(lior)):
            bandeauhaut.blit(listechiffre[int(lior[i])], (720 - 22 * i, 5))
        lior.reverse()


        fenetre.blit(curseur, curseurrect)
        pygame.display.flip()
