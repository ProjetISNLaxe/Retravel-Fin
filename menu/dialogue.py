import pygame, quete, os
from menu.imageinterfacetoload import *
from pygame.locals import *
from random import randint
import menu.closemenu as closemenu
import menu.travel as travel


with open("options\\fullscreen", "r") as fullscreen:
    fullscreenread = fullscreen.read()

if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else:
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)

def dialogue(pnj):
    """Fonction qui permet l'affichage des dialogues pnj perso"""
    listefi = os.listdir("menu/pnj/" + pnj)
    activefich = open("menu/quetes/pnjrencontre", "w")
    activefich.write(pnj)  # On sauvegarde le pnj rencontrés pour les quêtes
    activefich.close()
    pygame.image.save(fenetre, "menu/inventory/screenshot.jpg")  # mini-jeux (phase de test)
    fond = pygame.image.load("menu/inventory/screenshot.jpg").convert()
    clock = pygame.time.Clock()
    dialoguequete = pygame.image.load("menu/quetes/HUD/boitedialogue.png").convert_alpha()
    textefi = open("menu/pnj/" + pnj + "/dialogue", "r")
    textli = textefi.read().split(";")  # On ouvre une liste dans un fichier contenant divers dialogues possibles
    textefi.close()
    if (pnj + "_tall.png") in listefi:
        pnjtall=True
    else: pnjtall = False
    if pnjtall:
        imagepnj = pygame.image.load("menu/pnj/" + pnj + "/" + pnj + "_tall.png").convert_alpha()  # image du pnj à droite
        taillepnj = imagepnj.get_size()
    bouton1v = True if pnj == "palfrenier" else False
    quetedispof = open("menu/quetes/quetedispo", "r")
    quetedispo = quetedispof.read().split(",")  # On ouvre le fichier de sauvegarde contenant les quêtes disponibles
    quetedispof.close()

    if bouton1v:
        bouton1 = pygame.image.load("menu/quetes/HUD/boutonvoyager.png").convert_alpha()

    else : bouton1 = pygame.image.load("menu/quetes/HUD/boutonretour.png").convert_alpha()
    if pnj in quetedispo: # Si le pnj propose une quête on affiche le bouton quête
        bouton2 = pygame.image.load("menu/quetes/HUD/boutonquest.png").convert_alpha()
    else: bouton2 = pygame.image.load("menu/quetes/HUD/boutonretour.png").convert_alpha()#sinon simple retour
    bouton1rect = bouton1.get_rect()
    bouton1rect.x = 100
    bouton1rect.y = 545
    bouton2rect = bouton2.get_rect()

    bouton2rect.x = 420
    bouton2rect.y = 545

    quetefi = open("menu/quetes/active", "r")
    queteactive = quetefi.read()  # Quete active
    if queteactive == "jeanma":
        queteactive="histoire"
    quetefi.close()
    quete.quetes()

    x = 0
    tobreak = False
    text = textli[randint(0, len(textli) - 1)]
    i = 0
    nbrorfi = open("save1/invent/cpic", "r")
    nbror = int(nbrorfi.read())
    nbrorfi.close()
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                closemenu.closemenu()
                fenetre.blit(fond, (0, 0))
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                if event.key == K_UP:
                    return
                if event.key == K_RIGHT:
                    return
                if event.key == K_LEFT:
                    return
                if event.key == K_DOWN:
                    return
            if event.type == MOUSEMOTION:
                if event.type == MOUSEMOTION:
                    testrect.x = event.pos[0]
                    testrect.y = event.pos[1]
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if bouton1v and testrect.colliderect(bouton1rect):
                            voyage = travel.travel()
                            voyage.interface()
                            fenetre.blit(fond, (0,0))
                    elif testrect.colliderect(bouton1rect):
                        return
                    if testrect.colliderect(bouton2rect) and pnj in quetedispo:
                        if pnj == "jeanma":
                            pnj =="histoire"
                        affichquete(pnj)  # boite de dialogue quete
                    elif testrect.colliderect(bouton2rect):
                        return

        tobreak = False  # Pour casser une boucle
        fenetre.blit(dialoguequete, (0, 374))
        dialoguequete = pygame.image.load("menu/quetes/HUD/boitedialogue.png").convert_alpha()
        fenetre.blit(imagepnj, (10, 540 - taillepnj[1])) if pnjtall else None
        if bouton1v or pnj in quetedispo:
            fenetre.blit(bouton2, bouton2rect)
            fenetre.blit(bouton1, bouton1rect)
        if pnj not in quetedispo:
            fenetre.blit(bouton2, bouton2rect)

        if len(text) > 65:  # Si le texte sort du cadre
            affich = []  # liste des lignes à afficher
            k = 0  # increment
            motablit = text.split(" ")  # On crée un liste avec tout les mots
            for i in range(int(len(text) / 65) + 3):

                affich.append("")
                while len(affich[i]) < 65:  # On rajoute des mots
                    if k < len(motablit) - 1:  # sauf si le nombre de caractère sort du cadre
                        if len(affich[i] + motablit[k] + " ") < 65:
                            affich[i] += motablit[k] + " "
                        else:
                            break
                        k += 1
                    else:
                        break
            if motablit[-1] not in affich[-1]:  # Si le dernier mot est décalé on le reblit dans la dernière phrase
                for i in range(len(alphabet)):
                    for j in range(len(affich)):
                        if alphabet[i] not in affich[j]:
                            affich[j] += motablit[-1]
                            tobreak = True
                            break
                    if tobreak:
                        break
            if len(affich) <= 10:  # Si on sort pas du cadre horizontale
                for i in range(len(affich)):  # blit normal
                    dialoguequete.blit(police.render(affich[i], True, (32, 153, 152)), (175, 10 + 15 * i))
            else:  # sinon on crée un curseur

                tkey = pygame.key.get_pressed()
                if tkey[K_UP] and x + 374 + 15 * len(affich) + 25 > 550:

                    x -= 7.5
                    dialoguequete = pygame.image.load("menu/quetes/HUD/boitedialogue.png").convert_alpha()
                elif tkey[K_DOWN] and 384 + x + 10 <= 384:
                    x += 7.5
                    dialoguequete = pygame.image.load("menu/quetes/HUD/boitedialogue.png").convert_alpha()
                for i in range(len(affich)):
                    if x + 384 + 15 * i < 530:
                        dialoguequete.blit(police.render(affich[i], True, (32, 153, 152)), (175, x + 10 + 15 * i))

        if len(text) < 65:
            dialoguequete.blit(police.render(text, True, (32, 153, 152)), (175, 10 + 15 * i))

        clock.tick(60)  # 60 FPS
        pygame.display.flip()


def affichquete(pnj):
    """fonction qui affiche la liste des quêtes en cour"""


    clock = pygame.time.Clock()
    dialoguequete = pygame.image.load("menu/quetes/HUD/boitedialogue.png").convert_alpha()
    pygame.image.save(fenetre, "menu/inventory/screenshot.jpg")  # mini-jeux (phase de test)
    fond = pygame.image.load("menu/inventory/screenshot.jpg").convert()
    textefi = open("menu/quetes/" + pnj + "/objectif", "r")
    text = textefi.read()
    textefi.close()
    quetedispof = open("menu/quetes/quetedispo", "r")
    quetedispo = quetedispof.read().split(",")
    quetedispof.close()
    quetefi = open("menu/quetes/liste", "r")
    queteli = quetefi.read()
    quetefi.close()
    imagepnj = pygame.image.load("menu/pnj/" + pnj + "/" + pnj + "_tall.png").convert_alpha()
    bouton1 = pygame.image.load("menu/quetes/HUD/boutonaccepter.png").convert_alpha()
    bouton2 = pygame.image.load("menu/quetes/HUD/boutonrefuser.png").convert_alpha()
    bouton1rect = bouton1.get_rect()
    bouton2rect = bouton2.get_rect()
    bouton1rect.x = 100
    bouton1rect.y = 545
    bouton2rect.x = 420
    bouton2rect.y = 545

    taillepnj = imagepnj.get_size()
    x = 0
    tobreak = False

    while 1:

        for event in pygame.event.get():
            if event.type == QUIT:
                closemenu.closemenu()
                fenetre.blit(fond, (0, 0))

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                if event.key == K_UP:
                    return
                if event.key == K_RIGHT:
                    return
                if event.key == K_LEFT:
                    return
                if event.key == K_DOWN:
                    return
            if event.type == MOUSEMOTION:
                if event.type == MOUSEMOTION:
                    testrect.x = event.pos[0]
                    testrect.y = event.pos[1]
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if testrect.colliderect(bouton2rect):
                        return
                    if testrect.colliderect(bouton1rect):
                        quetefi = open("menu/quetes/liste", "r")
                        queteli = quetefi.read().split(",")
                        quetefi.close()
                        if pnj not in queteli and pnj in quetedispo:
                            quetefi = open("menu/quetes/liste", "a")
                            quetefi.write("," + pnj)
                            quetefi.close()
                            return

                        if pnj not in queteactive and pnj in queteli:
                            quetefi = open("menu/quetes/active", "w")
                            quetefi.write(pnj)
                            quetefi.close()
                            return

        tobreak = False
        fenetre.blit(dialoguequete, (0, 374))
        dialoguequete = pygame.image.load("menu/quetes/HUD/boitedialogue.png").convert_alpha()
        fenetre.blit(imagepnj, (10, 540 - taillepnj[1]))

        if pnj in queteli and pnj not in queteactive:
            bouton1 = pygame.image.load("menu/quetes/HUD/boutonactiver.png").convert_alpha()
            bouton2 = pygame.image.load("menu/quetes/HUD/boutonretour.png").convert_alpha()
            fenetre.blit(bouton1, bouton1rect)
        if pnj in queteli and pnj in queteactive:
            bouton2 = pygame.image.load("menu/quetes/HUD/boutonretour.png").convert_alpha()
        if pnj in quetedispo and pnj not in queteli:
            bouton1 = pygame.image.load("menu/quetes/HUD/boutonaccepter.png").convert_alpha()
            bouton2 = pygame.image.load("menu/quetes/HUD/boutonrefuser.png").convert_alpha()
            fenetre.blit(bouton1, bouton1rect)
        fenetre.blit(bouton2, bouton2rect)

        if len(text) > 65:

            affich = []
            k = 0
            motablit = text.split(" ")
            for i in range(int(len(text) / 65) + 3):

                affich.append("")
                while len(affich[i]) < 65:
                    if k < len(motablit) - 1:
                        if len(affich[i] + motablit[k] + " ") < 65:
                            affich[i] += motablit[k] + " "
                        else:
                            break
                        k += 1
                    else:
                        break
            if motablit[-1] not in affich[-1]:
                for i in range(len(alphabet)):
                    for j in range(len(affich)):
                        if alphabet[i] not in affich[j]:
                            affich[j] += motablit[-1]
                            tobreak = True
                            break
                    if tobreak:
                        break

            if len(affich) <= 10:
                for i in range(len(affich)):
                    dialoguequete.blit(police.render(affich[i], True, (32, 153, 152)), (175, 10 + 15 * i))
            else:

                tkey = pygame.key.get_pressed()
                if tkey[K_UP] and x + 374 + 15 * len(affich) + 25 > 550:

                    x -= 7.5
                    dialoguequete = pygame.image.load("menu/quetes/HUD/boitedialogue.png").convert_alpha()
                elif tkey[K_DOWN] and 384 + x + 10 <= 384:
                    x += 7.5
                    dialoguequete = pygame.image.load("menu/quetes/HUD/boitedialogue.png").convert_alpha()
                for i in range(len(affich)):
                    if x + 384 + 15 * i < 530:
                        dialoguequete.blit(police.render(affich[i], True, (32, 153, 152)), (175, x + 10 + 15 * i))
        if len(text) < 65:
            dialoguequete.blit(police.render(text, True, (32, 153, 152)), (175, 15))

        clock.tick(60)  # 60 FPS
        pygame.display.flip()

def jeanmadia(message, mode="retour",pnj = "jeanma"):
    """Fonction qui permet l'affichage des dialogues pnj perso"""
    activefich = open("menu/quetes/pnjrencontre", "w")
    activefich.write(pnj)  # On sauvegarde le pnj rencontrés pour les quêtes
    activefich.close()
    pygame.image.save(fenetre, "menu/inventory/screenshot.jpg")  # mini-jeux (phase de test)
    fond = pygame.image.load("menu/inventory/screenshot.jpg").convert()
    clock = pygame.time.Clock()
    dialoguequete = pygame.image.load("menu/quetes/HUD/boitedialogue.png").convert_alpha()
    imagepnj = pygame.image.load("menu/pnj/"+pnj+"/"+pnj+"_tall.png").convert_alpha()  # image du pnj à droite
    if mode == "retour":
        bouton2 = pygame.image.load("menu/quetes/HUD/boutonretour.png").convert_alpha()
    elif mode == "valider":
        bouton2 = pygame.image.load("menu/quetes/HUD/boutonvalider.png").convert_alpha()
    elif mode == "suivant":
        bouton2 = pygame.image.load("menu/quetes/HUD/boutonsuivant.png").convert_alpha()
    bouton2rect = bouton2.get_rect()
    bouton2rect.x = 420
    bouton2rect.y = 545
    taillepnj = imagepnj.get_size()
    x = 0
    tobreak = False
    i = 0
    while 1:

        for event in pygame.event.get():
            if event.type == QUIT:
                closemenu.closemenu()
                fenetre.blit(fond, (0, 0))
            if event.type == MOUSEMOTION:
                if event.type == MOUSEMOTION:
                    testrect.x = event.pos[0]
                    testrect.y = event.pos[1]
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if testrect.colliderect(bouton2rect):
                        return

        fenetre.blit(dialoguequete, (0, 374))
        dialoguequete = pygame.image.load("menu/quetes/HUD/boitedialogue.png").convert_alpha()
        fenetre.blit(imagepnj, (10, 540 - taillepnj[1]))
        fenetre.blit(bouton2, bouton2rect)
        dialoguequete.blit(police.render(message, True, (32, 153, 152)), (175, 10 + 15 * i))

        clock.tick(60)  # 60 FPS
        pygame.display.flip()
