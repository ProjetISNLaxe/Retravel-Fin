import pygame


def respawn():
    from classes.classes_tpt import perso_joueur, david, sinatra
    pygame.mixer.music.load("son/Sound/day.mp3")
    pygame.mixer.music.play(-1)
    with open("save1/map", "r") as mapactive:
            mapactive = mapactive.read()
    with open("save1/pv/pvp1", "w") as pvp1:
        pvp1.write(str(perso_joueur.viemax))
    with open("save1/pv/pvp2", "w") as pvp2:
        pvp2.write(str(david.viemax))
    with open("save1/pv/pvp3", "w") as pvp3:
        pvp3.write(str(sinatra.viemax))
    if "fjordglas" not in mapactive:
        with open("save1/posmap/posmap"+mapactive, "w") as writer:
            writer.write("")

        with open("save1/pospeso/pospeso"+mapactive, "w") as writer:
            writer.write("")

        with open("save1/map", "w") as mapactive:
            mapactive.write("maison_2")

        with open("save1/pospeso/pospesomaison_2", "w") as writer:
            writer.write("571,237")

        with open("save1/posmap/posmapmaison_2", "w") as writer:
            writer.write("-208,-9")
        with open("save1/pospeso/pospesocapitale", "w") as writer:
            writer.write("403,208")

        with open("save1/posmap/posmapcapitale", "w") as writer:
            writer.write("-1136,-2925")
    else:
        with open("save1/map", "w") as mapactive:
            mapactive.write("cheminfjord")
        with open("save1/posmap/posmapfjordglasrdc", "w") as writer:
            writer.write("")
        with open("save1/pospeso/pospesofjordglasrdc", "w") as writer:
            writer.write("")
