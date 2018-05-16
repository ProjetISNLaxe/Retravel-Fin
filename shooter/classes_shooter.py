#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from random import randrange
from math import cos
import time
from shooter.constantes import *


class personnage(pygame.sprite.Sprite):
    def __init__(self, fenetre_taille, nbrVie=VIE_PERSO):
        super().__init__()
        self.image = pygame.image.load("shooter\\perso\\N-Ship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.size = self.image.get_size()
        self.vie = nbrVie
        self.incollision = False
        self.rect = Rect(fenetre_taille[0] / 2 - self.size[0] / 2, fenetre_taille[1] - self.size[1], self.size[0],
                         self.size[1])  # Position initiale du Perso
        self.nbrTir = 0
        self.tiry = []
        self.tirx = []
        self.surchauffe = 0
        self.timea = time.time()
        self.surchauffemax = 50
        self.temptir = 0.4
        self.maxtir = 70
        self.inexplosion = False
        self.explosionim = []
        self.persodeath = []
        self.persodeathsize = []

        for i in range(9):
            explosionnom = "shooter\\explosion\\regularExplosion0" + str(i) + ".png"
            self.explosionim.append(pygame.image.load(explosionnom).convert_alpha())
        for i in range(3):
            anim = "shooter\\perso\\brokennship" + str(i + 1) + ".png"
            self.persodeath.append(pygame.image.load(anim).convert_alpha())
            self.persodeathsize.append(self.persodeath[i].get_size())

        self.persodeathrect0 = self.persodeath[0].get_rect()
        self.persodeathrect1 = self.persodeath[1].get_rect()
        self.persodeathrect2 = self.persodeath[2].get_rect()
        self.persodeathrect0 = Rect(self.rect.x / 2, self.rect.y, self.persodeathsize[0][0], self.persodeathsize[0][1])
        self.persodeathrect1 = Rect(self.rect.x, self.rect.y, self.persodeathsize[1][0], self.persodeathsize[1][1])
        self.persodeathrect2 = Rect(self.rect.x / 3, self.rect.y, self.persodeathsize[2][0], self.persodeathsize[2][1])
        self.explosion = self.explosionim[0]
        self.explosion_rect = self.explosion.get_rect
        self.explosionact = False
        self.p = 0
        self.inc = 0
        self.test = False
        self.test1 = True
        self.immortel = False
        self.shootsound = pygame.mixer.Sound("son/Sound/shoot.ogg")
        self.shootsound.set_volume(0.2)
        self.boom = pygame.mixer.Sound("son/Sound/boom.ogg")
        self.boom.set_volume(0.3)

    def moveTop(self):
        if self.rect.y > 0:  # Si on est dans l'écran.
            self.rect.y -= VITESSE_PERSO  # Vitesse définie dans Constantes

    def moveRight(self):
        if self.rect.x < 700:
            self.rect.x += VITESSE_PERSO

    def moveLeft(self):
        if self.rect.x > 0:
            self.rect.x -= VITESSE_PERSO

    def moveDown(self):
        if self.rect.y <= 500:
            self.rect.y += VITESSE_PERSO

    def eventkey(self):
        tkey = pygame.key.get_pressed()
        if tkey[HAUT]:  # Touche définie par le joueur
            if tkey[TIR]:  # Touche de Tir
                self.shoot()  # Fonction de Tir
                self.moveTop()  # Fonction de déplacements
            else:
                self.moveTop()
        if tkey[BAS]:
            if tkey[TIR]:
                self.shoot()
                self.moveDown()
            else:
                self.moveDown()
        if tkey[GAUCHE]:
            if tkey[TIR]:
                self.shoot()
                self.moveLeft()
            else:
                self.moveLeft()
        if tkey[DROITE]:
            if tkey[K_SPACE]:
                self.shoot()
                self.moveRight()
            else:
                self.moveRight()
        if tkey[TIR] and self.vie > 0:
            self.shoot()

    def shoot(self):
        if self.surchauffe < 1000 and time.time() - self.timea > self.temptir:
            self.shootsound.play()
            self.timea = time.time()
            self.surchauffe += self.surchauffemax  # On incremente la surchauffe
            self.nbrTir += 1  # On incremente le nombre de tir
            if self.nbrTir % 2 == 0:  # Si le nombre de chiffre est paire on le fait tirer du canon gauche
                self.tirx.append(self.rect.x + 38)
                self.tiry.append(self.rect.y + 20)
            else:  # Si le nombre de chiffre est impaire on le fait tirer du canon droite
                self.tirx.append(self.rect.x + 47)
                self.tiry.append(self.rect.y + 20)
        if self.nbrTir == self.maxtir:
            self.tirx = []
            self.tiry = []
            self.nbrTir = 0
            self.nbrTir += 1
            self.tirx.append(self.rect.x + 47)
            self.tiry.append(self.rect.y + 20)

    def explosionanim(self):  # animation de l'explosion
        if self.inexplosion:
            self.test = True
            self.boom.play()
            self.inexplosion = False
        if self.test:
            self.explosionact = True
        if self.explosionact:
            self.p += 1
            if 1 < self.p < 5:
                self.explosion = self.explosionim[0]
            elif 5 < self.p < 10:
                self.explosion = self.explosionim[1]
            elif 10 < self.p < 15:
                self.explosion = self.explosionim[2]
            elif 15 < self.p < 20:
                self.explosion = self.explosionim[3]
            elif 20 < self.p < 25:
                self.explosion = self.explosionim[4]
            elif 25 < self.p < 30:
                self.explosion = self.explosionim[5]
            elif 30 < self.p < 35:
                self.explosion = self.explosionim[6]
            elif 35 < self.p < 40:
                self.explosion = self.explosionim[7]
            elif 40 < self.p < 45:
                self.explosion = self.explosionim[8]
            elif self.p == 45:
                self.p = 0
                self.explosionact = False
                self.test = False

    def inideath(self):
        if self.test1:
            self.persodeathrect0 = Rect(self.rect.x, self.rect.y, self.persodeathsize[0][0], self.persodeathsize[0][1])
            self.persodeathrect1 = Rect(self.rect.x, self.rect.y, self.persodeathsize[1][0], self.persodeathsize[1][1])
            self.persodeathrect2 = Rect(self.rect.x, self.rect.y, self.persodeathsize[2][0], self.persodeathsize[2][1])
            self.test1 = False

    def death(self):
        self.inc += 1
        if self.inc < 50:
            self.persodeathrect0.x += 1.5
            self.persodeathrect1.x -= 1.5
            self.persodeathrect2.x += 0.25
            self.persodeathrect0.y += 1
            self.persodeathrect1.y += 0.5
            self.persodeathrect2.y -= 1.5
        elif self.inc > 50:
            self.persodeathrect0.x += 1.5
            self.persodeathrect1.x -= 0.75
            self.persodeathrect2.x += 0.125
            self.persodeathrect0.y += 1
            self.persodeathrect1.y += 0.25
            self.persodeathrect2.y -= 0.75
        if self.inc == 100:
            self.vie -= 1


class ennemi(pygame.sprite.Sprite):
    def __init__(self, imageennemi):
        super().__init__()
        self.image = pygame.image.load(imageennemi).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.size = self.image.get_size()
        self.incollision = False
        self.alive = False
        self.boom = pygame.mixer.Sound("son/Sound/boom.ogg")
        self.boom.set_volume(0.3)

    def respawn(self):
        d = randrange(40, 500)  # On fais  l'ennemi a une coordonnee aleatoire sur x
        self.rect = Rect(d, -self.rect.y - 200, self.size[0], self.size[1])


class ennemi1(ennemi):
    """Classe du premier ennemi"""

    def __init__(self, fenetre_taille):
        ennemi.__init__(self, "shooter\\ennemi\ennemi_1.png")
        self.rect.x = fenetre_taille[0] / 2 - self.size[0] / 2  # Position initiale du Premier ennemi
        self.alive == True
        self.inexplosion = False
        self.explosionim = []
        for i in range(9):
            # On charge l'annimation de l'explosion
            explosionnom = "shooter\\explosion\\regularExplosion0" + str(i) + ".png"
            self.explosionim.append(pygame.image.load(explosionnom).convert_alpha())
        self.explosion = self.explosionim[0]
        self.explosion_rect = self.explosion.get_rect()
        self.explosionact = False
        self.p = 0
        self.test = False
        self.speed = VITESSE_ENNEMI_1

    def move(self, score):
        if self.rect.y < 600 and self.alive == True and score <= ENNEMI_1_ZIGZAG:  # Si l'ennemi est dans l' et que le score est   20 on le deplace normalement
            self.rect.y += self.speed

        elif self.rect.y < 600 and self.alive == True and score > ENNEMI_1_ZIGZAG:  # Si l'ennemi est dans l' et que le score est   20 on le deplace en zigzag
            self.rect.y += self.speed
            self.rect.x += (5 * cos(self.rect.y / 20))

        elif self.alive:  # Si l'ennemi est en dessous de l'ecrans on le respawn en haut
            self.rect = Rect(randrange(40, 500), -self.size[1] - 200, self.size[0], self.size[1])

    def collision(self, perso):
        if pygame.sprite.collide_mask(self, perso):
            self.incollision = True

    def explosionanim(self):
        if self.inexplosion:
            self.test = True
            self.boom.play()
            self.inexplosion = False
        if self.test:
            self.explosionact = True
        if self.explosionact:
            self.p += 1
            if 1 < self.p < 5:
                self.explosion = self.explosionim[0]
            elif 5 < self.p < 10:
                self.explosion = self.explosionim[1]
            elif 10 < self.p < 15:
                self.explosion = self.explosionim[2]
            elif 15 < self.p < 20:
                self.explosion = self.explosionim[3]
            elif 20 < self.p < 25:
                self.explosion = self.explosionim[4]
            elif 25 < self.p < 30:
                self.explosion = self.explosionim[5]
            elif 30 < self.p < 35:
                self.explosion = self.explosionim[6]
            elif 35 < self.p < 40:
                self.explosion = self.explosionim[7]
            elif 40 < self.p < 45:
                self.explosion = self.explosionim[8]
            elif self.p == 45:
                self.p = 0
                self.explosionact = False
                self.test = False


class ennemi2(ennemi):
    def __init__(self, fenetre_taille):
        ennemi.__init__(self, "shooter\\ennemi\ennemi_2.png")
        self.alive = False
        self.rect = Rect(75, -self.size[1], self.size[0], self.size[1])  # Position initiale du deuxieme ennemi
        self.tir_ok = False
        self.speed_tir = 50
        self.nbrTir = 0
        self.tiry = []
        self.tirx = []
        self.inexplosion = False
        self.explosionim = []
        for i in range(9):
            explosionnom = "shooter\\explosion\\regularExplosion0" + str(i) + ".png"
            self.explosionim.append(pygame.image.load(explosionnom).convert_alpha())
        self.explosion = self.explosionim[0]
        self.explosion_rect = self.explosion.get_rect
        self.explosionact = False
        self.p = 0
        self.test = False
        self.speed_y = VITESSE_ENNEMI_2_Y
        self.speed_x = VITESSE_ENNEMI_2_X
        self.shootsound = pygame.mixer.Sound("son/Sound/shootenemy2.ogg")
        self.shootsound.set_volume(0.2)

    def move(self, score):
        if self.rect.y <= 100 and self.alive == True:  # Si l'ennemi 2 n'a pas atteint y=100 on le fait avancer
            self.rect.y += self.speed_y

        elif self.rect.y >= 100 and self.alive == True:  # Si l'ennemi 2 a atteint y=100 on le fait avancer sur x
            if self.rect.x > 800:  # Si l'ennemi est au bord on le respawn de l'autre
                self.rect.x -= 800 + self.size[0]
            else:  # Si l'ennemi 2 a atteint y=100 et n'est pas au bord on le fait avancer sur x
                self.rect.x += self.speed_x

    def collision(self, perso):
        if pygame.sprite.collide_mask(self, perso):
            self.incollision = True

    def shoot(self, increment):
        if self.rect.y >= 101:  # Si le score est  a 50 l'ennemi tir tout les 50 tours de boucles
            if (increment % self.speed_tir) == 0:
                self.tir_ok = True
                self.shootsound.play()
                self.nbrTir += 1  # on  le nombre de tir ennemi
                if self.nbrTir % 2 == 0:  # Si le nombre de chiffre est paire on le fait tirer du canon droit
                    self.tirx.append(self.rect.x + 38)
                    self.tiry.append(self.rect.y + 20)
                else:  # Si le nombre de chiffre est impaire on le fait tirer du canon gauche
                    self.tirx.append(self.rect.x + 47)
                    self.tiry.append(self.rect.y + 20)
                if self.nbrTir == 15:
                    self.tirx = []
                    self.tiry = []
                    self.nbrTir = 0

    def explosionanim(self):
        if self.inexplosion:
            self.test = True
            self.boom.play()
            self.inexplosion = False
        if self.test:
            self.explosionact = True
        if self.explosionact:
            self.p += 1
            if 1 < self.p < 5:
                self.explosion = self.explosionim[0]
            elif 5 < self.p < 10:
                self.explosion = self.explosionim[1]
            elif 10 < self.p < 15:
                self.explosion = self.explosionim[2]
            elif 15 < self.p < 20:
                self.explosion = self.explosionim[3]
            elif 20 < self.p < 25:
                self.explosion = self.explosionim[4]
            elif 25 < self.p < 30:
                self.explosion = self.explosionim[5]
            elif 30 < self.p < 35:
                self.explosion = self.explosionim[6]
            elif 35 < self.p < 40:
                self.explosion = self.explosionim[7]
            elif 40 < self.p < 45:
                self.explosion = self.explosionim[8]
            elif self.p == 45:
                self.p = 0
                self.explosionact = False
                self.test = False


class imfond(pygame.sprite.Sprite):
    def __init__(self, fenetre_taille, *groups):
        super().__init__(*groups)
        self.image1 = pygame.image.load("shooter\\HUD\space.png").convert()
        self.image2 = pygame.image.load("shooter\\HUD\space.png").convert()
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect1.y = -3000
        self.rect2.y = -3000
        self.size1 = self.image1.get_size()
        self.size2 = self.image2.get_size()
        self.deplacement1 = True
        self.deplacement2 = False
        self.nombreavancement = 0
        self.nombreavancement2 = 0

    def deplacement(self):
        if self.deplacement1:
            self.rect1.y += VITESSE_FOND
            self.nombreavancement += VITESSE_FOND
            if self.nombreavancement == 3000:
                self.rect1.y -= 3000
                self.deplacement2 = True
                self.deplacement1 = False
                self.nombreavancement = 0
        if self.deplacement2:
            self.rect2.y += VITESSE_FOND
            self.nombreavancement2 += VITESSE_FOND
            if self.nombreavancement2 == 3000:
                self.rect2.y -= 3000
                self.deplacement2 = False
                self.deplacement1 = True
                self.nombreavancement2 = 0


class clminiboss(pygame.sprite.Sprite):
    def __init__(self, fenetre_taille):
        super().__init__()
        self.image = pygame.image.load("shooter\\ennemi\miniboss\mini_boss.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()
        self.rect.x += fenetre_taille[0] / 2 - self.size[0] / 2
        self.rect.y -= self.size[1] - 50
        self.mask = pygame.mask.from_surface(self.image)
        self.attaque1_movevert = False
        self.attaque1_moveinvert = False
        self.ptVie = 20
        self.canonPtVie = 20
        self.alive = True
        self.test = True
        self.test1 = True
        self.test2 = True
        self.test3 = True
        self.test4 = True
        self.rafale = False
        self.energiebowl = False
        self.energiebowl1 = False
        self.speed_tir = 10
        self.tir_ok = False
        self.tirx = []
        self.tiry = []
        self.nbrTir = 0
        self.imgcanon = pygame.image.load("shooter\\ennemi\miniboss\miniboss_ailes.png").convert_alpha()
        self.imgcanoncasse = pygame.image.load("shooter\\ennemi\miniboss\Boss wings broken.png").convert_alpha()
        self.maskcanon = pygame.mask.from_surface(self.imgcanon)
        self.maskcanoncasse = pygame.mask.from_surface(self.imgcanoncasse)
        self.rectcanon = self.imgcanon.get_rect()
        self.sizecanon = self.imgcanon.get_size()
        self.rectcanon = Rect(fenetre_taille[0] / 2 - 199, self.rect.y + 49, self.sizecanon[0], self.sizecanon[1])
        self.canonalive = True
        self.bouleimageli = []
        self.boulerectli = []
        self.boulesizeli = []
        self.boulemaskli = []
        self.persoinzone = False
        for k in range(3):
            bouleimage = "shooter\\ennemi\\miniboss\\sprite_energyball" + str(k) + ".png"
            self.bouleimageli.append(pygame.image.load(bouleimage).convert_alpha())
            self.boulerectli.append(self.bouleimageli[k].get_rect())
            self.boulesizeli.append(self.bouleimageli[k].get_size())
            self.boulerectli[k] = Rect(250, 110, self.boulesizeli[k][0], self.boulesizeli[k][1])
            self.boulemaskli.append(pygame.mask.from_surface(self.bouleimageli[k]))

        self.bouleimage = self.bouleimageli[0]
        self.boulerect = self.boulerectli[0]
        self.boulemask = self.boulemaskli[0]
        self.increment_boule = 0

        self.bouleload = False
        self.bouleattak = False
        self.boulemovex = 0
        self.boulemovey = 0

        self.bouleimageli1 = []
        self.boulerectli1 = []
        self.boulesizeli1 = []
        self.boulemaskli1 = []
        self.persoinzone1 = False
        self.bouleimageli2 = []
        self.boulerectli2 = []
        self.boulesizeli2 = []
        self.boulemaskli2 = []
        for m in range(3):
            bouleimage = "shooter\\ennemi\\miniboss\\sprite_energyball" + str(m) + ".png"
            self.bouleimageli1.append(pygame.image.load(bouleimage).convert_alpha())
            self.boulerectli1.append(self.bouleimageli1[m].get_rect())
            self.boulesizeli1.append(self.bouleimageli1[m].get_size())
            self.boulerectli1[m] = Rect(515, 110, self.boulesizeli1[m][0], self.boulesizeli1[m][1])
            self.boulemaskli1.append(pygame.mask.from_surface(self.bouleimageli1[m]))
        for m in range(3):
            bouleimage = "shooter\\ennemi\\miniboss\\sprite_energyball" + str(m) + ".png"
            self.bouleimageli2.append(pygame.image.load(bouleimage).convert_alpha())
            self.boulerectli2.append(self.bouleimageli2[m].get_rect())
            self.boulesizeli2.append(self.bouleimageli2[m].get_size())
            self.boulerectli2[m] = Rect(400 - self.boulesizeli2[m][0], 50, self.boulesizeli2[m][0],
                                        self.boulesizeli2[m][1])
            self.boulemaskli2.append(pygame.mask.from_surface(self.bouleimageli2[m]))

        self.bouleimage1 = self.bouleimageli1[0]
        self.boulerect1 = self.boulerectli1[0]
        self.boulemask1 = self.boulemaskli1[0]
        self.increment_boule1 = 0
        self.bouleimage2 = self.bouleimageli2[0]
        self.boulerect2 = self.boulerectli2[0]
        self.boulemask2 = self.boulemaskli2[0]
        self.increment_boule2 = 0

        self.bouleload1 = False
        self.bouleattak1 = False
        self.boulemove1x = 0
        self.boulemove1y = 0

        self.bouleload2 = False
        self.bouleattak2 = False
        self.boulemove2x = 0
        self.boulemove2y = 0

        self.unlimitedpoweer = False
        # Eclairimage
        self.eclairimageli = []
        self.eclairrectli = []
        self.eclairsizeli = []
        self.eclairmaskli = []
        for i in range(5):
            eclairnom = "shooter\\ennemi\\miniboss\\eclair\\eclair_" + str(i + 1) + ".png"
            self.eclairimageli.append(pygame.image.load(eclairnom).convert_alpha())
            self.eclairrectli.append(self.eclairimageli[i].get_rect())
            self.eclairsizeli.append(self.eclairimageli[i].get_size())
            self.eclairrectli[i] = Rect(253, 180, self.eclairsizeli[i][0], self.eclairsizeli[i][1])
            self.eclairmaskli.append(pygame.mask.from_surface(self.eclairimageli[i]))

        self.increment_eclair = 0
        self.eclairimage = self.eclairimageli[0]
        self.eclairrect = self.eclairrectli[0]
        self.eclairmask = self.eclairmaskli[0]

        self.timea = time.time()
        # LASERRRRR
        self.laserimage = pygame.image.load("shooter\\ennemi\miniboss\Boss_lazor2.png").convert_alpha()
        self.laserrect = self.laserimage.get_rect()
        self.lasermask = pygame.mask.from_surface(self.laserimage)
        self.laser = False
        self.laserload = False
        self.laserattak = False
        self.laserdep = False
        self.test5 = True
        self.laseer = False
        self.timeb = time.time()
        self.timec = 0
        self.energiebowlsound = pygame.mixer.Sound("son/Sound/energyball.ogg")
        self.energiebowlsound.set_volume(0.3)
        self.shootsound = pygame.mixer.Sound("son/Sound/shootenemy2.ogg")
        self.shootsound.set_volume(0.1)
        self.arcele = pygame.mixer.Sound("son/Sound/electrik.wav")
        self.arcele.set_volume(0.1)

    def perdvie(self):
        self.ptVie -= 10

    def attaque1(self, score):
        if score == SCORE_MINIBOSS + 5 and self.test == True:
            self.attaque1_movevert = True
            self.test = False
            self.unlimitedpoweer = False
        if self.attaque1_movevert:
            self.rect.y += 10
            self.rectcanon.y += 10
            if self.rect.y >= 600:
                self.attaque1_movevert = False
                self.attaque1_moveinvert = True
        if self.attaque1_moveinvert:
            if self.rectcanon.y >= 49:
                self.rectcanon.y -= 2.5
            self.rect.y -= 2.5
            if self.rect.y <= -25:
                self.attaque1_moveinvert = False
                self.unlimitedpoweer = True
                self.rectcanon = Rect(400 - 199, 49, self.sizecanon[0], self.sizecanon[1])

    def attaque2(self, score, increment):
        if score >= SCORE_MINIBOSS and self.attaque1_moveinvert == False and self.attaque1_movevert == False and self.test1 == True:
            self.rafale = True
            self.test1 = False
        if self.rafale:
            if (increment % self.speed_tir) == 0:
                self.shootsound.play()
                self.tir_ok = True
                self.nbrTir += 1  # On  le nombre de tir ennemi
                if self.nbrTir % 2 == 0:  # Si le nombre de chiffre est paire on le fait tirer du canon droit
                    self.tirx.append(self.rect.x + 268)
                    self.tiry.append(self.rect.y + 235)
                else:  # Si le nombre de chiffre est impaire on le fait tirer du canon gauche
                    self.tirx.append(self.rect.x + 176)
                    self.tiry.append(self.rect.y + 235)
        if self.nbrTir == 15:
            self.rafale = False

        if time.time() - self.timea > 5 and self.laseer == False:
            self.test1 = True
            self.tirx = []
            self.tiry = []
            self.nbrTir = 0
            self.timea = time.time()

    def attaque3(self, score):
        if self.test2 == True and score >= SCORE_MINIBOSS:
            self.unlimitedpoweer = True
            self.test2 = False
        if self.unlimitedpoweer == True and self.canonalive == True:
            self.increment_eclair += 2.5
            self.arcele.play()
            if self.increment_eclair <= 10:
                self.eclairimage = self.eclairimageli[0]
                self.eclairrect = self.eclairrectli[0]
                self.eclairmask = self.eclairmaskli[0]
            if 20 >= self.increment_eclair > 10:
                self.eclairimage = self.eclairimageli[1]
                self.eclairrect = self.eclairrectli[1]
                self.eclairmask = self.eclairmaskli[1]
            if 30 >= self.increment_eclair > 20:
                self.eclairimage = self.eclairimageli[2]
                self.eclairrect = self.eclairrectli[2]
                self.eclairmask = self.eclairmaskli[2]
            if 40 >= self.increment_eclair > 30:
                self.eclairimage = self.eclairimageli[3]
                self.eclairrect = self.eclairrectli[3]
                self.eclairmask = self.eclairmaskli[3]
            if 50 >= self.increment_eclair > 40:
                self.eclairimage = self.eclairimageli[4]
                self.eclairrect = self.eclairrectli[4]
                self.eclairmask = self.eclairmaskli[4]
                if self.increment_eclair == 50:
                    self.increment_eclair = 0

    def attaque4(self, score, increment):
        if score >= SCORE_MINIBOSS + 5 and not self.attaque1_moveinvert and not self.attaque1_movevert and self.test3:
            self.energiebowl = True
            self.energiebowlsound.play()
            self.test3 = False
        if self.energiebowl:
            self.bouleload = True
        if self.bouleload:
            self.increment_boule += 1
            if self.increment_boule < 20:
                self.bouleimage = self.bouleimageli[0]
                self.boulerect = self.boulerectli[0]
                self.boulemask = self.boulemaskli[0]
            if 20 < self.increment_boule < 40:
                self.bouleimage = self.bouleimageli[1]
                self.boulerect = self.boulerectli[1]
                self.boulemask = self.boulemaskli[1]
            if 40 < self.increment_boule < 60:
                self.bouleimage = self.bouleimageli[1]
                self.boulerect = self.boulerectli[1]
                self.boulemask = self.boulemaskli[1]
            if self.increment_boule >= 80:
                self.bouleimage = self.bouleimageli[0]
                self.boulerect = self.boulerectli[0]
                self.boulemask = self.boulemaskli[0]
                if self.persoinzone == True and self.attaque1_moveinvert == False and self.attaque1_movevert == False:
                    self.bouleattak = True
                    self.bouleload = False
        if self.bouleattak:
            self.boulerect.y += self.boulemovey
            self.boulerect.x += self.boulemovex
            if self.boulerect.y >= 1200:
                self.bouleattak = False
                self.energiebowl = False
                self.boulerect.y = 110
                self.boulerect.x = 250
                self.test3 = True
                self.increment_boule = 0

    def attaque5(self, score, increment):
        if score >= SCORE_MINIBOSS + 5 and self.attaque1_moveinvert == False and self.attaque1_movevert == False and self.test4 == True:
            self.energiebowl1 = True
            self.energiebowlsound.play()
            self.test4 = False
        if self.energiebowl1:
            self.bouleload1 = True
        if self.bouleload1:
            self.increment_boule1 += 1
            if self.increment_boule1 < 20:
                self.bouleimage1 = self.bouleimageli1[0]
                self.boulerect1 = self.boulerectli1[0]
                self.boulemask1 = self.boulemaskli1[0]
            if 20 < self.increment_boule1 < 40:
                self.bouleimage1 = self.bouleimageli1[1]
                self.boulerect1 = self.boulerectli1[1]
                self.boulemask1 = self.boulemaskli1[1]
            if 40 < self.increment_boule1 < 60:
                self.bouleimage1 = self.bouleimageli1[1]
                self.boulerect1 = self.boulerectli1[1]
                self.boulemask1 = self.boulemaskli1[1]
            if self.increment_boule1 >= 80:
                self.bouleimage1 = self.bouleimageli1[0]
                self.boulerect1 = self.boulerectli1[0]
                self.boulemask1 = self.boulemaskli1[0]
                if self.persoinzone1 == True and self.attaque1_moveinvert == False and self.attaque1_movevert == False:
                    self.bouleattak1 = True
                    self.bouleload1 = False
        if self.bouleattak1:
            self.boulerect1.y += self.boulemove1y
            self.boulerect1.x += self.boulemove1x
            if self.boulerect1.y >= 1200 and self.attaque1_moveinvert == False and self.attaque1_movevert == False:
                self.bouleattak1 = False
                self.energiebowl1 = False
                self.boulerect1.y = 110
                self.boulerect1.x = 515
                self.test4 = True
                self.increment_boule1 = 0

    def attaque6(self, score, increment, perso):
        if self.canonalive == False and self.test5 == True and score > SCORE_MINIBOSS:
            self.laser = True
            self.laserload = True
            self.test5 = False
        if self.laserload:
            print("ok")
            self.increment_boule2 += 1
            if self.increment_boule2 < 20:
                self.bouleimage2 = self.bouleimageli2[0]
                self.boulerect2 = self.boulerectli2[0]
                self.boulemask2 = self.boulemaskli2[0]
            if 20 < self.increment_boule2 < 40:
                self.bouleimage2 = self.bouleimageli2[1]
                self.boulerect2 = self.boulerectli2[1]
                self.boulemask2 = self.boulemaskli2[1]
            if 40 < self.increment_boule2 < 60:
                self.bouleimage2 = self.bouleimageli2[1]
                self.boulerect2 = self.boulerectli2[1]
                self.boulemask2 = self.boulemaskli2[1]
            if self.increment_boule2 >= 60:
                self.bouleimage2 = self.bouleimageli2[0]
                self.boulerect2 = self.boulerectli2[0]
                self.boulemask2 = self.boulemaskli2[0]
                if self.attaque1_moveinvert == False and self.attaque1_movevert == False:
                    self.laserdep = True
                    self.laserload = False
                    self.timeb = time.time()
        if self.laserdep:
            if time.time() - self.timeb < 5:
                self.boulemove2x = (perso.rect.x + perso.size[0] / 2 - self.boulerect2[0]) / 75
                self.boulerect2.x += self.boulemove2x
            if time.time() - self.timeb > 5:
                self.boulemove2x = 0
                if self.boulerect2.y > 35:
                    self.boulerect2.y -= 1
                else:
                    if self.attaque1_moveinvert == False and self.attaque1_movevert == False:
                        self.laseer = True
                        self.timec = time.time()
                        self.laserdep = False
        if self.laseer:
            self.laserrect = self.boulerect2
            if time.time() - self.timec > 4:
                self.laseer = False
                self.laserdep = False
                self.laser = False
                self.test5 = True
