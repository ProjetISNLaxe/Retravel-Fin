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
