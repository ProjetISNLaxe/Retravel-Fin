import pygame, sys
from pygame.locals import *
from menu.imageinterfacetoload import test, testrect, testmask, police, ouverture, fermeture

with open("options\\fullscreen", "r") as fullscreen:
    fullscreenread = fullscreen.read()

if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else:
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)


def closemenu():
    """Fonction qui permet l'affichage de la fenetre de confirmation de fermeture"""
    ouverture.play()
    clock = pygame.time.Clock()
    dialoguequete = pygame.image.load("menu/quetes/HUD/boitedialogue.png").convert_alpha()
    bouton1 = pygame.image.load("menu/quetes/HUD/boutonrester.png").convert_alpha()
    bouton2 = pygame.image.load("menu/quetes/HUD/boutonvalider.png").convert_alpha()
    bouton1rect = bouton1.get_rect()
    bouton2rect = bouton2.get_rect()
    bouton1rect.x = 100
    bouton1rect.y = 165
    bouton2rect.x = 420
    bouton2rect.y = 165
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            if event.type == MOUSEMOTION:
                if event.type == MOUSEMOTION:
                    testrect.x = event.pos[0]
                    testrect.y = event.pos[1]
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if testrect.colliderect(bouton1rect):
                        fermeture.play()
                        return
                    if testrect.colliderect(bouton2rect):
                        from battle.save import savetpt
                        savetpt()
                        fermeture.play()
                        pygame.mixer.quit()
                        pygame.quit()
                        sys.exit()

        fenetre.blit(dialoguequete, (0, 0))
        dialoguequete = pygame.image.load("menu/quetes/HUD/boitedialogue.png").convert_alpha()
        fenetre.blit(bouton2, bouton2rect)
        fenetre.blit(bouton1, bouton1rect)
        dialoguequete.blit(police.render("Voulez-vous quitter ?", True, (32, 153, 152)), (175, 25))
        dialoguequete.blit(police.render("Votre partie sera sauvegardé", True, (32, 153, 152)), (175, 40))

        clock.tick(60)  # 60 FPS
        pygame.display.flip()
