import pygame

interfaceinvent = pygame.image.load("menu/inventory/interface_inventaire_objets.png").convert_alpha()
ouverture = pygame.mixer.Sound("son/Sound/Menu_Open.wav")
fermeture = pygame.mixer.Sound("son/Sound/Menu_Close.wav")
sounditem = pygame.mixer.Sound("son/Sound/Item_1.wav")
emplacementperso0 = pygame.image.load("menu/inventory/emplacementperso0.png").convert_alpha()
emplacementperso1 = pygame.image.load("menu/inventory/emplacementperso1.png").convert_alpha()
emplacementperso2 = pygame.image.load("menu/inventory/emplacementperso2.png").convert_alpha()
perso0 = pygame.image.load("perso/N-Ship/F1.png").convert_alpha()

stuff_actuel_1 = pygame.image.load("menu/inventory/stuff_actuel.png").convert_alpha()

stuff_actuel_2 = pygame.image.load("menu/inventory/stuff_actuel_2.png").convert_alpha()
curseur = pygame.image.load("menu/inventory/curseur.png").convert_alpha()
test = pygame.image.load("launcher/pixelgitan.png").convert_alpha()
testrect = test.get_rect()
curseurrect = curseur.get_rect()
testmask = pygame.mask.from_surface(test)
curseurmask = pygame.mask.from_surface(curseur)

police = pygame.font.SysFont("monospace", 15)
objetinventairerect = []
listechiffre = []
taillechiffre = []
for i in range(10):
    listechiffre.append(pygame.image.load("menu/inventory/chiffre/chiffre0" + str(i) + ".png").convert_alpha())
    taillechiffre.append(listechiffre[i].get_size())
consommable = ["pomme", "nbsoin", "mana", "nbresurect"]

ongletli = []
for i in range(3):
    ongletli.append(pygame.image.load("menu/inventory/onglet" + str(i) + ".png").convert_alpha())
onglet = ongletli[0]
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(alphabet)
inventaireimage = pygame.image.load("menu/inventory/objetinventaire.png").convert_alpha()
portionvie = pygame.image.load("menu/inventory/portionvie.png").convert_alpha()
portionxp = pygame.image.load("menu/inventory/portionxp.png").convert_alpha()
listechiffre_miniature = []
for i in range(10):
    listechiffre_miniature.append(
        pygame.image.load("menu/inventory/chiffre_miniature/" + str(i) + ".png").convert_alpha())

slash = pygame.image.load("menu/inventory/chiffre_miniature/slash.png").convert_alpha()

# FENETRE VOYAGE

boitevoyage = pygame.image.load("menu/voyage/boite.png").convert_alpha()
boutonfjordglas = pygame.image.load("menu/voyage/fjordglas.png").convert_alpha()
boutonfjordglasmask = pygame.mask.from_surface(boutonfjordglas)
boutonchateau = pygame.image.load("menu/voyage/chateau.png").convert_alpha()
boutonchateaumask= pygame.mask.from_surface(boutonchateau)
boutonvillage = pygame.image.load("menu/voyage/villageforestier.png").convert_alpha()
boutonvillagemask = pygame.mask.from_surface(boutonvillage)

#FENETRE ESCAPE
boitescape = pygame.image.load("menu/escape/boite.png").convert_alpha()
boutonmenuprincipal=pygame.image.load("menu/escape/boutonmenuprincipal.png").convert_alpha()
boutonmenumask=pygame.mask.from_surface(boutonmenuprincipal)
boutonquitter = pygame.image.load("menu/escape/boutonquitter.png").convert_alpha()
boutonquittermask=pygame.mask.from_surface(boutonquitter)
boutonaide= pygame.image.load("menu/escape/boutonaide.png").convert_alpha()
boutonaidemask=pygame.mask.from_surface(boutonaide)#Les boutons ont le même mask

#FENETRE ENDLESS
boiterunner = pygame.image.load("Endless/boite.png").convert_alpha()
boutonshooter=pygame.image.load("Endless/boutonshooter.png").convert_alpha()
boutonshootermask=pygame.mask.from_surface(boutonshooter)
boutonrunner = pygame.image.load("Endless/boutonrunner.png").convert_alpha()
boutonrunnerlock = pygame.image.load("Endless/boutonrunnerlock.png").convert_alpha()
boutonrunnermask=pygame.mask.from_surface(boutonrunner)
boutonRPG= pygame.image.load("Endless/boutonRPG.png").convert_alpha()
boutonRPGlock= pygame.image.load("Endless/boutonRPGlock.png").convert_alpha()
boutonRPGmask=pygame.mask.from_surface(boutonRPG)#Les boutons ont le même mask

#FENETRE AIDE
boutontutoriel=pygame.image.load("menu/escape/boutontutoriel.png").convert_alpha()
boutontutorielmask=pygame.mask.from_surface(boutontutoriel)
boutonquete=pygame.image.load("menu/escape/boutonquete.png").convert_alpha()
boutonquetemask=pygame.mask.from_surface(boutonquete)
boutonunstuck=pygame.image.load("menu/escape/boutonunstuck.png").convert_alpha()
boutonunstuckmask=pygame.mask.from_surface(boutonunstuck)
