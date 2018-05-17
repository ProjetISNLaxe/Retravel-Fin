import pygame
from pygame.locals import *
from random import *
import random
import time
import menu.closemenu as closemenu
import maps, respawn
pygame.init()
with open("options\\fullscreen", "r") as fullscreen:
    fullscreenread = fullscreen.read()

if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else:
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)


class attaqueennemi():
    def __init__(self):
        self.p = 0

    def cible(self):
        if not sinatra.active:
            n = [1, 2]
        else:
            n = [1, 2, 3]
        if david.vie == 0:
            n[1] = 0
        if perso_joueur.vie == 0:
            n[0] = 0
        if sinatra.vie == 0 and sinatra.active:
            n[2] = 0
        self.p = choice(n)
        if david.taunt!=0 and david.vie!=0:
            self.p=2
        while self.p == 0:
            self.p = choice(n)

    def verification(self):
        if david.vie <= 0:
            david.alive = False
            david.vie = 0
        if perso_joueur.vie <= 0:
            perso_joueur.alive = False
            perso_joueur.vie = 0
        if sinatra.vie <= 0:
            sinatra.alive = False
            sinatra.vie = 0
        if sinatra.active:
            if sinatra.vie == 0 and david.vie == 0 and perso_joueur.vie == 0:
                combat.etat = "mort"
                respawn.respawn()
                fondu = pygame.Surface((800, 600))
                fondu.set_alpha(0)
                fondu.fill((0, 0, 0))
                for i in range(255):
                    fenetre.blit(fondu, (0, 0))
                    fondu.set_alpha(i)
                    pygame.display.flip()

                maps.selecmap()
        elif david.vie == 0 and perso_joueur.vie == 0:
            combat.etat = "mort"
            respawn.respawn()
            fondu = pygame.Surface((800, 600))
            fondu.set_alpha(0)
            fondu.fill((0, 0, 0))
            for i in range(255):
                fenetre.blit(fondu, (0, 0))
                fondu.set_alpha(i)
                pygame.display.flip()

            maps.selecmap()

class menu:
    def __init__(self):
        self.menu_ = 0


class sac:
    def __init__(self, q, image):
        self.quantite = q
        self.imageanim = pygame.image.load(image).convert_alpha()


class bataille:
    def __init__(self):
        self.etat = "combatencour"
        self.anim = 0
        self.tour = 1
        self.hardcore=False


class perso(pygame.sprite.Sprite):
    def __init__(self, imageperso, imageperso2, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(imageperso).convert_alpha()
        self.image2 = pygame.image.load(imageperso2).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()
        self.alive = True
        self.niveau = 1
        self.xp = 0
        self.ptdecompetance = 0
        self.ptforce = 0
        self.ptvie = 0
        self.bonus = 0
        self.ingame = False
        self.verificationvie=1
        self.empoisoner = 0
        if self.xp >= 50 * self.niveau:
            self.xp -= 50 * self.niveau
            self.niveau += 1
            self.ptdecompetance += 1


class perso1(perso):
    def __init__(self):
        perso.__init__(self, "battle/imagebonhomme/joueur/combivaisseau/Perso1nship0.png",
                       "battle/imagebonhomme/joueur/combivaisseau/Perso1nship1.png")
        self.vie = 150
        self.mana = 100
        self.fleche = 0
        self.armure = 0
        self.ptmana = 0
        self.sortdefeu = False
        self.viemax = 150 + (self.ptvie * 20)
        if self.ptmana == 1:
            self.sortdefeu = True


class perso2(perso):
    def __init__(self):
        perso.__init__(self, "battle/imagebonhomme/perso2/perso2base0.png", "battle/imagebonhomme/perso2/perso2base1.png")
        self.vie = 200
        self.taunt = 0
        self.armure = 10
        self.ptbouclier = 0
        self.immortal = False
        self.viemax = 200 + (self.ptvie * 20)


class perso3(perso):
    def __init__(self):
        perso.__init__(self, "battle/imagebonhomme/perso3/perso3armurebase.png",
                       "battle/imagebonhomme/perso3/perso3armurebase2.png")
        self.vie = 150
        self.active = False
        self.poison = False
        self.ptdodge = 0
        self.viemax = 150 + (self.ptvie * 20)


class affichage():
    def __init__(self):
        0

    def affichageanimennemi(self, d, varanim):
        fichier = open("save1/map", "r")
        map = fichier.read()
        fichier.close()

        if map == "capitale":
            fond = pygame.image.load("battle/Battlebacks/009-CastleTown01.jpg")
        elif map == "chateau_3F":
            fond = pygame.image.load("battle/Battlebacks/026-Castle02.jpg")
        elif map == "caverne":
            fond = pygame.image.load("battle/Battlebacks/043-Cave01.jpg")
        elif map == "mapdepart":
            fond = pygame.image.load("battle/Battlebacks/005-Beach01.jpg")
        elif "fjord" in map:
            fond = pygame.image.load("battle/Battlebacks/icecave.png").convert_alpha()
        elif map=="village":
            fond = pygame.image.load("battle/Battlebacks/003-Forest01.jpg")
        else:fond = pygame.image.load("battle/Battlebacks/043-Cave01.jpg")
        clock = pygame.time.Clock()
        my_font = pygame.font.SysFont("Calibri", 36)
        bandeaubleue = pygame.image.load("battle/animation/Fightblue.png").convert_alpha()
        bandeaurouge = pygame.image.load("battle/animation/Fightred.png").convert_alpha()
        pointinterro = pygame.image.load("battle/animation/pointintero.png").convert_alpha()
        feu = pygame.image.load("battle/animation/fire.png").convert_alpha()
        feus=pygame.mixer.Sound("son/bruit/Fire1.ogg")
        malediction = pygame.image.load("battle/animation/malediction.png").convert_alpha()
        damage = pygame.mixer.Sound("son/bruit/Damage2.ogg")
        fenetre.blit(fond, (0, 0))
        for i in range (42):
            for event in pygame.event.get():
                if event.type == QUIT:  # pour pouvoir quitter le jeux
                    closemenu.closemenu()
            fenetre.blit(bandeaubleue, (811 - i * 10, 200))
            fenetre.blit(bandeaurouge, (-421 + i * 10, 200))
            i += 1
            clock.tick(60)
            pygame.display.flip()
        for i in range(160):
            for event in pygame.event.get():
                if event.type == QUIT:  # pour pouvoir quitter le jeux
                     closemenu.closemenu()
            fenetre.blit(bandeaubleue, (390, 200))
            fenetre.blit(bandeaurouge, (-1, 200))

            if i < 80:
                if varanim!=3 and varanim!=4 and varanim!=1 :
                    if fennemi.p == 2 or david.taunt > 0:
                        fenetre.blit(david.image, (659, 200))
                    elif fennemi.p == 1:
                        fenetre.blit(perso_joueur.image, (659, 200))
                    elif fennemi.p == 3:
                        fenetre.blit(sinatra.image, (659, 200))
                if varanim==1:
                        fenetre.blit(enemitipe.image, (11, 200))
                        fenetre.blit(david.image, (625, 150))
                        fenetre.blit(perso_joueur.image, (610, 230))
                elif varanim==2:
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(pointinterro, (11, 100))
                elif varanim==3:
                    fenetre.blit(sinatra.image, (640, 70))
                    fenetre.blit(david.image, (625, 150))
                    fenetre.blit(perso_joueur.image, (610, 230))
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(feu, (600, 150))

                elif varanim==4:
                    fenetre.blit(sinatra.image, (640, 70))
                    fenetre.blit(david.image, (625, 150))
                    fenetre.blit(perso_joueur.image, (610, 230))
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(malediction, (600, 150))
                elif varanim==5:
                        fenetre.blit(enemitipe.image, (11, 200))
                elif varanim==0:
                        fenetre.blit(enemitipe.image, (11 + i * 4, 200))
            if i==80:
                if varanim==0:
                    damage.play()
                if varanim==3:
                    feus.play()
            if i > 80:
                if varanim!=3 and varanim!=4 and varanim!=1:
                    if fennemi.p == 2 or david.taunt > 0:
                        fenetre.blit(david.image, (689, 200))
                    elif fennemi.p == 1:
                        fenetre.blit(perso_joueur.image, (659, 200))
                    elif fennemi.p == 3:
                        fenetre.blit(sinatra.image, (659, 200))
                else:
                    if varanim != 1:
                        fenetre.blit(sinatra.image, (640, 70))
                        fenetre.blit(david.image, (625, 150))
                        fenetre.blit(perso_joueur.image, (610, 230))
                if varanim == 1:
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(david.image, (625, 150))
                    fenetre.blit(perso_joueur.image, (610, 230))
                    fenetre.blit(my_font.render("poison", 3, (0, 200, 10)), (659, 180))
                elif varanim==2:
                    fenetre.blit(enemitipe.image, (11, 200))
                    if d>0:
                        fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (659, 180))
                    elif d<0:
                        fenetre.blit(my_font.render(str(-d), 3, (10, 255, 10)), (659, 180))
                    elif d==0:
                        fenetre.blit(my_font.render(str(d), 3, (10, 10, 10)), (659, 180))
                elif varanim == 3:
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(my_font.render(str(d)+"*3", 3, (255, 10, 10)), (659, 180))
                elif varanim == 4:
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(malediction, (600, 150))
                elif varanim == 5:
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(my_font.render("1000", 3, (100, 255, 10)), (30, 180))
                elif varanim==0:
                    fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (659, 180))
                    fenetre.blit(enemitipe.image, (411, 200))



            clock.tick(60)
            pygame.display.flip()

    def affichage(self, action, choix):
        my_font = pygame.font.SysFont("Calibri", 18)  # les different taille d'ecriture
        my_font2 = pygame.font.SysFont("Calibri", 19)
        fichier = open("save1/map", "r")
        map = fichier.read()
        fichier.close()

        if map == "capitale":
            fond = pygame.image.load("battle/Battlebacks/009-CastleTown01.jpg")
        elif map == "chateau_3F":
            fond = pygame.image.load("battle/Battlebacks/026-Castle02.jpg")
        elif map == "caverne":
            fond = pygame.image.load("battle/Battlebacks/043-Cave01.jpg")
        elif map == "mapdepart":
            fond = pygame.image.load("battle/Battlebacks/005-Beach01.jpg")
        elif "fjord" in map:
            fond = pygame.image.load("battle/Battlebacks/icecave.png").convert_alpha()
        elif map=="village":
            fond = pygame.image.load("battle/Battlebacks/003-Forest01.jpg")
        else:fond = pygame.image.load("battle/Battlebacks/043-Cave01.jpg"
                                      )
        bulle = pygame.image.load("battle/animation/bullecombat.png")
        barreviemonstre = pygame.image.load("battle/animation/barreviemonstre.png")
        barreviemonstre1 = pygame.image.load("battle/animation/barreviemonstre1.png")
        barrevieperso = pygame.image.load("battle/animation/barrevieperso.png")
        barrevieperso1 = pygame.image.load("battle/animation/barrevieperso1.png")
        poison = pygame.image.load("battle/animation/poison.png")



        position1 = (550, 200)  # la position du perso qui jou
        position2 = (565, 120)  # la position du perso qui attent
        position3 = (580, 40)  # la position du perso qui attent
        positionpv3 = (665, 20)  # la position des pv du perso qui jou
        positionpv2 = (665, 45)  # la position des pv du perso qui attend
        positionpv1 = (665, 70)  # la position des pv du perso qui attend
        pv3=20
        pv2=45
        pv1=70
        position_ennemi1 = (100, 100)

        fenetre.blit(fond, (0, 0))
        fenetre.blit(bulle, (0, 420))
        if voleur.poison>0 or sinatramechante.poison:
            fenetre.blit(poison, (770, 380))
        if sinatra.poison:
            fenetre.blit(poison, (20, 380))

        for i in range(4):
            fenetre.blit(my_font.render(action[i], False, (255, 255, 255)), (530, 500 + i * 20))

        pourcentagepvennemie = int((enemitipe.vie / enemitipe.viemax) * 100)
        pourcentagepvjoueur=int((perso_joueur.vie/perso_joueur.viemax)*100)
        pourcentagepvdavid = int((david.vie / david.viemax) * 100)
        pourcentagepvsinatra = int((sinatra.vie / sinatra.viemax) * 100)

        fenetre.blit(barreviemonstre, (0, 20))
        fenetre.blit(barreviemonstre1, (pourcentagepvennemie*2-200, 20))




        fenetre.blit(my_font2.render(str(enemitipe.vie), False, (255, 255, 255)), (210, 20))
        if combat.tour == 1:
            fenetre.blit(my_font.render(str(perso_joueur.mana), False, (255, 255, 255)), (80, 500))
            fenetre.blit(my_font.render(str(perso_joueur.fleche), False, (255, 255, 255)), (80, 520))
            fenetre.blit(my_font.render("mana:", False, (255, 255, 255)), (20, 500))
            fenetre.blit(my_font.render("fleches:", False, (255, 255, 255)), (20, 520))
        if objet.menu_ == 1:
            fenetre.blit(my_font.render(str(soin.quantite), False, (255, 255, 255)), (670, 520))
            fenetre.blit(my_font.render(str(resurection.quantite), False, (255, 255, 255)), (670, 500))
            fenetre.blit(my_font.render(str(manap.quantite), False, (255, 255, 255)), (670, 540))
        if combat.tour == 1:
            if not sinatra.active:
                david.rect = position2  # endroit de spawn du perso
                perso_joueur.rect = position1
            else:
                sinatra.rect = position3
                david.rect = position2  # endroit de spawn du perso
                perso_joueur.rect = position1
            if sinatra.active and sinatra.alive == True and david.alive == True:
                fenetre.blit(sinatra.image, sinatra.rect)
                fenetre.blit(my_font2.render(str(sinatra.vie), False, (255, 255, 255)), positionpv3)
                fenetre.blit(barrevieperso, (696, pv3))
                fenetre.blit(barrevieperso1, (796 - pourcentagepvsinatra, pv3))
            if david.alive == True:
                fenetre.blit(david.image, david.rect)
                fenetre.blit(my_font2.render(str(david.vie), False, (255, 255, 255)), positionpv2)
                fenetre.blit(barrevieperso, (696, pv2))
                fenetre.blit(barrevieperso1, (796 - pourcentagepvdavid, pv2))
            elif sinatra.active and sinatra.alive == True:
                fenetre.blit(sinatra.image, sinatra.rect)
                fenetre.blit(my_font2.render(str(sinatra.vie), False, (255, 255, 255)), positionpv2)
                fenetre.blit(barrevieperso, (696, pv2))
                fenetre.blit(barrevieperso1, (796 - pourcentagepvdavid, pv2))


            fenetre.blit(perso_joueur.image, perso_joueur.rect)

            fenetre.blit(my_font2.render(str(perso_joueur.vie), False, (255, 255, 255)), positionpv1)
            fenetre.blit(barrevieperso, (696, pv1))
            fenetre.blit(barrevieperso1, (796 - pourcentagepvjoueur, pv1))


        if combat.tour == 2:
            if not sinatra.active:
                david.rect = position1  # endroit de spawn du perso
                perso_joueur.rect = position2
            else:
                sinatra.rect = position2
                david.rect = position1  # endroit de spawn du perso
                perso_joueur.rect = position3

            if perso_joueur.alive == True and sinatra.active and sinatra.alive == True:
                fenetre.blit(perso_joueur.image, perso_joueur.rect)
                fenetre.blit(my_font2.render(str(perso_joueur.vie), False, (255, 255, 255)), positionpv3)
                fenetre.blit(barrevieperso, (696, pv3))
                fenetre.blit(barrevieperso1, (796 - pourcentagepvjoueur, pv3))

            if sinatra.active and sinatra.alive == True:
                fenetre.blit(sinatra.image, sinatra.rect)
                fenetre.blit(my_font2.render(str(sinatra.vie), False, (255, 255, 255)), positionpv2)
                fenetre.blit(barrevieperso, (696, pv2))
                fenetre.blit(barrevieperso1, (796 - pourcentagepvsinatra, pv2))
            elif perso_joueur.alive == True:
                fenetre.blit(perso_joueur.image, perso_joueur.rect)
                fenetre.blit(my_font2.render(str(perso_joueur.vie), False, (255, 255, 255)), positionpv2)
                fenetre.blit(barrevieperso, (696, pv2))
                fenetre.blit(barrevieperso1, (796 - pourcentagepvjoueur, pv2))



            fenetre.blit(david.image, david.rect)

            fenetre.blit(my_font2.render(str(david.vie), False, (255, 255, 255)), positionpv1)
            fenetre.blit(barrevieperso, (696, pv1))
            fenetre.blit(barrevieperso1, (796 - pourcentagepvdavid, pv1))

        if combat.tour == 3:
            david.rect = position3  # endroit de spawn du perso
            perso_joueur.rect = position2
            sinatra.rect = position1
            if david.alive == True and perso_joueur.alive == True:
                fenetre.blit(david.image, david.rect)
                fenetre.blit(my_font2.render(str(david.vie), False, (255, 255, 255)), positionpv3)
                fenetre.blit(barrevieperso, (696, pv3))
                fenetre.blit(barrevieperso1, (796 - pourcentagepvdavid, pv3))
            if perso_joueur.alive == True:
                fenetre.blit(perso_joueur.image, perso_joueur.rect)
                fenetre.blit(my_font2.render(str(perso_joueur.vie), False, (255, 255, 255)), positionpv2)
                fenetre.blit(barrevieperso, (696, pv2))
                fenetre.blit(barrevieperso1, (796 - pourcentagepvjoueur, pv2))
            elif david.alive == True :
                fenetre.blit(david.image, david.rect)
                fenetre.blit(my_font2.render(str(david.vie), False, (255, 255, 255)), positionpv2)
                fenetre.blit(barrevieperso, (696, pv2))
                fenetre.blit(barrevieperso1, (796 - pourcentagepvdavid, pv2))


            fenetre.blit(sinatra.image, sinatra.rect)

            fenetre.blit(my_font2.render(str(sinatra.vie), False, (255, 255, 255)), positionpv1)
            fenetre.blit(barrevieperso, (696, pv1))
            fenetre.blit(barrevieperso1, (796 - pourcentagepvsinatra, pv1))
        fenetre.blit(enemitipe.image, position_ennemi1)
        if choix == 1:
            fenetre.blit(my_font.render("-", False, (255, 255, 255)), (520, 500))
        elif choix == 2:
            fenetre.blit(my_font.render("-", False, (255, 255, 255)), (520, 520))
        elif choix == 3:
            fenetre.blit(my_font.render("-", False, (255, 255, 255)), (520, 540))
        elif choix == 4:
            fenetre.blit(my_font.render("-", False, (255, 255, 255)), (520, 560))
        pygame.display.flip()

    def affichageanim(self, d):
        fichier = open("save1/map", "r")
        map = fichier.read()
        fichier.close()

        if map == "capitale":
            fond = pygame.image.load("battle/Battlebacks/009-CastleTown01.jpg")
        elif map == "chateau_3F":
            fond = pygame.image.load("battle/Battlebacks/026-Castle02.jpg")
        elif map == "caverne":
            fond = pygame.image.load("battle/Battlebacks/043-Cave01.jpg")
        elif map == "mapdepart":
            fond = pygame.image.load("battle/Battlebacks/005-Beach01.jpg")
        elif "fjord" in map:
            fond = pygame.image.load("battle/Battlebacks/icecave.png").convert_alpha()
        elif map=="village":
            fond = pygame.image.load("battle/Battlebacks/003-Forest01.jpg")
        else:fond = pygame.image.load("battle/Battlebacks/043-Cave01.jpg")
        clock = pygame.time.Clock()
        my_font = pygame.font.SysFont("Calibri", 36)
        bandeaubleue = pygame.image.load("battle/animation/Fightblue.png").convert_alpha()
        bandeaurouge = pygame.image.load("battle/animation/Fightred.png").convert_alpha()
        fouldebeu = pygame.image.load("battle/animation/fireball.png").convert_alpha()
        fouldebeunul = pygame.image.load("battle/animation/fireballkitomb.png").convert_alpha()
        fleche = pygame.image.load("battle/animation/fleche.png").convert_alpha()
        bouclier = pygame.image.load("battle/animation/bouclier.png").convert_alpha()
        damage= pygame.mixer.Sound("son/bruit/Damage2.ogg")
        potion=pygame.mixer.Sound("son/bruit/Heal3.ogg")
        feu = pygame.mixer.Sound("son/bruit/Fire1.ogg")



        i = 0
        fenetre.blit(fond, (0, 0))
        while i < 42:
            for event in pygame.event.get():
                if event.type == QUIT:  # pour pouvoir quitter le jeux
                    closemenu.closemenu(fenetre)
            fenetre.blit(bandeaubleue, (811 - i * 10, 200))
            fenetre.blit(bandeaurouge, (-421 + i * 10, 200))
            i += 1
            clock.tick(60)
            pygame.display.flip()

        i = 0
        while i < 160:
            fenetre.blit(fond, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:  # pour pouvoir quitter le jeux
                    closemenu.closemenu()
            fenetre.blit(bandeaubleue, (390, 200))
            fenetre.blit(bandeaurouge, (-1, 200))
            if combat.anim == 1 or combat.anim == 3 or combat.anim == 6 or combat.anim == 7 or combat.anim == 8:
                if combat.tour == 1:
                    fenetre.blit(perso_joueur.image, (689, 200))
                if combat.tour == 2:
                    fenetre.blit(david.image, (689, 200))
                if combat.tour == 3:
                    fenetre.blit(sinatra.image, (689, 200))
                fenetre.blit(enemitipe.image, (11, 200))
                if i < 80:
                    if combat.anim == 1:
                        fenetre.blit(fouldebeu, (689 - i * 6, 250))
                    elif combat.anim == 3:
                        fenetre.blit(fleche, (689 - i * 6, 250))
                    elif combat.anim == 6:
                        fenetre.blit(manap.imageanim, (640, 250 - i))
                    elif combat.anim == 7:
                        fenetre.blit(soin.imageanim, (640, 250 - i))
                    elif combat.anim == 8:
                        fenetre.blit(resurection.imageanim, (640, 250 - i))
                elif i==80:
                    if combat.anim == 6 or combat.anim == 7 or combat.anim == 8:
                        potion.play()
                    if combat.anim==1:
                        feu.play()

                else:
                    if combat.anim == 6:
                        fenetre.blit(my_font.render("50", 3, (0, 0, 200)), (680, 180))

                    elif combat.anim == 7:
                        fenetre.blit(my_font.render("50", 3, (0, 200, 0)), (680, 180))
                    elif combat.anim == 8:
                        fenetre.blit(my_font.render("Les allié sont en vie", 3, (0, 200, 200)),
                                     (680, 180))
                    else:
                        fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (41, 180))
                        damage.play()
            elif combat.anim == 2:
                fenetre.blit(perso_joueur.image, (689, 200))
                fenetre.blit(enemitipe.image, (11, 200))
                if i < 20:
                    fenetre.blit(fouldebeu, (689 - i * 6, 250))
                else:
                    fenetre.blit(fouldebeunul, (569, 250 + i * 2))
            elif combat.anim == 4:
                fenetre.blit(david.image, (689, 200))
            elif combat.anim == 5:
                fenetre.blit(david.image, (689, 200))
                fenetre.blit(bouclier, (689, 200))

            else:

                if i < 80:
                    if combat.tour == 1:
                        fenetre.blit(perso_joueur.image, (689 - i * 4, 200))
                    if combat.tour == 2:
                        fenetre.blit(david.image, (689 - i * 4, 200))
                    if combat.tour == 3:
                        fenetre.blit(sinatra.image, (689 - i * 4, 200))
                if i==80:
                    damage.play()
                if i > 80:
                    if combat.tour == 1:
                        fenetre.blit(perso_joueur.image2, (289, 200))
                    if combat.tour == 2:
                        fenetre.blit(david.image2, (289, 200))
                    if combat.tour == 3:
                        fenetre.blit(sinatra.image2, (289, 200))
                    fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (41, 180))


            fenetre.blit(enemitipe.image, (11, 200))

            clock.tick(60)
            pygame.display.flip()
            i += 1


class ennemi(pygame.sprite.Sprite):
    def __init__(self, imageperso, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(imageperso).convert_alpha()
        self.rect = self.image.get_rect()
        self.alive = False
        self.viemax=0
        self.vie=0


class loup(ennemi):
    def __init__(self):
        ennemi.__init__(self, "battle/imagebonhomme/ennemi/cerberus.png")

    def attaque(self):
        fennemi.cible()
        if combat.hardcore==True:
            d = randint(30+(perso_joueur.niveau*3), 45+(perso_joueur.niveau*3))
        else:
            d = randint(15+perso_joueur.niveau, 20+perso_joueur.niveau)
        varanim = 0
        if david.taunt > 0:
            david.vie -= (d - david.armure-david.ptbouclier*2)
        elif fennemi.p == 2:
            if not david.immortal:
                david.vie -= (d - david.armure-david.ptbouclier*2)
        elif fennemi.p == 1:
            perso_joueur.vie -= (d - perso_joueur.armure)
        elif fennemi.p == 3:
            if random.random() <= 0.3 + (0.05 * sinatra.ptdodge):
                sinatra.vie -= d
        affichage.affichageanimennemi(d, varanim)
        fennemi.verification()


class bestiole(ennemi):
    def __init__(self):
        ennemi.__init__(self, "battle/mob/Imp.png")

    def attaque(self):
        for i in range(2):
            fennemi.cible()
            if combat.hardcore == True:
                d = randint(40 + (perso_joueur.niveau * 3), 55 + (perso_joueur.niveau * 3))
            else:
                d = randint(20 + perso_joueur.niveau, 25 + perso_joueur.niveau )
            varanim = 0
            if david.taunt > 0:
                david.vie -= (d - david.armure-david.ptbouclier*2)
            elif fennemi.p == 2:
                if not david.immortal:
                    david.vie -= (d - david.armure-david.ptbouclier*2)
            elif fennemi.p == 1:
                perso_joueur.vie -= (d - perso_joueur.armure)
            elif fennemi.p == 3:
                if random.random() <= 0.3 + (0.05 * sinatra.ptdodge):
                    sinatra.vie -= d
            affichage.affichageanimennemi(d, varanim)
            fennemi.verification()


class soldatpt(ennemi):
    def __init__(self):
        ennemi.__init__(self, "battle/mob/soldier.png")

    def attaque(self):
        fennemi.cible()
        if combat.hardcore == True:
            d = randint(300, 400)
        else:
            d = randint(200, 300)
        varanim = 0
        if david.taunt > 0:
            david.vie -= (d - david.armure-david.ptbouclier*2)
        elif fennemi.p == 2:
            if not david.immortal:
                david.vie -= (d - david.armure-david.ptbouclier*2)
        elif fennemi.p == 1:
            perso_joueur.vie -= (d - perso_joueur.armure)
        elif fennemi.p == 3:
            if random.random() <= 0.3 + (0.05 * sinatra.ptdodge):
                sinatra.vie -= d
        affichage.affichageanimennemi(d, varanim)
        fennemi.verification()


class malarich(ennemi):
    def __init__(self):
        ennemi.__init__(self, "battle/mob/darklord.png")
    def attaque(self):
        fennemi.cible()
        u = randint(0, 3)
        varanim = 0


        if u==1 or u==3:
            if combat.hardcore == True:
                if random.random() <= 0.1:
                    d = 150
                elif random.random() <= 0.001:
                    d = 1000
                else:
                    d = randint(90, 100)
            else:
                if random.random() <= 0.1:
                    d = 100
                elif random.random() <= 0.001:
                    d = 1000
                else:
                    d = randint(70, 80)
        elif u == 2:
            if fennemi.p == 2:
                lvie = list(str(david.vie))
            elif fennemi.p == 1:
                lvie = list(str(perso_joueur.vie))
            elif fennemi.p == 3:
                lvie = list(str(sinatra.vie))
            if len(lvie) != 3:
                a=3-len(lvie)
                for i in range(a):
                    lvie.append("0")
            random.shuffle(lvie)

            l = int(lvie[0]) * 100 + int(lvie[1]) * 10 + int(lvie[2])
            if fennemi.p == 2:
                d=david.vie-l
            elif fennemi.p == 1:
                d = perso_joueur.vie - l
            elif fennemi.p == 3:
                d = sinatra.vie - l
            varanim = 2
            print(david.vie,perso_joueur.vie)
        if u == 0:
            if combat.hardcore == True:
                d=40
            else:
                d=20
            varanim = 3
        if varanim==3:
            david.vie -= d
            perso_joueur.vie -= d
            sinatra.vie -= d
        else:
            if david.taunt > 0:
                    if varanim==2:
                        david.vie -= d
                    elif david.armure-david.ptbouclier*2 < d:
                        david.vie -= (d - david.armure-david.ptbouclier*2)
            elif fennemi.p == 2:
                if not david.immortal:
                    if varanim==2:
                        david.vie -= d
                    elif david.armure+david.ptbouclier*2 < d:
                        david.vie -= (d - david.armure-david.ptbouclier*2)

            elif fennemi.p == 1:
                if varanim == 2:
                    perso_joueur.vie -= d
                elif perso_joueur.armure < d:
                    perso_joueur.vie -= (d - perso_joueur.armure)
            elif fennemi.p == 3:
                if varanim==2:
                    sinatra.vie -= d
                elif random.random() <= 0.3 + (0.05 * sinatra.ptdodge):
                    sinatra.vie -= d
        affichage.affichageanimennemi(d, varanim)
        fennemi.verification()


class voleur(ennemi):
    def __init__(self):
        ennemi.__init__(self, "battle/mob/Rogue.png")
        self.poison = 0

    def attaque(self):
        fennemi.cible()
        u = randint(0, 1)
        varanim = 0
        if u == 0 or self.poison>0:
            if combat.hardcore == True:
                d = randint(45 + (perso_joueur.niveau * 3), 60 + (perso_joueur.niveau * 3))
            else:
                d = randint(25 + perso_joueur.niveau, 35 + perso_joueur.niveau)
            if david.taunt > 0:
                david.vie -= (d - david.armure-david.ptbouclier*2)
            elif fennemi.p == 2:
                if not david.immortal:
                    david.vie -= (d - david.armure-david.ptbouclier*2)
            elif fennemi.p == 1:
                perso_joueur.vie -= (d - perso_joueur.armure)
        else:
            d = 0
            varanim=1
            self.poison=3
        affichage.affichageanimennemi(d, varanim)
        if self.poison>0:
            self.poison-=1
            david.vie-=10
            perso_joueur.vie-=10
        fennemi.verification()

class sinatramechante(ennemi):
    def __init__(self):
        ennemi.__init__(self, "battle/imagebonhomme/perso3/perso3armurebase.png")
        self.poison = False
        self.esquive=False

    def attaque(self):
        fennemi.cible()
        u = randint(0, 1)
        varanim = 0
        if u == 0:
            if combat.hardcore == True:
                d = randint(50 + (perso_joueur.niveau * 3), 75 + (perso_joueur.niveau * 3))
            else:
                d = randint(30 + perso_joueur.niveau, 40 + perso_joueur.niveau)
            if david.taunt > 0:
                david.vie -= (d - david.armure-david.ptbouclier*2)
            elif fennemi.p == 2:
                if not david.immortal:
                    david.vie -= (d - david.armure-david.ptbouclier*2)
            elif fennemi.p == 1:
                perso_joueur.vie -= (d - perso_joueur.armure)
        else:
            d = 0
            varanim=1
            if self.poison==False:
                self.poison=True
            else:
                if combat.hardcore == True:
                    d = randint(45 + (perso_joueur.niveau * 3), 70 + (perso_joueur.niveau * 3))
                else:
                    d = randint(25 +perso_joueur.niveau , 35 + perso_joueur.niveau)
                varanim = 0
                if david.taunt > 0:
                    david.vie -= (d - david.armure-david.ptbouclier*2)
                elif fennemi.p == 2:
                    if not david.immortal:
                        david.vie -= (d - david.armure-david.ptbouclier*2)
                elif fennemi.p == 1:
                    perso_joueur.vie -= (d - perso_joueur.armure)
        if self.poison==True:
            david.vie-=10
            perso_joueur.vie-=10

        affichage.affichageanimennemi(d, varanim)
        fennemi.verification()

class hornet(ennemi):
    def __init__(self):
        ennemi.__init__(self, "battle/mob/Hornet.png")

    def attaque(self):
        for i in range(2):
            fennemi.cible()
            if combat.hardcore == True:
                d = randint(35 + (perso_joueur.niveau * 3), 50 + (perso_joueur.niveau * 3))
            else:
                d = randint(15 + perso_joueur.niveau, 20 + perso_joueur.niveau )
            varanim = 0
            if david.taunt > 0:
                david.vie -= (d - david.armure-david.ptbouclier*2)
            elif fennemi.p == 2:
                if not david.immortal:
                    david.vie -= (d - david.armure-david.ptbouclier*2)
            elif fennemi.p == 1:
                perso_joueur.vie -= (d - perso_joueur.armure)
            elif fennemi.p == 3:
                if random.random() <= 0.3 + (0.05 * sinatra.ptdodge):
                    sinatra.vie -= d
            affichage.affichageanimennemi(d, varanim)
            fennemi.verification()

class goddess(ennemi):
    def __init__(self):
        ennemi.__init__(self, "battle/mob/Goddess.png")
        self.malediction=0
        self.soin=1

    def attaque(self):
        varanim=0
        fennemi.cible()
        if self.vie<=1000 and self.soin>0:
            self.vie+=2000
            d=0
            varanim = 5
            sinatra.poison=False
            self.soin-=1
        elif self.malediction==0:
            self.malediction=5
            d=0
            varanim = 4
        elif fennemi.p==2 and david.vie>=david.viemax/2:
            d=david.vie/2
        elif fennemi.p==1 and perso_joueur.vie>=perso_joueur.viemax/2:
            d=perso_joueur.vie/2
        elif fennemi.p==3 and sinatra.vie>=sinatra.viemax/2 :
            d=sinatra.vie/2
        elif david.vie>=david.viemax/2:
            d=david.vie/2
        elif  perso_joueur.vie>=perso_joueur.viemax/2:
            d=perso_joueur.vie/2
        elif sinatra.vie>=sinatra.viemax/2 and sinatra.active :
            d=sinatra.vie/2
        else:
            if combat.hardcore == True:
                if random.random() <= 0.1:
                    d = 200
                elif random.random() <= 0.001:
                    d = 1000
                else:
                    d = randint(120, 150)
            else:
                if random.random() <= 0.1:
                    d = 150
                elif random.random() <= 0.001:
                    d = 1000
                else:
                    d = randint(90, 120)
        if fennemi.p == 2:
            if not david.immortal:
                if david.armure+david.ptbouclier*2 < d:
                    david.vie -= (d - david.armure-david.ptbouclier*2)

        elif fennemi.p == 1:
            if perso_joueur.armure<d:
                perso_joueur.vie -= (d - perso_joueur.armure)

        elif fennemi.p == 3:
            if random.random() <= 0.3 + (0.05 * sinatra.ptdodge):
                sinatra.vie -= d

        affichage.affichageanimennemi(d, varanim)
        fennemi.verification()

fichier = open("menu/quetes/mobmort", "r")
nomennemie = fichier.read()
fichier.close()
perso_joueur = perso1()
david = perso2()
sinatra = perso3()
loup = loup()
goddess=goddess()
soldatpt = soldatpt()
malarich = malarich()
bestiole = bestiole()
hornet = hornet()
voleur = voleur()
sinatramechante=sinatramechante()
base = menu()
objet = menu()
attaque = menu()
soin = sac(1, "battle/animation/nbsoin.png")
resurection = sac(1, "battle/animation/nbresurect.png")
manap = sac(1, "battle/animation/mana.png")
combat = bataille()
enemitipe = ennemi("battle/imagebonhomme/ennemi/cerberus.png")
fennemi = attaqueennemi()
affichage = affichage()
