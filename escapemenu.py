import pygame
from pygame.locals import *
from menu.closemenu import closemenu
from menu.imageinterfacetoload import *
import menu.dialogue as dialogue


with open("options/fullscreen", "r") as fullscreen:
    fullscreenread = fullscreen.read()

if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else:
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)

class escape():
    """Classe menu escape"""
    def __init__(self):
        self.image = boitescape
        self.rect = self.image.get_rect()
        self.rect.x = 255 #position de la fenetre, centré sur l'écran par rapport à ses dimensions
        self.rect.y = 105
        self.fond=pygame.image.save(fenetre, "menu/inventory/fond.jpg")

    class bouton1():
        def __init__(self):
            self.image = boutonmenuprincipal
            self.mask = boutonmenumask

    class bouton2():
        def __init__(self):
            self.image = boutonquitter
            self.mask = boutonquittermask

    class bouton3():
        def __init__(self):
            self.image = boutonaide
            self.mask = boutonaidemask

    def interface(self):
        fond=pygame.image.load("menu/inventory/fond.jpg").convert()
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    closemenu()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
                if event.type == MOUSEMOTION:
                    testrect.x = event.pos[0]
                    testrect.y = event.pos[1]
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.bouton1().mask.overlap(testmask, (testrect.x - self.rect.x, testrect.y - self.rect.y)):
                            from Launcher import launcher
                            launcher()
                        if self.bouton2().mask.overlap(testmask, (testrect.x - self.rect.x, testrect.y - self.rect.y)):
                            closemenu()
                        if self.bouton3().mask.overlap(testmask, (testrect.x - self.rect.x, testrect.y - self.rect.y)):
                            toreturn= aide().interface()
                            if toreturn == "return":
                                return
            fenetre.blit(fond, (0,0))
            fenetre.blit(self.image, self.rect)
            fenetre.blit(self.bouton1().image, self.rect)
            fenetre.blit(self.bouton2().image, self.rect)#Affichage
            fenetre.blit(self.bouton3().image, self.rect)
            pygame.display.flip()


class aide():
    """Classe menu escape aide"""

    def __init__(self):
        self.image = boitescape
        self.rect = self.image.get_rect()
        self.rect.x = 255  # position de la fenetre, centré sur l'écran par rapport à ses dimensions
        self.rect.y = 105

    class bouton1():
        def __init__(self):
            self.image = boutontutoriel
            self.mask = boutontutorielmask

    class bouton2():
        def __init__(self):
            self.image = boutonquete
            self.mask = boutonquetemask

    class bouton3():
        def __init__(self):
            self.image = boutonunstuck
            self.mask = boutonunstuckmask

    def interface(self):
        fond = pygame.image.load("menu/inventory/fond.jpg").convert()
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    closemenu()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
                if event.type == MOUSEMOTION:
                    testrect.x = event.pos[0]
                    testrect.y = event.pos[1]
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.bouton1().mask.overlap(testmask, (testrect.x - self.rect.x, testrect.y - self.rect.y)):
                            self.tutoriel()
                        if self.bouton2().mask.overlap(testmask, (testrect.x - self.rect.x, testrect.y - self.rect.y)):
                            quetefi = open("menu/quetes/active", "r")
                            pnj = quetefi.read()
                            quetefi.close()
                            dialogue.affichquete(pnj)
                        if self.bouton3().mask.overlap(testmask, (testrect.x - self.rect.x, testrect.y - self.rect.y)):
                            self.unstuck()
                            return "return"
            fenetre.blit(fond, (0, 0))
            fenetre.blit(self.image, self.rect)
            fenetre.blit(self.bouton1().image, self.rect)
            fenetre.blit(self.bouton2().image, self.rect)  # Affichage
            fenetre.blit(self.bouton3().image, self.rect)
            pygame.display.flip()
    def tutoriel(self):
        dialogue.jeanmadia("Appuie sur I pour ouvrir l'inventaire", "valider", "aide")
        dialogue.jeanmadia("Dans l'inventaire appui sur Tab pour l'arbre de compétance", "valider", "aide")
        dialogue.jeanmadia("Quand tu croise un pnj, appuie sur F pour interagir", "valider", "aide")
        dialogue.jeanmadia("Appuie sur E sur une porte ouverte pour y rentrer", "valider", "aide")
        dialogue.jeanmadia("Tu peux aller à l'écurie pour voyager vers des contrées lointaines", "valider", "aide")
        dialogue.jeanmadia("Tu peux aller à la boutique de potion si tu n'en a plus", "valider", "aide")

    def unstuck(self):
        with open("save1/map") as map:
            map=map.read()
        with open("map/"+map+"/spawn"+map, "r") as spawn:
            spawn=spawn.read()
        spawn=spawn.split(";")
        spawnmap=spawn[0].split(",")
        spawnpeso = spawn[1].split(",")
        with open("save1/posmap/posmap"+map, "w") as posmap:
            posmap.write(str(spawnmap[0])+","+str(spawnmap[1]))
        with open("save1/pospeso/pospeso"+map, "w") as pospeso:
            pospeso.write(str(spawnpeso[0])+","+str(spawnpeso[1]))





