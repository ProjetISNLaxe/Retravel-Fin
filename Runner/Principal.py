# idées jeu :

# phase 1 : scrolling décidé par le perso, vaisseaux bugués comme ennemis, en tuer 10 pour accéder à la phase 2 // fait
#           ennemi : 3 fois bon sprite, 1 fois sprite bugué // fait
#           MANQUE : améliorer la génération des plateformes, son lorque l'on est touché // fait

# phase 2 : passage dans le portail bleu // fait
#           boost de vitesse ramassable sur platfeformes : améliorer la physique
#           arc électriques en obstacles, pics,
#           scrolling indépendant du joueur
#           passage dans le portail orange
#           le boss nous retrouve à la fin de cette phase

# phase 3 : le boss nous poursuit, armes récupérables pour ralentir le boss, bouclier

import pygame as pg
import random
from Runner.Options import *
from Runner.Classes import *
from os import path

class Jeu :
    def __init__(self) :
        # initialisation de la fenêtre, etc
        self.fenetre = pg.display.set_mode((LARGEUR,HAUTEUR))
        pg.display.set_caption(TITRE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        # charger les différents sons du jeu
        self.dir = path.dirname(__file__)
        self.son_dir = path.join(self.dir, 'Runner/son')
        self.jump_son = pg.mixer.Sound('Runner/son/Jump15.wav')
        self.jump_son.set_volume(0.3)
        self.boost_son = pg.mixer.Sound('Runner/son/Randomize87.wav')
        self.hurt_son = pg.mixer.Sound('Runner/son/Hit_Hurt5.wav')
        self.list_fond = []
        for i in range (1, 6):
            nom_image = 'Runner/img/fond' + str(i) + '.png'
            self.list_fond.append(pg.image.load(nom_image).convert())
        self.list_fond2 = [self.list_fond[1], self.list_fond[2]]
        self.fond = self.list_fond[0]

    def new(self) :
        # commencer une nouvelle partie
        self.score = 0
        self.mob_timer = 0
        self.portal_timer = 0
        self.current_frame = 0
        self.last_update = 0
        self.spawned_portal = False
        self.pass_portal = False
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.platforms = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.portals = pg.sprite.Group()
        self.player = Player(self)
        for plat in PLATFORM_LIST :
            Platform(self, *plat)
        pg.mixer.music.load('Runner/son/Son_phase1.wav')
        self.run()

    def run(self):
        # boucle du jeu
        pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing == True :
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.animation_fond()
            self.display()
        pg.mixer.music.fadeout(500)

    def update(self):
        # boucle du jeu mise à jour
        self.all_sprites.update()

        # apparition ennemis
        now = pg.time.get_ticks()
        if now - self.mob_timer > MOQ_FREQ + random.choice([-1000, -500, 0, 500, 1000]) :
            self.mob_timer = now
            if self.score < 10 :
                Mob_ship(self)

        #collision ennemis
        mob_hits = pg.sprite.spritecollide(self.player, self.mobs, False, pg.sprite.collide_mask)
        mob_died = False
        for mob in self.mobs :
            if not self.player.invincible :
                if (mob.rect.left <= self.player.rect.centerx <= mob.rect.right  and \
                mob.rect.top-5 <= self.player.rect.bottom <= mob.rect.centery) and self.player.jumping :
                    mob_died = True
                    mob.kill()
                    self.score += 1
                if mob_hits and not mob_died :
                    self.hurt_son.play()
                    self.player.vie -= 1
                    self.player.invincible = True

        # on vérifie si le joueur touche une plateforme (uniquement en descendant)
        if self.player.vit.y > 0 :
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits :
                    if hit.rect.bottom > lowest.rect.bottom :
                        lowest = hit
                if lowest.rect.left-10 < self.player.pos.x < lowest.rect.right+10 :
                    if self.player.pos.y < lowest.rect.bottom+5 :
                        self.player.pos.y = lowest.rect.top+0.3
                        self.player.vit.y = 0
                        self.player.jumping = False
        #si le joueur arrive au 2/3 de la largeur de l'écran
        if self.player.rect.x >= LARGEUR/3 :
            self.player.pos.x -= max(abs(self.player.vit.x), 2)
            for mob in self.mobs :
                mob.rect.x -= max(abs(self.player.vit.x),2)
            for plat in self.platforms :
                if plat.rect.right <= 0 :
                    plat.kill()
                else :
                    plat.rect.right -= max(abs(self.player.vit.x),2)
            for portal in self.portals :
                if portal.rect.right <= 0 :
                    portal.kill()
                else :
                    portal.rect.right -= max(abs(self.player.vit.x),2)

        # collision entre le powerup et le joueur
        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)
        for pow in pow_hits :
            if pow.type == 'boost':
                self.boost_son.play()
                self.player.vit.x = BOOST_POWER
                self.player.vit.y = 0
                self.player.walking = False

        #créer de nouvelles plateformes
        while len(self.platforms) < 8 :
            Platform(self, LARGEUR+240,
                           random.randrange(100, HAUTEUR-20))

        for plat in self.platforms :
            plat_bug = pg.sprite.spritecollide(plat, self.platforms, False)
            for bug in plat_bug:
                if bug != plat:
                    bug.kill()

        # déclenchement phase 2
        if self.score > 9 :
            if now - self.portal_timer > 5000  and not self.spawned_portal:
                self.portal_timer = now
                self.portal = Portal(self)
                self.spawned_portal = True

        # franchissement portail
        for portal in self.portals :
            if self.player.rect.right > portal.rect.centerx :
                self.pass_portal = True
            else :
                self.pass_portal = False


        # si le joueur tombe dans le vide
        if self.player.rect.top > HAUTEUR :
            self.playing = False

        # si le joueur n'a plus de vies
        if self.player.vie <= 0 :
            self.playing = False

    def animation_fond(self):
        # changement du fond selon les phase
        now = pg.time.get_ticks()
        if self.pass_portal :
            if now - self.last_update > 2000 :
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.list_fond2)
                self.fond = self.list_fond2[self.current_frame]
        else :
            self.fond = self.list_fond[0]

    def events(self) :
        # actions / événements
        for event in pg.event.get() :
            if event.type == pg.QUIT :
                if self.playing == True :
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN :
                if event.key == pg.K_SPACE :
                    self.player.jump()
            if event.type == pg.KEYUP :
                if event.key == pg.K_SPACE :
                    self.player.jump_cut()

    def display(self) :
        # boucle d'affichage du jeu
        self.fenetre.blit(self.fond, (0, 0))
        self.all_sprites.draw(self.fenetre)
        if self.player.invincible and self.player.vie > 0:
            self.fenetre.blit(self.player.shield, (self.player.rect.x-10, self.player.rect.y-3))
        for portal in self.portals :
            if self.pass_portal == True :
                self.fenetre.blit(portal.image, portal.rect)
        if not self.pass_portal :
            self.affiche_text(str(self.score), 30, BLANC, LARGEUR-20, 20)
        for i in range (self.player.vie):
            self.fenetre.blit(self.player.coeur,(10+35*i, 10))
        # après affichage de tous les éléments, on rafraîchit l'écran
        pg.display.flip()

    def affiche_text(self, text, size, color, x, y) :
        #affiche le nombre d'ennemis tués lors de la phase 1
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.fenetre.blit(text_surface, text_rect)

    def start_screen(self):
        # écran d'accueil
        pg.mixer.music.load('Runner/son/Son_start_screen.ogg')
        pg.mixer.music.play(loops=-1)
        self.fenetre.fill(COULEUR_FOND)
        self.affiche_text('RUNNER', 48, JAUNE, LARGEUR/2, HAUTEUR/4)
        self.affiche_text("FLECHES pour BOUGER, ESPACE pour SAUTER", 22 , JAUNE, LARGEUR/2, HAUTEUR/2)
        self.affiche_text("APPUYEZ sur ENTER pour JOUER", 22 , JAUNE, LARGEUR/2, HAUTEUR*(3/4))
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def game_over_screen(self):
        # écran lorsque l'on perd
        if self.running == False :
            return
        pg.mixer.music.load('Runner/son/Son_game_over.ogg')
        pg.mixer.music.play(loops=-1)
        self.fenetre.fill(COULEUR_FOND)
        self.affiche_text('GAME OVER', 48, ROUGE, LARGEUR/2, HAUTEUR/4)
        self.affiche_text("APPUYEZ sur ENTER pour REJOUER", 22 , ROUGE, LARGEUR/2, HAUTEUR/2)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def wait_for_key(self):
        waiting = True
        while waiting :
            self.clock.tick(FPS)
            for event in pg.event.get() :
                if event.type == pg.QUIT :
                    waiting = False
                    self.running = False
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    from Launcher import launcher
                    launcher()
                if event.type == pg.KEYUP :
                    if event.key == pg.K_RETURN :
                        waiting = False


