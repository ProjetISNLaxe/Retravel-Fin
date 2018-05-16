import pygame
from pygame.locals import *
from random import *
from battle.combatV3 import *
import random

SPEED = 8
class Personnage(pygame.sprite.Sprite):

    def __init__(self, nom):
        self.speed = SPEED
        self.pas1 = pygame.mixer.Sound("son/Sound/Run_0.wav")
        self.pas2 = pygame.mixer.Sound("son/Sound/Run_1.wav")
        self.pas3 = pygame.mixer.Sound("son/Sound/Run_2.wav")
        self.pas1.set_volume(0.1)
        self.pas2.set_volume(0.1)
        self.pas3.set_volume(0.1)
        self.imageperso = self.B1
        self.size = self.imageperso.get_size()
        self.rect = self.imageperso.get_rect()
        self.rect = Rect(400 - self.size[0] + 16, 600 - self.size[1], self.size[0], self.size[1])
        self.mask = pygame.mask.from_surface(self.imageperso)
        self.inc = 0
        self.glissright = False
        self.glisstop = False
        self.glissdown = False
        self.glissleft = False
        rectpersoactif = str("save1/pospeso/pospeso" + nom)
        try:
            with open(rectpersoactif, "r") as rectpersof:
                shaperso = rectpersof.read()
        except FileNotFoundError:
            with open(rectpersoactif, "w") as rectpersof:
                rectpersof.write("")
                shaperso = ""
        if shaperso == "":
            rectf = open("map/" + nom + "/spawn" + nom)
            carect = rectf.read().split(";")
            rectf.close()
            carect = carect[1].split(",")
            self.rect.x = int(carect[0])
            self.rect.y = int(carect[1])
        else:
            lipersorect = shaperso.split(",")
            self.rect.x = int(lipersorect[0])
            self.rect.y = int(lipersorect[1])
        if nom == "capitale":
            self.chance = 0.00004
        elif "fjordglas" in nom:
            self.chance = 0.001
        elif nom == "village":
            self.chance = 0.00008
        elif "guilde" in nom:
            self.chance = 0.001
        else : self.chance = 0

    def moveTop(self):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.B1
            self.rect.y -= int(self.size[1] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.B2
            self.rect.y -= int(self.size[1] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.B3
            self.rect.y -= int(self.size[1] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def moveRight(self):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.R1
            self.rect.x += int(self.size[0] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.R2
            self.rect.x += int(self.size[0] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.R3
            self.rect.x += int(self.size[0] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def moveLeft(self):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.L1
            self.rect.x -= int(self.size[0] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.L2
            self.rect.x -= int(self.size[0] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.L3
            self.rect.x -= int(self.size[0] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def moveDown(self):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.F1
            self.rect.y += int(self.size[1] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.F2
            self.rect.y += int(self.size[1] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.F3
            self.rect.y += int(self.size[1] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def mapDown(self, position):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.F1
            position.y -= int(self.size[1] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.F2
            position.y -= int(self.size[1] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.F3
            position.y -= int(self.size[1] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def mapLeft(self, position):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.L1
            position.x += int(self.size[0] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.L2
            position.x += int(self.size[0] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.L3
            position.x += int(self.size[0] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def mapRight(self, position):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.R1
            position.x -= int(self.size[0] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.R2
            position.x -= int(self.size[0] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.R3
            position.x -= int(self.size[0] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def mapTop(self, position):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.B1
            position.y += int(self.size[1] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.B2
            position.y += int(self.size[1] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.B3
            position.y += int(self.size[1] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def eventkey(self, position, masque, taille):
        self.mask = pygame.mask.from_surface(self.imageperso)
        tkey = pygame.key.get_pressed()
        if tkey[K_LSHIFT]:
            self.speed = int(SPEED/2)
        else:
            self.speed = SPEED
        if (tkey[K_UP] or tkey[K_w]) and position.y >= 0 or (tkey[K_UP] or tkey[K_w]) and self.rect.y > 300:
            for i in range(int(self.size[1] /4+1)):
                if masque.overlap(self.mask,
                                  (self.rect.x - position.x, self.rect.y - i - position.y)) or self.rect.x <= 0:
                    break
                if i == int(self.size[1] /4):
                    self.moveTop()
        elif (tkey[K_UP] or tkey[K_w]) and position.y <= 0:
            for i in range(int(self.size[1] /4+1)):
                if masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y - i)):
                    break
                if i == int(self.size[1] /4):
                    self.mapTop(position)
        if (tkey[K_DOWN] or tkey[K_s]) and position.y <= -taille[1] + 600 or (tkey[K_DOWN] or tkey[K_s]) and self.rect.y < 200:

            for i in range(int(self.size[1] /4 + 1)):
                if masque.overlap(self.mask,
                                  (self.rect.x - position.x, self.rect.y + i - position.y)) or self.rect.y >= 600 - \
                        self.size[1]:
                    break
                if i == int(self.size[1] /4):
                    self.moveDown()
        elif (tkey[K_DOWN] or tkey[K_s]) and position.y >= -taille[1] + 600:
            for i in range(int(self.size[1] /4 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y + i)):
                    break
                if i == int(self.size[1] /4):
                    self.mapDown(position)

        if (tkey[K_LEFT] or tkey[K_a]) and position.x >= 0 or (tkey[K_LEFT] or tkey[K_a]) and self.rect.x > 400:
            for i in range(int(self.size[0] /4 + 1)):
                if masque.overlap(self.mask,
                                  (self.rect.x - i - position.x, self.rect.y - position.y)) or self.rect.x <= 0:
                    break
                if i == int(self.size[0] /4):
                    self.moveLeft()
        elif (tkey[K_LEFT] or tkey[K_a]) and position.x <= 0:
            for i in range(int(self.size[0] /4 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x - i, self.rect.y - position.y)):
                    break
                if i == int(self.size[0] /4):
                    self.mapLeft(position)

        if (tkey[K_RIGHT] or tkey[K_d]) and position.x <= -taille[0] + 800 or (tkey[K_RIGHT] or tkey[K_d]) and self.rect.x < 400:
            for i in range(int(self.size[0] /4 + 1)):
                if masque.overlap(self.mask,
                                  (self.rect.x + i - position.x, self.rect.y - position.y)) or self.rect.x >= 800 - \
                        self.size[0]:
                    break
                if i == int(self.size[0] /4):
                    self.moveRight()
        elif (tkey[K_RIGHT] or tkey[K_d]) and position.x >= -taille[0] + 800:
            for i in range(int(self.size[0] /4 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x + i, self.rect.y - position.y)):
                    break
                if i == int(self.size[0] /4):
                    self.mapRight(position)

        if masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)):
            try:
                if ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                        0] + position.x - self.rect.x) >= 0:
                    self.rect.x += int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            0] + position.x - self.rect.x) / 5
                elif ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                          0] + position.x - self.rect.x) <= 0:
                    self.rect.x -= int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            0] + position.x - self.rect.x) / 5
                if ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                        1] + position.y - self.rect.y) >= 0:
                    self.rect.y -= int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            1] + position.y - self.rect.y) / 5
                elif ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                          1] + position.y - self.rect.y) <= 0:
                    self.rect.y += int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            1] + position.y - self.rect.y) / 5
            except TypeError:
                pass
        if position.y < -taille[1] + 600:
            position.y = -taille[1] + 600
        if position.y > 0:
            position.y = 0
        if position.x > 0:
            position.x = 0
        if position.x < -taille[0] + 800:
            position.x = -taille[0] + 800

    def eventkeytest(self, position, masque, taille, pnj):
        self.mask = pygame.mask.from_surface(self.imageperso)
        tkey = pygame.key.get_pressed()
        tobreak = False
        if (tkey[K_UP] or tkey[K_w]) and position.y >= 0 or (tkey[K_UP] or tkey[K_w]) and self.rect.y > 300:
            for i in range(int(self.size[1] /4)):
                if masque.overlap(self.mask,
                                  (self.rect.x - position.x, self.rect.y - i - position.y)) or self.rect.x <= 0:
                    break
                for j in range(len(pnj)):
                    if pnj[j].overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)):
                        tobreak = True
                        break
                if tobreak:
                    break
                if i == int(self.size[1] /4 - 1):
                    self.moveTop()
        elif (tkey[K_UP] or tkey[K_w]) and position.y <= 0:
            for i in range(int(self.size[1] /4 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y - i)):
                    break
                for j in range(len(pnj)):
                    if pnj[j].overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y - i)):
                        tobreak = True
                        break
                if tobreak:
                    break
                if i == int(self.size[1] /4):
                    self.mapTop(position)
        if (tkey[K_DOWN] or tkey[K_s]) and position.y <= -taille[1] + 600 or (tkey[K_DOWN] or tkey[K_s]) and self.rect.y < 200:

            for i in range(int(self.size[1] /4 + 1)):
                if masque.overlap(self.mask,
                                  (self.rect.x - position.x, self.rect.y + 1 - position.y)) or self.rect.y >= 600 - \
                        self.size[1]:
                    break
                if i == int(self.size[1] /4):
                    self.moveDown()
        elif (tkey[K_DOWN] or tkey[K_s]) and position.y >= -taille[1] + 600:
            for i in range(int(self.size[1] /4 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y + 1)):
                    break
                if i == int(self.size[1] /4):
                    self.mapDown(position)

        if (tkey[K_LEFT] or tkey[K_a]) and position.x >= 0 or (tkey[K_LEFT] or tkey[K_a]) and self.rect.x > 400:
            for i in range(int(self.size[0] /4 + 1)):
                if masque.overlap(self.mask,
                                  (self.rect.x - i - position.x, self.rect.y - position.y)) or self.rect.x <= 0:
                    break
                if i == int(self.size[0] /4):
                    self.moveLeft()
        elif (tkey[K_LEFT] or tkey[K_a]) and position.x <= 0:
            for i in range(int(self.size[0] /4 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x - i, self.rect.y - position.y)):
                    break
                if i == int(self.size[0] /4):
                    self.mapLeft(position)

        if (tkey[K_RIGHT] or tkey[K_d]) and position.x <= -taille[0] + 800 or (tkey[K_RIGHT] or tkey[K_d]) and self.rect.x < 400:
            for i in range(int(self.size[0] /4 + 1)):
                if masque.overlap(self.mask,
                                  (self.rect.x + i - position.x, self.rect.y - position.y)) or self.rect.x >= 800 - \
                        self.size[0]:
                    break
                if i == int(self.size[0] /4):
                    self.moveRight()
        elif (tkey[K_RIGHT] or tkey[K_d]) and position.x >= -taille[0] + 800:
            for i in range(int(self.size[0] /4 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x + i, self.rect.y - position.y)):
                    break
                if i == int(self.size[0] /4):
                    self.mapRight(position)

        if masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)):
            try:
                if ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                        0] + position.x - self.rect.x) >= 0:
                    self.rect.x += int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            0] + position.x - self.rect.x) / 5
                elif ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                          0] + position.x - self.rect.x) <= 0:
                    self.rect.x -= int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            0] + position.x - self.rect.x) / 5
                if ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                        1] + position.y - self.rect.y) >= 0:
                    self.rect.y -= int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            1] + position.y - self.rect.y) / 5
                elif ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                          1] + position.y - self.rect.y) <= 0:
                    self.rect.y += int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            1] + position.y - self.rect.y) / 5
            except:
                0
        if position.y < -taille[1] + 600:
            position.y = -taille[1] + 600
        if position.y > 0:
            position.y = 0#Pas que la map se décale
        if position.x > 0:
            position.x = 0
        if position.x < -taille[0] + 800:
            position.x = -taille[0] + 800

    def glisse(self, position, masque, taille):
        """Mode glisse dans fjordglas"""
        self.mask = pygame.mask.from_surface(self.imageperso)
        tkey = pygame.key.get_pressed()
        if (tkey[K_UP] or tkey[K_w]) and position.y >= 0 or (tkey[K_UP] or tkey[K_w]) and self.rect.y > 300 or self.glisstop and position.y >= 0 or self.glisstop and self.rect.y > 300:
            for i in range(int(self.size[1] /4)):
                if masque.overlap(self.mask,
                                  (self.rect.x - position.x, self.rect.y - i - position.y)) or self.rect.x <= 0:
                    self.glisstop = False
                    break
                if i == int(
                        self.size[1] /4 - 1) and not self.glissright and not self.glissleft and not self.glissdown:
                    self.glisstop = True
                    self.glisseTop()
        elif (tkey[K_UP] or tkey[K_w]) and position.y <= 0 or self.glisstop and position.y <= 0:
            for i in range(int(self.size[1] /4 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y - i)):
                    self.glisstop = False
                    break
                if i == int(self.size[1] /4) and not self.glissright and not self.glissleft and not self.glissdown:
                    self.glisstop = True
                    self.mapglisseTop(position)
        if (tkey[K_DOWN] or tkey[K_s]) and position.y <= -taille[1] + 600 or (tkey[K_DOWN] or tkey[K_s]) and self.rect.y < 200 or self.glissdown and position.y <= -taille[1] + 600 or self.glissdown and self.rect.y < 200:

            for i in range(int(self.size[1] /4 + 1)):
                if masque.overlap(self.mask,(self.rect.x - position.x, self.rect.y + 1 - position.y)) or self.rect.y >= 600 - self.size[1]:
                    self.glissdown = False
                    break
                if i == int(self.size[1] /4) and not self.glisstop and not self.glissright and not self.glissleft:
                    self.glissdown = True
                    self.glisseDown()
        elif (tkey[K_DOWN] or tkey[K_s]) and position.y >= -taille[1] + 600 or self.glissdown and position.y >= -taille[1] + 600:
            for i in range(int(self.size[1] /4 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y + 1)):
                    self.glissdown = False
                    break
                if i == int(self.size[1] /4) and not self.glisstop and not self.glissright and not self.glissleft:
                    self.glissdown = True
                    self.mapglisseDown(position)

        if (tkey[K_LEFT] or tkey[K_a]) and position.x >= 0 or (tkey[K_LEFT] or tkey[K_a]) and self.rect.x > 400 or self.glissleft and position.x >= 0 or self.glissleft and self.rect.x > 400:
            for i in range(int(self.size[0] /4 + 1)):
                if masque.overlap(self.mask,
                                  (self.rect.x - i - position.x, self.rect.y - position.y)) or self.rect.x <= 0:
                    self.glissleft = False
                    break
                if i == int(self.size[0] /4) and not self.glisstop and not self.glissright and not self.glissdown:
                    self.glissleft = True
                    self.glisseLeft()
        elif (tkey[K_LEFT] or tkey[K_a]) and position.x <= 0 or self.glissleft and position.x <= 0:
            for i in range(int(self.size[0] /4 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x - i, self.rect.y - position.y)):
                    self.glissleft = False
                    break
                if i == int(self.size[0] /4) and not self.glisstop and not self.glissright and not self.glissdown:
                    self.glissleft = True
                    self.mapglisseLeft(position)

        if (tkey[K_RIGHT] or tkey[K_d]) and position.x <= -taille[0] + 800 or (tkey[K_RIGHT] or tkey[K_d]) and self.rect.x < 400 or self.glissright and position.x <= -taille[
            0] + 800 or self.glissright and self.rect.x < 400:
            for i in range(int(self.size[0] /4 + 1)):
                if masque.overlap(self.mask,(self.rect.x + i - position.x, self.rect.y - position.y)) or self.rect.x >= 800 - self.size[0]:
                    self.glissright = False
                    break
                if i == int(self.size[0] /4) and not self.glisstop and not self.glissleft and not self.glissdown:
                    self.glissright = True
                    self.glisseRight()
        elif (tkey[K_RIGHT] or tkey[K_d]) and position.x >= -taille[0] + 800 or self.glissright and position.x >= -taille[0] + 800:
            for i in range(int(self.size[0] /4 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x + i, self.rect.y - position.y)):
                    self.glissright = False
                    break
                if i == int(self.size[0] /4) and not self.glisstop and not self.glissleft and not self.glissdown:
                    self.glissright = True
                    self.mapglisseRight(position)

        if masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)):
            try:
                if ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                        0] + position.x - self.rect.x) >= 0:
                    self.rect.x += int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            0] + position.x - self.rect.x) / 5
                elif ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                          0] + position.x - self.rect.x) <= 0:
                    self.rect.x -= int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            0] + position.x - self.rect.x) / 5
                if ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                        1] + position.y - self.rect.y) >= 0:
                    self.rect.y -= int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            1] + position.y - self.rect.y) / 5
                elif ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                          1] + position.y - self.rect.y) <= 0:
                    self.rect.y += int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            1] + position.y - self.rect.y) / 5
            except:
                0
        if position.y < -taille[1] + 600:
            position.y = -taille[1] + 600
        if position.y > 0:
            position.y = 0
        if position.x > 0:
            position.x = 0
        if position.x < -taille[0] + 800:
            position.x = -taille[0] + 800

    def glisseTop(self):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.B1
            self.rect.y -= int(self.size[1] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.B1
            self.rect.y -= int(self.size[1] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.B1
            self.rect.y -= int(self.size[1] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def glisseRight(self):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.R1
            self.rect.x += int(self.size[0] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.R1
            self.rect.x += int(self.size[0] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.R1
            self.rect.x += int(self.size[0] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def glisseLeft(self):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.L1
            self.rect.x -= int(self.size[0] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.L1
            self.rect.x -= int(self.size[0] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.L1
            self.rect.x -= int(self.size[0] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def glisseDown(self):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.F1
            self.rect.y += int(self.size[1] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.F1
            self.rect.y += int(self.size[1] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.F1
            self.rect.y += int(self.size[1] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def mapglisseDown(self, position):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.F1
            position.y -= int(self.size[1] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.F1
            position.y -= int(self.size[1] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.F1
            position.y -= int(self.size[1] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def mapglisseLeft(self, position):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.L1
            position.x += int(self.size[0] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.L1
            position.x += int(self.size[0] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.L1
            position.x += int(self.size[0] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def mapglisseRight(self, position):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.R1
            position.x -= int(self.size[0] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.R1
            position.x -= int(self.size[0] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.R1
            position.x -= int(self.size[0] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0

    def mapglisseTop(self, position):
        if random.random() <= self.chance:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.pas1.play()
            self.imageperso = self.B1
            position.y += int(self.size[1] /4)
        if self.inc == int(self.speed):
            self.pas2.play()
            self.imageperso = self.B1
            position.y += int(self.size[1] /4)
        if self.inc == int(2 * self.speed):
            self.pas3.play()
            self.imageperso = self.B1
            position.y += int(self.size[1] /4)
        if self.inc >= int(3 * self.speed):
            self.inc = 0


class persobase(Personnage):
    def __init__(self, nom):
        self.B1 = pygame.image.load("perso/N-Ship/B1.png")
        self.B2 = pygame.image.load("perso/N-Ship/B2.png")
        self.B3 = pygame.image.load("perso/N-Ship/B3.png")

        self.F1 = pygame.image.load("perso/N-Ship/F1.png")
        self.F2 = pygame.image.load("perso/N-Ship/F2.png")
        self.F3 = pygame.image.load("perso/N-Ship/F3.png")

        self.R1 = pygame.image.load("perso/N-Ship/R1.png")
        self.R2 = pygame.image.load("perso/N-Ship/R2.png")
        self.R3 = pygame.image.load("perso/N-Ship/R3.png")

        self.L1 = pygame.image.load("perso/N-Ship/L1.png")
        self.L2 = pygame.image.load("perso/N-Ship/L2.png")
        self.L3 = pygame.image.load("perso/N-Ship/L3.png")
        Personnage.__init__(self, nom)


class David():
    def __init__(self):
        self.B1 = pygame.image.load("perso/David/B1.png").convert_alpha()
        self.B2 = pygame.image.load("perso/David/B2.png").convert_alpha()
        self.B3 = pygame.image.load("perso/David/B3.png").convert_alpha()

        self.F1 = pygame.image.load("perso/David/F1.png").convert_alpha()
        self.F2 = pygame.image.load("perso/David/F2.png").convert_alpha()
        self.F3 = pygame.image.load("perso/David/F3.png").convert_alpha()

        self.R1 = pygame.image.load("perso/David/R1.png").convert_alpha()
        self.R2 = pygame.image.load("perso/David/R2.png").convert_alpha()
        self.R3 = pygame.image.load("perso/David/R3.png").convert_alpha()

        self.L1 = pygame.image.load("perso/David/L1.png").convert_alpha()
        self.L2 = pygame.image.load("perso/David/L2.png").convert_alpha()
        self.L3 = pygame.image.load("perso/David/L3.png").convert_alpha()
        self.image = self.B1
        self.rect = self.image.get_rect()
        self.rect.x = 1400
        self.rect.y = 963
        self.inc = 0
        self.incl = 0
        self.incf = 0
        self.incb = 0

    def move(self):
        self.inc += 1
        if self.inc < 20:
            self.incl += 1
            if self.incl == 3:
                self.image = self.L1
            if self.incl == 6:
                self.image = self.L2
            if self.incl == 9:
                self.image = self.L3
                self.incl = 0
            self.rect.x -= 5
        if 20 < self.inc < 30:
            self.incl = 0
            self.incb += 1
            if self.incb == 3:
                self.image = self.B1
            if self.incb == 6:
                self.image = self.B2
            if self.incb == 9:
                self.image = self.B3
                self.incb = 0
            self.rect.y -= 5
        if 30 < self.inc < 110:
            self.incl += 1
            if self.incl == 3:
                self.image = self.L1
            if self.incl == 6:
                self.image = self.L2
            if self.incl == 9:
                self.image = self.L3
                self.incl = 0
            self.rect.x -= 5
        if 110 < self.inc < 155:
            self.incl = 0
            self.incf += 1
            if self.incf == 3:
                self.image = self.F1
            if self.incf == 6:
                self.image = self.F2
            if self.incf == 9:
                self.image = self.F3
                self.incf = 0
            self.rect.y += 5
        if self.inc > 155:
            self.image = self.F1

    def move2(self):
        self.inc += 1
        if self.inc < 15:
            self.incl += 1
            if self.incl == 3:
                self.image = self.L1
            if self.incl == 6:
                self.image = self.L2
            if self.incl == 9:
                self.image = self.L3
                self.incl = 0
            self.rect.y += 5
        if 15 < self.inc < 75:
            self.incl = 0
            self.incb += 1
            if self.incb == 3:
                self.image = self.L1
            if self.incb == 6:
                self.image = self.L2
            if self.incb == 9:
                self.image = self.L3
                self.incb = 0
            self.rect.x -= 5
        if 75 < self.inc < 160:
            self.incl += 1
            if self.incl == 3:
                self.image = self.F1
            if self.incl == 6:
                self.image = self.F2
            if self.incl == 9:
                self.image = self.F3
                self.incl = 0
            self.rect.y += 5

        if self.inc > 160:
            self.image = self.F1
            with open("menu/quetes/jeanma/diamaison_2", "w") as diamaison2:
                diamaison2.write("1")

    def move3(self):
        self.inc += 1
        if self.inc < 15:
            self.incl += 1
            if self.incl == 3:
                self.image = self.L1
            if self.incl == 6:
                self.image = self.L2
            if self.incl == 9:
                self.image = self.L3
                self.incl = 0
            self.rect.y += 5
        if self.inc > 15:
            self.image = self.F1


class Rogue():
    def __init__(self):
        self.B1 = pygame.image.load("perso/Rogue/B1.png").convert_alpha()
        self.B2 = pygame.image.load("perso/Rogue/B2.png").convert_alpha()
        self.B3 = pygame.image.load("perso/Rogue/B3.png").convert_alpha()

        self.F1 = pygame.image.load("perso/Rogue/F1.png").convert_alpha()
        self.F2 = pygame.image.load("perso/Rogue/F2.png").convert_alpha()
        self.F3 = pygame.image.load("perso/Rogue/F3.png").convert_alpha()

        self.R1 = pygame.image.load("perso/Rogue/R1.png").convert_alpha()
        self.R2 = pygame.image.load("perso/Rogue/R2.png").convert_alpha()
        self.R3 = pygame.image.load("perso/Rogue/R3.png").convert_alpha()

        self.L1 = pygame.image.load("perso/Rogue/L1.png").convert_alpha()
        self.L2 = pygame.image.load("perso/Rogue/L2.png").convert_alpha()
        self.L3 = pygame.image.load("perso/Rogue/L3.png").convert_alpha()
        self.image = self.B1
        self.rect = self.image.get_rect()
        self.rect.x = 1280
        self.rect.y = 3453
        self.inc = 0
        self.incl = 0
        self.incf = 0
        self.incb = 0

    def move(self):
        self.inc += 1
        if self.inc < 50:
            self.incl += 1
            if self.incl == 3:
                self.image = self.B1
            if self.incl == 6:
                self.image = self.B2
            if self.incl == 9:
                self.image = self.B3
                self.incl = 0
            self.rect.y -= 5
        if 50 < self.inc < 100:
            self.incl = 0
            self.incb += 1
            if self.incb == 3:
                self.image = self.R1
            if self.incb == 6:
                self.image = self.R2
            if self.incb == 9:
                self.image = self.R3
                self.incb = 0
            self.rect.x += 5
        if 100 < self.inc < 150:
            self.incl += 1
            if self.incl == 3:
                self.image = self.L1
            if self.incl == 6:
                self.image = self.L2
            if self.incl == 9:
                self.image = self.L3
                self.incl = 0
            self.rect.x -= 5
        if 150 < self.inc < 230:
            self.incl = 0
            self.incf += 1
            if self.incf == 3:
                self.image = self.F1
            if self.incf == 6:
                self.image = self.F2
            if self.incf == 9:
                self.image = self.F3
                self.incf = 0
            self.rect.y += 5
        if self.inc > 230:
            self.image = self.F1
            with open("menu/quetes/jeanma/vol", "w") as jeanmavol:
                jeanmavol.write("1")
