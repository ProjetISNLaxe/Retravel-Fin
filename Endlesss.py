import pygame, sys
from pygame.locals import *
from menu.closemenu import closemenu
from menu.imageinterfacetoload import *
import menu.dialogue
import shooter.shooter_fonction as shooter
import maps
from Runner.Principal import *
with open("options\\fullscreen", "r") as fullscreen:
    fullscreenread = fullscreen.read()

if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else:
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)

class Endless():
    """Classe menu escape"""
    def __init__(self):
        self.image = boitescape
        self.rect = self.image.get_rect()
        self.rect.x = 255 #position de la fenetre, centré sur l'écran par rapport à ses dimensions
        self.rect.y = 105
        fond = pygame.image.save(fenetre, "Endless/fond.jpg")
        save = open("save1/runner", "r")
        self.runnerlock = bool(int(save.read()))
        save.close()
        save = open("save1/save", "r")
        self.RPGlock = bool(int(save.read()))
        save.close()
    class bouton1():
        def __init__(self):
            self.image = boutonshooter
            self.mask = boutonshootermask

    class bouton2():
        def __init__(self):
            save = open("save1\\save", "r")
            RPG = bool(int(save.read()))
            save.close()
            if RPG:
                self.image = boutonRPG
            else: self.image = boutonRPGlock
            self.mask = boutonRPGmask

    class bouton3():
        def __init__(self):
            save = open("save1\\runner", "r")
            runner = bool(int(save.read()))
            save.close()
            if runner:
                self.image = boutonrunner
            else: self.image = boutonrunnerlock
            self.mask = boutonrunnermask

    def interface(self):
        fond=pygame.image.load("Endless/fond.jpg").convert()
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
                            shooter.endless(fenetre)
                        if self.bouton2().mask.overlap(testmask, (testrect.x - self.rect.x, testrect.y - self.rect.y)) and self.RPGlock:
                            maps.selecmap()
                        if self.bouton3().mask.overlap(testmask, (testrect.x - self.rect.x, testrect.y - self.rect.y)):
                            g = Jeu()
                            g.start_screen()
                            while g.running:
                                g.new()
                                g.game_over_screen()

                            pygame.quit()
                            sys.exit()
            fenetre.blit(fond, (0,0))
            fenetre.blit(self.image, self.rect)
            fenetre.blit(self.bouton1().image, self.rect)
            fenetre.blit(self.bouton2().image, self.rect)#Affichage
            fenetre.blit(self.bouton3().image, self.rect)
            pygame.display.flip()





