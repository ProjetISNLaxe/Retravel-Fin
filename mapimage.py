import pygame
from pygame.locals import *
with open("options\\fullscreen", "r") as fullscreen:
    fullscreenread = fullscreen.read()
retravel = pygame.image.load("launcher/retravel_logo.png").convert()

if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else:
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)
class imagemap:
    def __init__(self):
        self.map = {}
        self.map["capitale"] = pygame.image.load("map/capitale/capitale.png").convert_alpha()
        for i in range(785):
            fenetre.fill((0, 0, 0))
            fenetre.blit(retravel, (800 - i, 0))
            pygame.display.flip()
        self.map["capitale_obstacle"] = pygame.image.load("map/capitale/capitale_obstacle.png").convert_alpha()

        self.map["mapdepart"] = pygame.image.load("map/mapdepart/mapdepart.png").convert_alpha()
        self.map["mapdepart_obstacle"] = pygame.image.load("map/mapdepart/mapdepart_obstacle.png").convert_alpha()

        self.map["maison_1"] = pygame.image.load("map/maison_1/maison_1.png").convert_alpha()
        self.map["maison_1_obstacle"] = pygame.image.load("map/maison_1/maison_1_obstacle.png").convert_alpha()

        self.map["maison_2"] = pygame.image.load("map/maison_2/maison_2.png").convert_alpha()
        self.map["maison_2_obstacle"] = pygame.image.load("map/maison_2/maison_2_obstacle.png").convert_alpha()

        self.map["ecurie"] = pygame.image.load("map/ecurie/ecurie.png").convert_alpha()
        self.map["ecurie_obstacle"] = pygame.image.load("map/ecurie/ecurie_obstacle.png").convert_alpha()

        self.map["auberge_1F"] = pygame.image.load("map/auberge_1F/auberge_1F.png").convert_alpha()
        self.map["auberge_1F_obstacle"] = pygame.image.load("map/auberge_1F/auberge_1F_obstacle.png").convert_alpha()

        self.map["auberge_2F"] = pygame.image.load("map/auberge_2F/auberge_2F.png").convert_alpha()
        self.map["auberge_2F_obstacle"] = pygame.image.load("map/auberge_2F/auberge_2F_obstacle.png").convert_alpha()

        self.map["cheminfjord"] = pygame.image.load("map/cheminfjord/cheminfjord.png").convert_alpha()
        self.map["cheminfjord_obstacle"] = pygame.image.load("map/cheminfjord/cheminfjord_obstacle.png").convert_alpha()

        self.map["chateau_1F"] = pygame.image.load("map/chateau_1F/chateau_1F.png").convert_alpha()
        self.map["chateau_1F_obstacle"] = pygame.image.load("map/chateau_1F/chateau_1F_obstacle.png").convert_alpha()

        self.map["chateau_2F"] = pygame.image.load("map/chateau_2F/chateau_2F.png").convert_alpha()
        self.map["chateau_2F_obstacle"] = pygame.image.load("map/chateau_2F/chateau_2F_obstacle.png").convert_alpha()

        self.map["chateau_3F"] = pygame.image.load("map/chateau_3F/chateau_3F.png").convert_alpha()
        self.map["chateau_3F_obstacle"] = pygame.image.load("map/chateau_3F/chateau_3F_obstacle.png").convert_alpha()

        self.map["village"] = pygame.image.load("map/village/village.png").convert_alpha()
        self.map["village_obstacle"] = pygame.image.load("map/village/village_obstacle.png").convert_alpha()

        self.map["manoir"] = pygame.image.load("map/manoir/manoir.png").convert_alpha()
        self.map["manoir_obstacle"] = pygame.image.load("map/manoir/manoir_obstacle.png").convert_alpha()

        self.map["maison_1village"] = pygame.image.load("map/maison_1village/maison_1village.png").convert_alpha()
        self.map["maison_1village_obstacle"] = pygame.image.load("map/maison_1village/maison_1village_obstacle.png").convert_alpha()

        self.map["shop_potion"] = pygame.image.load("map/shop_potion/shop_potion.png").convert_alpha()
        self.map["shop_potion_obstacle"] = pygame.image.load("map/shop_potion/shop_potion_obstacle.png").convert_alpha()

imagemaps = imagemap()
