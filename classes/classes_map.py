import pygame, quete, os
from classes.perso_classes import *
from mapimage import imagemaps
from menu.dialogue import dialogue

from battle.combatV3 import tourpartour


class classmapbasique():
    def __init__(self, nom):
        self.name=nom
        listefi = os.listdir("map/" + self.name)
        if self.name not in imagemaps.map:
            imagemaps.map[self.name]=pygame.image.load("map/"+self.name+"/"+self.name+".png").convert_alpha()
            imagemaps.map[self.name+"_obstacle"]=pygame.image.load("map/"+self.name+"/"+self.name+"_obstacle.png").convert_alpha()
        self.image = imagemaps.map[self.name]
        self.image_obstacle = imagemaps.map[self.name + "_obstacle"]
        self.mask = pygame.mask.from_surface(self.image_obstacle)
        self.size = self.image.get_size()
        self.rect = self.image.get_rect()
        try:
            with open("save1/posmap/posmap" + self.name, "r") as rectf:
                carect = rectf.read()
        except FileNotFoundError:
            with open("save1/posmap/posmap" + self.name, "w") as rectf:
                rectf.write("")
                carect=""
        rectf.close()
        lirect = carect.split(",")
        if carect == "":
            rectf = open("map/" + self.name + "/spawn" + self.name, "r")
            carect = rectf.read().split(";")
            rectf.close()
            lirect = carect[0].split(",")


        self.rect.x = int(lirect[0])
        self.rect.y = int(lirect[1])
        if "transi"+self.name not in imagemaps.map:
            transi = open("map/" + self.name + "/transi" + self.name, "r")
            imagemaps.map["transi"+self.name] = transi.read().split(",")
            transi.close()
            imagemaps.map["transi"+self.name+"image"] = []
            imagemaps.map["transi"+self.name+"mask"] = []
            for i in range(len(imagemaps.map["transi"+self.name])):
                imagemaps.map["transi" + self.name + "image"].append(
                    pygame.image.load("map/" + self.name + "/" + self.name + "_" + imagemaps.map["transi"+self.name][i] + ".png"))
                imagemaps.map["transi" + self.name + "mask"].append(pygame.mask.from_surface(imagemaps.map["transi" + self.name + "image"][i]))
        imagemaps.map["transi"+self.name]=imagemaps.map["transi"+self.name]

        self.affichetext = False
        if ("pnj"+self.name) in listefi:
            self.pnj = True
        else: self.pnj = False
        if self.pnj :
            if "pnj"+self.name not in imagemaps.map:

                pnji = open("map/" + self.name + "/pnj" + self.name, "r")
                imagemaps.map["pnj" + self.name] = pnji.read().split(",")
                pnji.close()
                imagemaps.map["pnj"+self.name+"image"] = []
                imagemaps.map["pnj" + self.name + "mask"] = []
            for i in range(len(imagemaps.map["pnj" + self.name])):
                imagemaps.map["pnj"+self.name+"image"].append(
                    pygame.image.load("map/" + self.name + "/" + self.name + "_" + imagemaps.map["pnj" + self.name][i] + ".png"))
                imagemaps.map["pnj" + self.name + "mask"].append(pygame.mask.from_surface(imagemaps.map["pnj"+self.name+"image"][i]))
        self.myfont = pygame.font.SysFont("monospace", 20)
        self.affichetext2=False
        if ("mob"+self.name) in  listefi:
            self.mob=True
        else : self.mob = False
        if self.mob:
            mobi = open("map/"+self.name+"/mob"+self.name, "r")
            mob = mobi.read()
            mobi.close()
            self.mobli = mob.split(",")
            self.imagemob = []
            self.maskmob = []

            for i in range(len(self.mobli)):
                self.imagemob.append(pygame.image.load("map/"+self.name+"/"+self.name+"_" + self.mobli[i] + ".png"))
                self.maskmob.append(pygame.mask.from_surface(self.imagemob[i]))
        if (self.name+"_dessus.png") in listefi:
            self.plan3 = True
        else: self.plan3 = False
        self.bandeau=pygame.image.load("menu/quetes/HUD/bandeau.png").convert_alpha()
        quetefi = open("menu/quetes/active", "r")
        self.queteactive = quetefi.read()
        self.queteactive = self.queteactive.capitalize()  # Quete active à afficher
        if self.queteactive != "":
            missionfi = open("menu/quetes/" + self.queteactive + "/toprint")
            self.mission = missionfi.read()  # Objectif de la quête
            missionfi.close()

        self.police = pygame.font.SysFont("monospace", 15)
        if self.plan3:
            self.dessus = pygame.image.load("map/"+self.name+"/"+self.name+"_dessus.png").convert_alpha()


        self.iconporte=[pygame.image.load("menu/sprite_0.png").convert_alpha(), pygame.image.load("menu/sprite_1.png").convert_alpha()]
        self.incporte=0

    def interaction(self, perso, fenetre):
        tkey = pygame.key.get_pressed()
        for i in range(len(imagemaps.map["transi"+self.name])):
            if imagemaps.map["transi"+self.name+"mask"][i].overlap(perso.mask, (perso.rect.x - self.rect.x, perso.rect.y - self.rect.y)):
                self.affichetext = True
                break
            else:
                self.affichetext = False
        if self.pnj:
            for i in range(len(imagemaps.map["pnj" + self.name])):
                if imagemaps.map["pnj" + self.name + "mask"][i].overlap(perso.mask, (perso.rect.x - self.rect.x, perso.rect.y - self.rect.y)):
                    self.affichetext2=True
                    if tkey[K_e]:
                            quete.quetes()  # vérifie si il fait partie d'une quête
                            dialogue(imagemaps.map["pnj" + self.name][i])  # lance dialogue pnj
                else:
                    self.affichetext2=False
        if self.mob:
            for i in range (len(self.mobli)):
                if tkey[K_f]:
                    if self.maskmob[i].overlap(perso.mask, (perso.rect.x - self.rect.x, perso.rect.y- self.rect.y)):
                        fichier = open("menu/quetes/mobmort", "w")
                        fichier.write(self.mobli[i])
                        fichier.close()
                        tourpartour()

    def affichage(self, fenetre, perso):
        fenetre.blit(self.image, self.rect)
        if self.pnj:
            for i in range(len(imagemaps.map["pnj" + self.name])):
                fenetre.blit(imagemaps.map["pnj"+self.name+"image"][i], self.rect)
        if self.mob:
            for i in range (len(self.mobli)):
                fenetre.blit(self.imagemob[i], self.rect)
        fenetre.blit(perso.imageperso, perso.rect)
        if self.plan3:
            fenetre.blit(self.dessus, self.rect)
        if self.affichetext:
            self.incporte+=1
            if self.incporte<=30:
                fenetre.blit(self.iconporte[0], (perso.rect.x - 50, perso.rect.y))
            else:
                fenetre.blit(self.iconporte[1], (perso.rect.x -50, perso.rect.y))
        else:
            self.incporte=0
        if self.affichetext2:
            fenetre.blit(self.myfont.render("PRESS F", True, (0,0,0)), (perso.rect.x-75, perso.rect.y))
        fenetre.blit(self.bandeau, (0,0))
        if self.queteactive != "":  # Si il y a une quete, on blit la description
            if self.queteactive != "Jeanma":
                fenetre.blit(self.police.render(self.queteactive + " : " + self.mission, True, (53, 255, 251)), (10, 10))
            else:
                fenetre.blit(self.police.render("Histoire" + " : " + self.mission, True, (53, 255, 251)), (10, 10))

