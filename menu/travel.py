import pygame
from pygame.locals import *
from menu.closemenu import closemenu
from menu.imageinterfacetoload import *


with open("options\\fullscreen", "r") as fullscreen:
    fullscreenread = fullscreen.read()

if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else:
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)

class travel():
    """Classe pour voyager à cheval"""
    def __init__(self):
        self.image = boitevoyage
        self.rect = self.image.get_rect()
        self.rect.x = 255 #position de la fenetre, centré sur l'écran par rapport à ses dimensions
        self.rect.y = 105

    class bouton1():
        def __init__(self):
            self.image = boutonfjordglas
            self.mask = boutonfjordglasmask

    class bouton2():
        def __init__(self):
            self.image = boutonchateau
            self.mask = boutonchateaumask

    class bouton3():
        def __init__(self):
            self.image = boutonvillage
            self.mask = boutonvillagemask

    def interface(self):
        fond=pygame.image.load("menu/inventory/screenshot.jpg").convert()
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    closemenu(fenetre)
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
                if event.type == MOUSEMOTION:
                    testrect.x = event.pos[0]
                    testrect.y = event.pos[1]
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.bouton1().mask.overlap(testmask, (testrect.x - self.rect.x, testrect.y - self.rect.y)):
                            self.voyage("cheminfjord")
                        if self.bouton2().mask.overlap(testmask, (testrect.x - self.rect.x, testrect.y - self.rect.y)):
                            self.voyage("capitale")
                        if self.bouton3().mask.overlap(testmask, (testrect.x - self.rect.x, testrect.y - self.rect.y)):
                            self.voyage("village")
            fenetre.blit(fond, (0,0))
            fenetre.blit(self.image, self.rect)
            fenetre.blit(self.bouton1().image, self.rect)
            fenetre.blit(self.bouton2().image, self.rect)#Affichage
            fenetre.blit(self.bouton3().image, self.rect)
            pygame.display.flip()


    def voyage(self, endroit):
        from maps import selecmap
        with open("save1/map", "w") as maptransi:
            maptransi.write(endroit)
        with open("save1/pospeso/pospesoecurie", "w") as pospeso:
            pospeso.write("")
        with open("save1/posmap/posmapecurie", "w") as posmap:
            posmap.write("")
        if endroit == "capitale":
            with open("save1/posmap/posmapcapitale", "w") as posmap:
                posmap.write("-904,-1620")#On met les coordonnées du chateau dans la capitale
            with open("save1/pospeso/pospesocapitale", "w") as pospeso:
                pospeso.write("395,208")
        selecmap()

