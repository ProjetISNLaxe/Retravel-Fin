import pygame, sys, quete, time
from pygame.locals import *
from classes.perso_classes import *
from classes.classes_tpt import *
import menu.closemenu as closemenu, menu.printinvent as printinvent, menu.dialogue as dialogue, menu.shop as shop
import battle.combatV3
import classes.classes_map as classes_map
from math import sqrt
import escapemenu
from battle.save import chargementsauvegarde
from menu.imageinterfacetoload import police
from mapimage import imagemaps

with open("options\\fullscreen", "r") as fullscreen:
    fullscreenread = fullscreen.read()

if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else:
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)

def verificationniveau():
    if david.xp >= 50 * david.niveau:
        david.xp -= 50 * david.niveau
        david.niveau += 1
        david.ptdecompetance += 1
    if sinatra.xp >= 50 * sinatra.niveau:
        sinatra.xp -= 50 * sinatra.niveau
        sinatra.niveau += 1
        sinatra.ptdecompetance += 1
    if perso_joueur.xp >= 50 * perso_joueur.niveau:
        perso_joueur.xp -= 50 * perso_joueur.niveau
        perso_joueur.niveau += 1
        perso_joueur.ptdecompetance += 1



def selecmap():
    """Selection de la map active"""
    pygame.mixer.init()
    chargementsauvegarde()
    pygame.mixer.music.load("son/Sound/day.mp3")
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play(-1)
    chargement()
    with open("save1/map", "r") as fichier:
        mapactive = fichier.read()
    if mapactive == "capitale":
        capitale()
    if mapactive == "maison_1":
        maison_1()
    if mapactive == "maison_2":
        maison_2()
    if mapactive == "auberge_1F":
        auberge_1F()
    if mapactive == "auberge_2F":
        auberge_2F()
    if mapactive == "shop_potion":
        shop_potion()
    if mapactive == "chateau_1F":
        chateau_1F()
    if mapactive == "chateau_2F":
        chateau_2F()
    if mapactive == "chateau_3F":
        chateau_3F()
    if mapactive == "mapdepart":
        mapdepart()
    if mapactive == "cheminfjord":
        cheminfjord()
    if mapactive == "fjordglasrdc":
        fjordglasrdc()
    if mapactive == "fjordglas-1":
        fjordglas_1()
    if mapactive == "fjordglas1":
        fjordglas1()
    if mapactive == "ecurie":
        ecurie()
    if mapactive == "village":
        village()
    if mapactive == "manoir":
        manoir()
    if mapactive == "maison_1village":
        maison_1village()
    if mapactive == "guilde-1":
        guilde_1()
    if mapactive == "guilde-2":
        guilde_2()
    if mapactive == "butin":
        butin()


def chargement():
    global capitaleload
    capitaleload = False
    global auberge_1Fload
    auberge_1Fload = False
    global chateau_1Fload
    chateau_1Fload = False
    global chateau_2Fload
    chateau_2Fload = False
    global cheminfjordload
    cheminfjordload = False
    global fjordglasrdcload
    fjordglasrdcload = False
    global villageload
    villageload = True


def capitale():
    with open("save1/activation/perso3", "r") as perso3:
        perso3 = bool(int(perso3.read()))
    if not perso3:
        fichier = open("menu/quetes/mobmort", "w")
        fichier.write("voleur")
        fichier.close()
    else:
        fichier = open("menu/quetes/mobmort", "w")
        fichier.write("")
        fichier.close()
    global capitaleload
    capitaleload = True
    quete.quetes()
    with open("save1/tuto", "r") as tuto:
        tuto = bool(int(tuto.read()))
    mapcl = classes_map.classmapbasique("capitale")
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("capitale")
    persof.close()
    rectpersoactif = str("save1/pospeso/pospesocapitale")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    testtime = time.time()
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    with open("menu/quetes/jeanma/vol", "r") as jeanmavol:
        jeanmavol=bool(int(jeanmavol.read()))
    with open("menu/quetes/jeanma/diamaison_2", "r") as diamaison2:
        diamaison2 = bool(int(diamaison2.read()))
    if diamaison2 and not jeanmavol:
        volencour=True
        jeanma=David()
        jeanma.rect.x = 1539
        jeanma.rect.y = 3133
        rogue=Rogue()
    else:volencour=False
    jeanmapuit = False
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesocapitale", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapcapitale", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesocapitale", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapcapitale", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesocapitale", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapcapitale", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()

        mapcl.interaction(perso, fenetre)
        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(imagemaps.map["transi"+mapcl.name])):
                if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(imagemaps.map["transi"+mapcl.name][i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesocapitale", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapcapitale", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("menu/quetes/visitelieu", "w")
                    litransifi.write(imagemaps.map["transi"+mapcl.name][i])
                    litransifi.close()
                    quete.quetes()
                    if imagemaps.map["transi"+mapcl.name][i] == "maison_1":
                        maison_1()
                        testtime = time.time()
                        break
                    if imagemaps.map["transi"+mapcl.name][i] == "maison_2":
                        maison_2()
                        testtime = time.time()
                        break
                    if imagemaps.map["transi"+mapcl.name][i] == "auberge_1F":
                        auberge_1F()
                        testtime = time.time()
                        break
                    if imagemaps.map["transi"+mapcl.name][i] == "chateau_1F":
                        chateau_1F()
                        testtime = time.time()
                        break
                    if imagemaps.map["transi"+mapcl.name][i] == "ecurie":
                        ecurie()
                        testtime = time.time()
                        break
                    if imagemaps.map["transi"+mapcl.name][i] == "shop_potion":
                        shop_potion()
                        testtime = time.time()
                        break
                    if imagemaps.map["transi"+mapcl.name][i] == "guilde-1":
                        guilde_1()
                        testtime = time.time()
                        break
        mapcl.affichage(fenetre, perso)
        if not tuto:
            dialogue.jeanmadia("Appuie sur I pour ouvrir l'inventaire","valider", "aide")
            dialogue.jeanmadia("Dans l'inventaire appui sur Tab pour l'arbre de compétance","valider", "aide")
            dialogue.jeanmadia("Quand tu croise un pnj, appuie sur F pour interagir","valider", "aide")
            dialogue.jeanmadia("Appuie sur E sur une porte ouverte pour y rentrer","valider", "aide")
            dialogue.jeanmadia("Tu peux aller à l'écurie pour voyager vers des contrées lointaines","valider", "aide")
            dialogue.jeanmadia("Tu peux aller à la boutique de potion si tu n'en a plus", "valider", "aide")
            tuto=True
            with open("save1/tuto", "w") as tutowr:
                tutowr.write("1")
        if volencour:
            jeanma.move3()
            rogue.move()
            fenetre.blit(jeanma.image, (jeanma.rect.x + mapcl.rect.x, jeanma.rect.y + mapcl.rect.y))
            fenetre.blit(rogue.image, (rogue.rect.x + mapcl.rect.x, rogue.rect.y + mapcl.rect.y))
            with open("menu/quetes/jeanma/vol", "r") as jeanmavol:
                jeanmavol = bool(int(jeanmavol.read()))
            if jeanmavol :
                volencour=False
                dialogue.jeanmadia("On m'a volé ! Retrouvons le voleur")
                jeanmapuit=True
                jeanma.rect.x=1119
                jeanma.rect.y=4409
        if jeanmapuit:
            fenetre.blit(jeanma.image, (jeanma.rect.x + mapcl.rect.x, jeanma.rect.y + mapcl.rect.y))
            dist = sqrt((jeanma.rect.x + mapcl.rect.x - perso.rect.x) ** 2 + ( jeanma.rect.y + mapcl.rect.y - perso.rect.y) ** 2)
            if dist < 20:
                dialogue.jeanmadia("Il est rentré par ce puit !", "suivant")
                jeanmapuit=False

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def maison_1():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("maison_1")
    persof.close()
    quete.quetes()
    mapcl = classes_map.classmapbasique("maison_1")
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesomaison_1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapmaison_1", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesomaison_1", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmaison_1", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesomaison_1", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapmaison_1", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        if tkey[K_e]:
            for i in range(len(imagemaps.map["transi"+mapcl.name])):
                if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    with open("save1/map", "w") as maptransi:
                        maptransi.write(imagemaps.map["transi"+mapcl.name][i])
                    with open("save1/pospeso/pospesomaison_1", "w") as pospeso:
                        pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    with open("save1/posmap/posmapmaison_1", "w") as posmap:
                        posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    quete.quetes()
                    fenetre.fill((0, 0, 0))
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    global capitaleload
                    if imagemaps.map["transi"+mapcl.name][i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale()
        mapcl.affichage(fenetre, perso)

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def maison_2():
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    quete.quetes()
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    mapcl = classes_map.classmapbasique("maison_2")
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("maison_2")
    persof.close()

    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    with open("save1/histoire/gardes", "r") as gardesverif:
        gardesverif = bool(int(gardesverif.read()))
    with open("menu/quetes/jeanma/diamaison_2", "r") as diamaison2:
        diamaison2 = bool(int(diamaison2.read()))
    if gardesverif and not diamaison2:
        jeanma2=True
        jeanma=David()
        jeanma.rect.x = 779
        jeanma.rect.y = 300
        jeanmadia=True
    else: jeanma2 = False

    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesomaison_2", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapmaison_2", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesomaison_2", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmaison_2", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesomaison_2", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapmaison_2", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        if tkey[K_e]:
            for i in range(len(imagemaps.map["transi"+mapcl.name])):
                if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask,
                                               (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(imagemaps.map["transi"+mapcl.name][i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesomaison_2", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmaison_2", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("menu/quetes/visitelieu", "w")
                    litransifi.write(imagemaps.map["transi"+mapcl.name][i])
                    litransifi.close()
                    quete.quetes()
                    global capitaleload
                    if imagemaps.map["transi"+mapcl.name][i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale()
        mapcl.affichage(fenetre, perso)
        if jeanma2:
            if jeanmadia==True:
                fenetre.blit(jeanma.image, (jeanma.rect.x + mapcl.rect.x, jeanma.rect.y + mapcl.rect.y))
                dialogue.jeanmadia("Il faut chercher de l'aide")
                jeanmadia=False
            jeanma.move2()
            fenetre.blit(jeanma.image, (jeanma.rect.x + mapcl.rect.x, jeanma.rect.y + mapcl.rect.y))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def auberge_1F():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    global auberge_1Fload
    auberge_1Fload = True
    quete.quetes()
    mapcl = classes_map.classmapbasique("auberge_1F")
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    testtime = time.time()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("auberge_1F")
    persof.close()
    affichetext = False
    myfont = pygame.font.SysFont("monospace", 20)
    rectpersoactif = str("save1/pospeso/pospesoauberge_1F")
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    onstairs = True
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesoauberge_1F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapauberge_1F", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesoauberge_1F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapauberge_1F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesoauberge_1F", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapauberge_1F", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        for i in range(len(mapcl.pnjli)):
            if mapcl.maskpnj[i].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                affichetext = True
            else:
                affichetext = False
        if tkey[K_e] and time.time() - testtime > 0.5:

            if imagemaps.map["transi"+mapcl.name+"mask"][0].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                maptransi = open("save1/map", "w")
                maptransi.write(imagemaps.map["transi"+mapcl.name][0])
                maptransi.close()
                pospeso = open("save1/pospeso/pospesoauberge_1F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapauberge_1F", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                litransifi = open("menu/quetes/visitelieu", "w")
                litransifi.write(imagemaps.map["transi"+mapcl.name][0])
                litransifi.close()
                quete.quetes()
                global capitaleload
                if capitaleload:
                    return
                    break
                else:
                    capitale()
                    break
        if imagemaps.map["transi"+mapcl.name+"mask"][1].overlap(perso.mask,
                                       (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and not onstairs:
            maptransi = open("save1/map", "w")
            maptransi.write("auberge_2F")
            maptransi.close()
            pospeso = open("save1/pospeso/pospesoauberge_1F", "w")
            pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
            pospeso.close()
            posmap = open("save1/posmap/posmapauberge_1F", "w")
            posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
            posmap.close()
            fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
            pygame.display.flip()
            litransifi = open("menu/quetes/visitelieu", "w")
            litransifi.write("auberge_2F")
            litransifi.close()
            auberge_2F()
            onstairs = True
        elif not imagemaps.map["transi"+mapcl.name+"mask"][1].overlap(perso.mask,
                                             (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and onstairs:
            onstairs = False
        mapcl.affichage(fenetre, perso)

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def auberge_2F():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    quete.quetes()
    mapcl = classes_map.classmapbasique("auberge_2F")
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("auberge_2F")
    persof.close()
    rectpersoactif = str("save1/pospeso/pospesoauberge_2F")
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    onstairs = True
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesoauberge_2F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapauberge_2F", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesoauberge_2F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapauberge_2F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesoauberge_2F", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapauberge_2F", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        mapcl.affichage(fenetre, perso)
        if imagemaps.map["transi"+mapcl.name+"mask"][0].overlap(perso.mask,
                                       (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and not onstairs:
            maptransi = open("save1/map", "w")
            maptransi.write("auberge_1F")
            maptransi.close()
            pospeso = open("save1/pospeso/pospesoauberge_2F", "w")
            pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
            pospeso.close()
            posmap = open("save1/posmap/posmapauberge_2F", "w")
            posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
            posmap.close()
            fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
            pygame.display.flip()
            litransifi = open("menu/quetes/visitelieu", "w")
            litransifi.write("auberge_1F")
            litransifi.close()
            global auberge_1Fload
            if not auberge_1Fload:
                auberge_1F()
                onstairs = True
            else:
                return
        elif not imagemaps.map["transi"+mapcl.name+"mask"][0].overlap(perso.mask,
                                             (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and onstairs:
            onstairs = False

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def chateau_1F():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    global chateau_1Fload
    chateau_1Fload = True
    quete.quetes()
    mapcl = classes_map.classmapbasique("chateau_1F")
    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("chateau_1F")
    persof.close()

    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()

    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesochateau_1F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapchateau_1F", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesochateau_1F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_1F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesochateau_1F", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapchateau_1F", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        mapcl.affichage(fenetre, perso)

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(imagemaps.map["transi"+mapcl.name])):
                if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask,
                                               (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(imagemaps.map["transi"+mapcl.name][i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesochateau_1F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_1F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    quete.quetes()
                    global capitaleload
                    if imagemaps.map["transi"+mapcl.name][i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale()
                    if imagemaps.map["transi"+mapcl.name][i] == "chateau_2F":
                        chateau_2F()
                        testtime = time.time()
                        break

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def chateau_2F():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    global chateau_2Fload
    chateau_2Fload = True
    quete.quetes()
    mapcl = classes_map.classmapbasique("chateau_2F")
    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("chateau_2F")
    persof.close()

    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()

    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesochateau_2F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapchateau_2F", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesochateau_2F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_2F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesochateau_2F", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapchateau_2F", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        mapcl.affichage(fenetre, perso)

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(imagemaps.map["transi"+mapcl.name])):
                if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask,
                                               (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(imagemaps.map["transi"+mapcl.name][i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesochateau_2F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_2F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    quete.quetes()
                    global chateau_1Fload
                    if imagemaps.map["transi"+mapcl.name][i] == "chateau_1F":
                        if chateau_1Fload:
                            return
                        else:
                            chateau_1F()
                    if imagemaps.map["transi"+mapcl.name][i] == "chateau_3F":
                        chateau_3F()
                        testtime = time.time()
                        break

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def chateau_3F():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    quete.quetes()
    mapcl = classes_map.classmapbasique("chateau_3F")
    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("chateau_3F")
    persof.close()

    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()

    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesochateau_3F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapchateau_3F", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesochateau_3F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_3F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesochateau_3F", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapchateau_3F", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        mapcl.affichage(fenetre, perso)

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(imagemaps.map["transi"+mapcl.name])):
                if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask,
                                               (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(imagemaps.map["transi"+mapcl.name][i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesochateau_3F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapchateau_3F", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    quete.quetes()
                    global chateau_2Fload
                    if imagemaps.map["transi"+mapcl.name][i] == "chateau_2F":
                        if chateau_2Fload:
                            return
                        else:
                            chateau_2F()

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def mapdepart():

    global mapdepartload
    mapdepartload = True
    jeanmacl = David()
    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    quete.quetes()
    mapcl = classes_map.classmapbasique("mapdepart")
    image_ship = pygame.image.load("map/mapdepart/mapdepart_ship.png").convert_alpha()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("mapdepart")
    persof.close()
    jeanmafi = open("menu/quetes/jeanma/jeanma", "r")
    jeanma = bool(int(jeanmafi.read()))
    jeanmafi.close()
    speakalone=True
    imagemob = pygame.image.load("map/mapdepart/mapdepart_loup.png")
    maskmob = pygame.mask.from_surface(imagemob)

    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    fondu = pygame.Surface((800, 600))
    fondu.set_alpha(0)
    fondu.fill((255, 255, 255))
    for i in range(255):
        fenetre.blit(fondu, (0, 0))
        fondu.set_alpha(255-i)
        pygame.display.flip()
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesomapdepart", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapmapdepart", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesomapdepart", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmapdepart", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesomapdepart", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapmapdepart", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        mapcl.affichage(fenetre, perso)
        fenetre.blit(jeanmacl.image, (jeanmacl.rect.x + mapcl.rect.x, jeanmacl.rect.y + mapcl.rect.y))
        transf = open("save1/histoire/transibateau", "r")
        transitionre = bool(int(transf.read()))
        transf.read()
        if transitionre:
            jeanmacl.move()
            fenetre.blit(image_ship, mapcl.rect)
        loupfi = open("menu/quetes/jeanma/loup", "r")
        loup = bool(int(loupfi.read()))
        loupfi.close()
        if not loup:
            fenetre.blit(imagemob, mapcl.rect)
        if tkey[K_f]:
            if maskmob.overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                mobfi = open("menu/quetes/mobmort", "w")
                mobfi.write("loup")
                mobfi.close()
                quete.quetes()
        dist=sqrt((jeanmacl.rect.x + mapcl.rect.x-perso.rect.x)**2+(jeanmacl.rect.y + mapcl.rect.y-perso.rect.y)**2)
        if dist<400 and not jeanma:
            dialogue.jeanmadia("A l'aide !!!", "suivant")
            dialogue.jeanmadia("Appuez sur F quand vous étes près du loup", "valider", "aide")
            jeanmafi = open("menu/quetes/jeanma/jeanma", "w")
            jeanmafi.write("1")
            jeanmafi.close()
            jeanma=True


        if tkey[K_e] and time.time() - testtime > 0.5:
            if transitionre and imagemaps.map["transi"+mapcl.name+"mask"][0].overlap(perso.mask,
                                                            (perso.rect.x - mapcl.rect.x,
                                                             perso.rect.y - mapcl.rect.y)):
                maptransi = open("save1/map", "w")
                maptransi.write("capitale")
                maptransi.close()
                pospeso = open("save1/pospeso/pospesomapdepart", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapmapdepart", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                fenetre.fill((0,0,0))
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                litransifi = open("menu/quetes/visitelieu", "w")
                litransifi.write("capitale")
                litransifi.close()
                quete.quetes()
                global capitaleload

                if capitaleload:
                    return
                else:
                    capitale()

        if speakalone:
            dialogue.jeanmadia("Qu'est-ce qui m'est arrivé ?", "suivant", "joueur")
            dialogue.jeanmadia("Est-ce que je rève ?...", "suivant", "joueur")
            dialogue.jeanmadia("Où suis-je ?", "suivant", "joueur")
            dialogue.jeanmadia("Quelles sont ces voix ?", "suivant", "joueur")
            dialogue.jeanmadia("Visitons les lieux...", "retour", "joueur")
            dialogue.jeanmadia("Appuyez sur les flèches directionelles pour vous déplacer", "valider", "aide")
            speakalone=False

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def cheminfjord():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    global cheminfjordload
    cheminfjordload = True
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("cheminfjord")
    persof.close()
    quete.quetes()
    mapcl = classes_map.classmapbasique("cheminfjord")
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    with open("save1/activation/perso3") as passage:
        passage=bool(int(passage.read()))
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesocheminfjord", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapcheminfjord", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesocheminfjord", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapcheminfjord", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesocheminfjord", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapcheminfjord", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        if tkey[K_e]:

            if imagemaps.map["transi"+mapcl.name+"mask"][0].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(imagemaps.map["transi"+mapcl.name][0])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesocheminfjord", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapcheminfjord", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    quete.quetes()
                    fenetre.fill((0, 0, 0))
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    if imagemaps.map["transi"+mapcl.name][0] == "ecurie":
                        ecurie()
            if imagemaps.map["transi"+mapcl.name+"mask"][1].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and passage:
                maptransi = open("save1/map", "w")
                maptransi.write(imagemaps.map["transi"+mapcl.name][1])
                maptransi.close()
                pospeso = open("save1/pospeso/pospesocheminfjord", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapcheminfjord", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                quete.quetes()
                fenetre.fill((0, 0, 0))
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                if imagemaps.map["transi"+mapcl.name][1] == "fjordglasrdc":
                    fjordglasrdc()

        mapcl.affichage(fenetre, perso)

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def fjordglasrdc():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("bestiole")
    fichier.close()
    myfont = pygame.font.SysFont("monospace", 20)
    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("map/fjordglasrdc/fjordglasrdc.png").convert_alpha()
    image_obstacles = pygame.image.load("map/fjordglasrdc/fjordglasrdc_obstacle.png").convert_alpha()
    image_dessus = pygame.image.load("map/fjordglasrdc/fjordglasrdc_dessus.png").convert_alpha()
    position = image.get_rect()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("fjordglasrdc")
    persof.close()
    mapactives = str("save1/posmap/posmapfjordglasrdc")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    lirect = carect.split(",")
    if carect == "":
        mapactives = str("map/fjordglasrdc/spawnfjordglasrdc")
        rectf = open(mapactives, "r")
        carect = rectf.read().split(";")
        rectf.close()
        lirect = carect[0].split(",")

    position.x = int(lirect[0])
    position.y = int(lirect[1])
    glace = pygame.image.load("map/fjordglasrdc/glace.png").convert_alpha()
    glacemask = pygame.mask.from_surface(glace)
    rectpersoactif = str("save1/pospeso/pospesofjordglasrdc")
    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("map/fjordglasrdc/transifjordglasrdc", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("map/fjordglasrdc/fjordglasrdc_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.load("son/Sound/fjordglas.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)
    escape=escapemenu.escape()
    onstairs = True

    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesofjordglasrdc", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapfjordglasrdc", "r") as posmap:
                        posmap = posmap.read().split(",")
                    position.x = int(posmap[0])
                    position.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1

        if not perso.mask.overlap(glacemask, (position.x - perso.rect.x, position.y - perso.rect.y)):
            perso.glissright = False
            perso.glissleft = False
            perso.glisstop = False
            perso.glissdown = False
            perso.eventkey(position, masque, taille)
        else:
            perso.glisse(position, masque, taille)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False
        fenetre.blit(image, position)
        fenetre.blit(perso.imageperso, perso.rect)
        fenetre.blit(image_dessus, position)

        if tkey[K_e] and time.time() - testtime > 0.5:

            if masktransi[0].overlap(perso.mask,
                                     (perso.rect.x - position.x, perso.rect.y - position.y)):
                maptransi = open("save1/map", "w")
                maptransi.write(transili[i])
                maptransi.close()
                pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                litransifi = open("menu/quetes/visitelieu", "w")
                litransifi.write(transili[i])
                litransifi.close()
                quete.quetes()
                global cheminfjordload
                pygame.mixer.music.load("son/Sound/day.mp3")
                pygame.mixer.music.play(-1)
                cheminfjord()
        for i in range(1, 5):
            if masktransi[i].overlap(perso.mask,
                                     (perso.rect.x - position.x, perso.rect.y - position.y)) and not onstairs:

                pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                if i == 1:
                    maptransi = open("save1/map", "w")
                    maptransi.write("fjordglas-1")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesofjordglas-1", "w")
                    pospeso.write("398,272")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglas-1", "w")
                    posmap.write("-432,-172")
                    posmap.close()
                    fjordglas_1()
                if i == 2:
                    maptransi = open("save1/map", "w")
                    maptransi.write("fjordglas-1")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesofjordglas-1", "w")
                    pospeso.write("396,207")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglas-1", "w")
                    posmap.write("-288,-616")
                    posmap.close()
                    fjordglas_1()
                if i == 3:
                    maptransi = open("save1/map", "w")
                    maptransi.write("fjordglas1")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesofjordglas1", "w")
                    pospeso.write("394,258")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglas1", "w")
                    posmap.write("-531,-470")
                    posmap.close()
                    fjordglas1()
                if i == 4:
                    maptransi = open("save1/map", "w")
                    maptransi.write("fjordglas1")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesofjordglas1", "w")
                    pospeso.write("399,200")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglas1", "w")
                    posmap.write("-339,-1091")
                    posmap.close()
                    fjordglas1()

                onstairs = True

            elif not masktransi[1].overlap(perso.mask,
                                           (perso.rect.x - position.x, perso.rect.y - position.y)) and onstairs:
                onstairs = False

        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def fjordglas_1():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("bestiole")
    fichier.close()

    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()

    perso = persobase("fjordglas-1")
    mapcl = classes_map.classmapbasique("fjordglas-1")
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    onstairs = True
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesofjordglas-1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglas-1", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesofjordglas-1", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglas-1", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesofjordglas-1", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapfjordglas-1", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1

        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)

        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        mapcl.affichage(fenetre, perso)

        for i in range(2):
            if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask,
                                     (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and not onstairs:
                maptransi = open("save1/map", "w")
                maptransi.write("fjordglasrdc")
                maptransi.close()
                pospeso = open("save1/pospeso/pospesofjordglas-1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglas-1", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                litransifi = open("menu/quetes/visitelieu", "w")
                litransifi.write("fjordglasrdc")
                litransifi.close()
                quete.quetes()
                if i == 0:
                    pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                    pospeso.write("408,309")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                    posmap.write("-315,-180")
                    posmap.close()
                if i == 1:
                    pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                    pospeso.write("397,200")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                    posmap.write("-288,-635")
                    posmap.close()
                fjordglasrdc()
                onstairs = True


            elif not imagemaps.map["transi"+mapcl.name+"mask"][0].overlap(perso.mask,
                                           (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and onstairs:
                onstairs = False

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def fjordglas1():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("bestiole")
    fichier.close()

    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("map/fjordglas1/fjordglas1.png").convert_alpha()
    image_obstacles = pygame.image.load("map/fjordglas1/fjordglas1_obstacle.png").convert_alpha()
    # image_dessus = pygame.image.load("map/fjordglas1/fjordglas1_dessus.png").convert_alpha()
    position = image.get_rect()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("fjordglas1")
    persof.close()
    mapactives = str("save1/posmap/posmapfjordglas1")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    lirect = carect.split(",")
    if carect == "":
        mapactives = str("map/fjordglas1/spawnfjordglas1")
        rectf = open(mapactives, "r")
        carect = rectf.read().split(";")
        rectf.close()
        lirect = carect[0].split(",")

    position.x = int(lirect[0])
    position.y = int(lirect[1])
    rectpersoactif = str("save1/pospeso/pospesofjordglas1")
    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()
    malarich = pygame.image.load("map/fjordglas1/malarich.png").convert_alpha()
    malarichmask = pygame.mask.from_surface(malarich)
    transi = open("map/fjordglas1/transifjordglas1", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("map/fjordglas1/fjordglas1_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    onstairs = True
    with open("save1/histoire/malarich", "r") as malarichfi:
        malarichwin = bool(int(malarichfi.read()))
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesofjordglas1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglas1", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesofjordglas1", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglas1", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesofjordglas1", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapfjordglas1", "r") as posmap:
                        posmap = posmap.read().split(",")
                    position.x = int(posmap[0])
                    position.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1

        perso.eventkey(position, masque, taille)

        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1/invent/cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)
        fenetre.blit(perso.imageperso, perso.rect)
        if not malarichwin:
            fenetre.blit(malarich, position)
        # fenetre.blit(image_dessus, position)
        for i in range(2):
            if masktransi[i].overlap(perso.mask,
                                     (perso.rect.x - position.x, perso.rect.y - position.y)) and not onstairs:
                maptransi = open("save1/map", "w")
                maptransi.write("fjordglasrdc")
                maptransi.close()
                pospeso = open("save1/pospeso/pospesofjordglas1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapfjordglas1", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                litransifi = open("menu/quetes/visitelieu", "w")
                litransifi.write("fjordglasrdc")
                litransifi.close()
                quete.quetes()
                if i == 0:
                    pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                    pospeso.write("397,200")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                    posmap.write("-416,-545")
                    posmap.close()
                if i == 1:
                    pospeso = open("save1/pospeso/pospesofjordglasrdc", "w")
                    pospeso.write("390,228")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapfjordglasrdc", "w")
                    posmap.write("-348,-1076")
                    posmap.close()
                fjordglasrdc()
                onstairs = True


            elif not masktransi[0].overlap(perso.mask,
                                           (perso.rect.x - position.x, perso.rect.y - position.y)) and onstairs:
                onstairs = False
        if perso.mask.overlap(malarichmask, (position.x-perso.rect.x, position.y-perso.rect.y)):
            fenetre.blit(myfont.render("PRESS F", False, (1,44,166)), (perso.rect.x-75, perso.rect.y))
            if tkey[K_f]:
                fichier = open("menu/quetes/mobmort", "w")
                fichier.write("malarich")
                fichier.close()
                quete.quetes()
        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def ecurie():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("ecurie")
    persof.close()
    quete.quetes()
    mapcl = classes_map.classmapbasique("ecurie")
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesoecurie", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapecurie", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesoecurie", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapecurie", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesoecurie", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapecurie", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        if tkey[K_e]:
            for i in range(len(imagemaps.map["transi"+mapcl.name])):
                if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    with open("save1/map", "w") as maptransi:
                        maptransi.write("capitale")
                    with open("save1/pospeso/pospesoecurie", "w") as pospeso:
                        pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    with open("save1/posmap/posmapecurie", "w") as posmap:
                        posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    quete.quetes()
                    fenetre.fill((0, 0, 0))
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    capitale()
        mapcl.affichage(fenetre, perso)

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def village():
    global villageload
    villageload = True
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    quete.quetes()
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("hornet")
    fichier.close()
    mapcl = classes_map.classmapbasique("village")
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("village")
    persof.close()
    testtime = time.time()
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesovillage", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapvillage", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesovillage", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapvillage", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesovillage", "r") as pospeso:
                        pospeso=pospeso.read().split(",")
                    perso.rect.x=int(pospeso[0])
                    perso.rect.y=int(pospeso[1])
                    with open("save1/posmap/posmapvillage", "r") as posmap:
                        posmap=posmap.read().split(",")
                    mapcl.rect.x=int(posmap[0])
                    mapcl.rect.y=int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(imagemaps.map["transi"+mapcl.name])):
                if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask,
                                               (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(imagemaps.map["transi"+mapcl.name][i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesovillage", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapvillage", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("menu/quetes/visitelieu", "w")
                    litransifi.write(imagemaps.map["transi"+mapcl.name][i])
                    litransifi.close()
                    quete.quetes()

                    if imagemaps.map["transi"+mapcl.name][i] == "ecurie":
                        ecurie()
                    if imagemaps.map["transi"+mapcl.name][i] == "manoir":
                        manoir()
                        testtime = time.time()
                        break
                    if imagemaps.map["transi"+mapcl.name][i] == "maison_1village":
                        maison_1village()
                        testtime = time.time()
                        break
        mapcl.affichage(fenetre, perso)

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def manoir():
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    quete.quetes()
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    mapcl = classes_map.classmapbasique("manoir")
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("manoir")
    persof.close()
    testtime = time.time()
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()

    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesomanoir", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapmanoir", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesomanoir", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmanoir", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesomanoir", "r") as pospeso:
                        pospeso=pospeso.read().split(",")
                    perso.rect.x=int(pospeso[0])
                    perso.rect.y=int(pospeso[1])
                    with open("save1/posmap/posmapmanoir", "r") as posmap:
                        posmap=posmap.read().split(",")
                    mapcl.rect.x=int(posmap[0])
                    mapcl.rect.y=int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(imagemaps.map["transi"+mapcl.name])):
                if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask,
                                               (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    maptransi = open("save1/map", "w")
                    maptransi.write(imagemaps.map["transi"+mapcl.name][i])
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesomanoir", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmanoir", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("menu/quetes/visitelieu", "w")
                    litransifi.write(imagemaps.map["transi"+mapcl.name][i])
                    litransifi.close()
                    quete.quetes()
                    global villageload
                    if villageload:
                        return
                    else:
                        village()
        mapcl.affichage(fenetre, perso)

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def maison_1village():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    testtime = time.time()
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("maison_1village")
    persof.close()
    quete.quetes()
    mapcl = classes_map.classmapbasique("maison_1village")
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesomaison_1village", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapmaison_1village", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesomaison_1village", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapmaison_1village", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesomaison_1village", "r") as pospeso:
                        pospeso=pospeso.read().split(",")
                    perso.rect.x=int(pospeso[0])
                    perso.rect.y=int(pospeso[1])
                    with open("save1/posmap/posmapmaison_1village", "r") as posmap:
                        posmap=posmap.read().split(",")
                    mapcl.rect.x=int(posmap[0])
                    mapcl.rect.y=int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT or event.key == K_a:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(imagemaps.map["transi"+mapcl.name])):
                if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    with open("save1/map", "w") as maptransi:
                        maptransi.write(imagemaps.map["transi"+mapcl.name][i])
                    with open("save1/pospeso/pospesomaison_1village", "w") as pospeso:
                        pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    with open("save1/posmap/posmapmaison_1village", "w") as posmap:
                        posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    quete.quetes()
                    fenetre.fill((0, 0, 0))
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    global villageload
                    if imagemaps.map["transi"+mapcl.name][i] == "village":
                        if villageload:
                            return
                        else:
                            village()
        mapcl.affichage(fenetre, perso)

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def shop_potion():
    fichier = open("menu/quetes/mobmort", "w")
    fichier.write("")
    fichier.close()
    testtime = time.time()
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    persof = open("save1/perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase("shop_potion")
    persof.close()
    quete.quetes()
    mapcl = classes_map.classmapbasique("shop_potion")
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    tapismask=pygame.mask.from_surface(pygame.image.load("map/shop_potion/shop_potion_tapis.png").convert_alpha())
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesoshop_potion", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapshop_potion", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesoshop_potion", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapshop_potion", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesoshop_potion", "r") as pospeso:
                        pospeso=pospeso.read().split(",")
                    perso.rect.x=int(pospeso[0])
                    perso.rect.y=int(pospeso[1])
                    with open("save1/posmap/posmapshop_potion", "r") as posmap:
                        posmap=posmap.read().split(",")
                    mapcl.rect.x=int(posmap[0])
                    mapcl.rect.y=int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
                if event.key == K_p:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    shop.shop()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT or event.key == K_a:
                    perso.imageperso = perso.L1
        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(imagemaps.map["transi"+mapcl.name])):
                if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask, (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                    with open("save1/map", "w") as maptransi:
                        maptransi.write(imagemaps.map["transi"+mapcl.name][i])
                    with open("save1/pospeso/pospesoshop_potion", "w") as pospeso:
                        pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    with open("save1/posmap/posmapshop_potion", "w") as posmap:
                        posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    quete.quetes()
                    fenetre.fill((0, 0, 0))
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    global capitaleload
                    if imagemaps.map["transi"+mapcl.name][i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale()
        mapcl.affichage(fenetre, perso)

        if perso.mask.overlap(tapismask, (mapcl.rect.x-perso.rect.x, mapcl.rect.y-perso.rect.y)):
            fenetre.blit(police.render("PRESS E", True, (0,0,0)), (perso.rect.x-75, perso.rect.y))
            if tkey[K_e]:
                pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                shop.shop()
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def guilde_1():
    with open("save1/activation/perso3", "r") as perso3:
        perso3 = bool(int(perso3.read()))
    if not perso3:
        fichier = open("menu/quetes/mobmort", "w")
        fichier.write("voleur")
        fichier.close()
    else:
        fichier = open("menu/quetes/mobmort", "w")
        fichier.write("")
        fichier.close()
    mapcl = classes_map.classmapbasique("guilde-1")
    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    perso = persobase("guilde-1")
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.load("son/Sound/guilde.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    escape = escapemenu.escape()
    onstairs = True

    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesoguilde-1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapguilde-1", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesoguilde-1", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapguilde-1", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesoguilde-1", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapguilde-1", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1

        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)

        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        mapcl.affichage(fenetre, perso)

        if tkey[K_e] and time.time() - testtime > 0.5:

            if imagemaps.map["transi"+mapcl.name+"mask"][0].overlap(perso.mask,
                                           (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)):
                maptransi = open("save1/map", "w")
                maptransi.write("capitale")
                maptransi.close()
                pospeso = open("save1/pospeso/pospesoguilde-1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapguilde-1", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                litransifi = open("menu/quetes/visitelieu", "w")
                litransifi.write(imagemaps.map["transi"+mapcl.name][i])
                litransifi.close()
                quete.quetes()
                pygame.mixer.music.load("son/Sound/guilde.mp3")
                pygame.mixer.music.play(-1)
                capitale()
        for i in range(4):
            if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask,
                                           (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and not onstairs:
                pospeso = open("save1/pospeso/pospesoguilde-1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapguilde-1", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                if i == 1:
                    maptransi = open("save1/map", "w")
                    maptransi.write("guilde-2")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesoguilde-2", "w")
                    pospeso.write("492,192")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapguilde-2", "w")
                    posmap.write("-1119,-408")
                    posmap.close()
                    guilde_2()
                if i == 2:
                    maptransi = open("save1/map", "w")
                    maptransi.write("guilde-2")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesoguilde-2", "w")
                    pospeso.write("492,192")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapguilde-2", "w")
                    posmap.write("-1792,0")
                    posmap.close()
                    guilde_2()
                if i == 3:
                    maptransi = open("save1/map", "w")
                    maptransi.write("guilde-2")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesoguilde-2", "w")
                    pospeso.write("320,372")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapguilde-2", "w")
                    posmap.write("-1512,-1032")
                    posmap.close()
                    guilde_2()

                onstairs = True

            elif not imagemaps.map["transi"+mapcl.name+"mask"][1].overlap(perso.mask,
                                                 (perso.rect.x - mapcl.rect.x,
                                                  perso.rect.y - mapcl.rect.y)) and onstairs:
                onstairs = False


        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def guilde_2():
    with open("save1/activation/perso3", "r") as perso3:
        perso3 = bool(int(perso3.read()))
    if not perso3:
        fichier = open("menu/quetes/mobmort", "w")
        fichier.write("voleur")
        fichier.close()
    else:
        fichier = open("menu/quetes/mobmort", "w")
        fichier.write("")
        fichier.close()
    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    mapcl = classes_map.classmapbasique("guilde-2")
    perso = persobase("guilde-2")
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape = escapemenu.escape()
    onstairs = True

    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesoguilde-2", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapguilde-2", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesoguilde-2", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapguilde-2", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesoguilde-2", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapguilde-2", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1

        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)
        mapcl.interaction(perso, fenetre)
        mapcl.affichage(fenetre, perso)

        for i in range(4):
            if imagemaps.map["transi"+mapcl.name+"mask"][i].overlap(perso.mask,
                                           (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and not onstairs:
                maptransi = open("save1/map", "w")
                maptransi.write("butin")
                maptransi.close()
                pospeso = open("save1/pospeso/pospesoguilde-2", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapguilde-2", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                litransifi = open("menu/quetes/visitelieu", "w")
                litransifi.write("butin")
                litransifi.close()
                quete.quetes()
                if i == 0:
                    maptransi = open("save1/map", "w")
                    maptransi.write("guilde-1")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesoguilde-1", "w")
                    pospeso.write("320,360")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapguilde-1", "w")
                    posmap.write("-1160,-261")
                    posmap.close()
                    guilde_1()
                if i == 1:
                    maptransi = open("save1/map", "w")
                    maptransi.write("guilde-1")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesoguilde-1", "w")
                    pospeso.write("460,206")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapguilde-1", "w")
                    posmap.write("-1792,-35")
                    posmap.close()
                    guilde_1()
                if i == 2:
                    maptransi = open("save1/map", "w")
                    maptransi.write("guilde-1")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesoguilde-1", "w")
                    pospeso.write("320,363")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapguilde-1", "w")
                    posmap.write("-1469,-1080")
                    posmap.close()
                    guilde_1()
                if i == 3:
                    maptransi = open("save1/map", "w")
                    maptransi.write("butin")
                    maptransi.close()
                    pospeso = open("save1/pospeso/pospesobutin", "w")
                    pospeso.write("220,221")
                    pospeso.close()
                    posmap = open("save1/posmap/posmapbutin", "w")
                    posmap.write("0,0")
                    posmap.close()
                    butin()
                onstairs = True
            for j in range (4):
                if not imagemaps.map["transi"+mapcl.name+"mask"][1].overlap(perso.mask,
                                                 (perso.rect.x - mapcl.rect.x,
                                                  perso.rect.y - mapcl.rect.y)) and onstairs:
                    if i == 3:
                        onstairs = False
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def butin():
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    sinatra=pygame.image.load("perso/Sinatra/F1.png").convert_alpha()
    sinatrarect=sinatra.get_rect()
    sinatrarect.x=396
    sinatrarect.y=345
    perso = persobase("butin")
    mapcl=classes_map.classmapbasique("butin")
    with open("save1/activation/perso3", "r") as perso3:
        perso3 = bool(int(perso3.read()))
    myfont = pygame.font.SysFont("monospace", 20)
    pygame.mixer.music.set_volume(0.1)
    escape=escapemenu.escape()
    onstairs = True
    while 1:
        verificationniveau()
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1/pospeso/pospesobutin", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapbutin", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                closemenu.closemenu()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1/pospeso/pospesobutin", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1/posmap/posmapbutin", "w")
                    posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                    posmap.close()
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    escape.interface()
                    with open("save1/pospeso/pospesobutin", "r") as pospeso:
                        pospeso = pospeso.read().split(",")
                    perso.rect.x = int(pospeso[0])
                    perso.rect.y = int(pospeso[1])
                    with open("save1/posmap/posmapbutin", "r") as posmap:
                        posmap = posmap.read().split(",")
                    mapcl.rect.x = int(posmap[0])
                    mapcl.rect.y = int(posmap[1])
                if event.key == K_i:
                    pygame.image.save(fenetre, "menu/inventory/fond.jpg")
                    printinvent.printinvent()
            if event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    perso.imageperso = perso.F1
                if event.key == K_UP or event.key == K_w:
                    perso.imageperso = perso.B1
                if event.key == K_RIGHT or event.key == K_d:
                    perso.imageperso = perso.R1
                if event.key == K_LEFT:
                    perso.imageperso = perso.L1

        perso.eventkey(mapcl.rect, mapcl.mask, mapcl.size)

        tkey = pygame.key.get_pressed()
        mapcl.interaction(perso, fenetre)
        mapcl.affichage(fenetre, perso)
        if not perso3:
            fenetre.blit(sinatra, (sinatrarect.x+mapcl.rect.x, sinatrarect.y+mapcl.rect.y))
            if perso.rect.colliderect(Rect(sinatrarect.x+mapcl.rect.x, sinatrarect.y+mapcl.rect.y, 37, 42)):
                fichier = open("menu/quetes/mobmort", "w")
                fichier.write("sinatramechante")
                fichier.close()
                quete.quetes()

        # fenetre.blit(image_dessus, mapcl.rect)

        if imagemaps.map["transi"+mapcl.name+"mask"][0].overlap(perso.mask,
                                     (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and not onstairs:
                maptransi = open("save1/map", "w")
                maptransi.write("butin")
                maptransi.close()
                pospeso = open("save1/pospeso/pospesobutin", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1/posmap/posmapbutin", "w")
                posmap.write(str(mapcl.rect.x) + "," + str(mapcl.rect.y))
                posmap.close()
                fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                pygame.display.flip()
                litransifi = open("menu/quetes/visitelieu", "w")
                litransifi.write("guilde-2")
                litransifi.close()
                quete.quetes()
                pospeso = open("save1/pospeso/pospesoguilde-2", "w")
                pospeso.write("401,292")
                pospeso.close()
                posmap = open("save1/posmap/posmapguilde-2", "w")
                posmap.write("-522,-2")
                posmap.close()
                guilde_2()
                onstairs = True


        elif not imagemaps.map["transi"+mapcl.name+"mask"][0].overlap(perso.mask,
                                           (perso.rect.x - mapcl.rect.x, perso.rect.y - mapcl.rect.y)) and onstairs:
            onstairs = False

        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS
