import pygame as pg
import random
from Runner.Options import *
from Runner.Classes import *
from os import path


class Jeu:
    def __init__(self):
        # initialisation de la fenêtre, etc
        pg.init()
        pg.mixer.init()
        self.fenetre = pg.display.set_mode((LARGEUR, HAUTEUR))
        pg.display.set_caption(TITRE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        # charger les différents sons du jeu
        self.jump_son = pg.mixer.Sound('Runner/son/Jump15.wav')
        self.boost_son = pg.mixer.Sound('Runner/son/Randomize87.wav')
        self.hurt_son = pg.mixer.Sound('Runner/son/Hit_Hurt5.wav')
        self.list_fond = []
        for i in range(1, 6):
            nom_image = 'Runner/img/fond' + str(i) + '.png'
            self.list_fond.append(pg.image.load(nom_image).convert())
        self.list_fond2 = [self.list_fond[1], self.list_fond[2]]
        self.list_fond3 = [self.list_fond[3], self.list_fond[4]]
        self.fond = self.list_fond[0]

    def new(self):
        # commencer une nouvelle partie
        self.score = 0
        self.gem_score = 0
        self.mob_timer = 0
        self.boss_timer = 0
        self.portal_timer = 0
        self.current_frame = 0
        self.last_update = 0
        self.spawned_portal = False
        self.pass_portal = False
        self.spawned_portal2 = False
        self.pass_portal2 = False
        self.spawn_sol = False
        self.spawned_boss = False
        self.combat = False
        self.boss_died = False
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.platforms = pg.sprite.Group()
        self.objects = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.portals = pg.sprite.Group()
        self.obstacles = pg.sprite.Group()
        self.boss = pg.sprite.Group()
        self.player = Player(self)
        for plat in PLATFORM_LIST:
            Platform(self, *plat)
        pg.mixer.music.load('Runner/son/Chagrin.wav')
        self.run()

    def run(self):
        # boucle du jeu
        pg.mixer.music.play(loops=-1)
        self.playing = True
        self.win = False
        while self.playing == True:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.display()
            if self.win:
                self.victory_screen()
        pg.mixer.music.fadeout(500)

    def update(self):
        # boucle du jeu mise à jour
        self.all_sprites.update()
        self.animation_fond()

        # apparition ennemis
        now = pg.time.get_ticks()
        if now - self.mob_timer > MOQ_FREQ + random.choice([-1000, -500, 0, 500, 1000]):
            self.mob_timer = now
            if self.score <= SCORE_LIMIT:
                Mob_ship(self)

        # collision ennemis - phase 1
        mob_hits = pg.sprite.spritecollide(self.player, self.mobs, False, pg.sprite.collide_mask)
        mob_died = False
        for mob in self.mobs:
            if not self.player.invincible:
                if (mob.rect.left <= self.player.rect.centerx <= mob.rect.right and \
                    mob.rect.top - 5 <= self.player.rect.bottom <= mob.rect.centery) and self.player.jumping:
                    mob_died = True
                    mob.kill()
                    if not self.spawned_portal:
                        self.score += 1
                if mob_hits and not mob_died:
                    self.hurt_son.play()
                    self.player.vie -= 1
                    self.player.invincible = True

        # collision obstacles - phase 2
        obst_hits = pg.sprite.spritecollide(self.player, self.obstacles, False, pg.sprite.collide_mask)
        if obst_hits:
            if not self.player.invincible:
                self.hurt_son.play()
                self.player.vie -= 1
                self.player.invincible = True

        # on vérifie si le joueur touche une plateforme (uniquement en descendant)
        if self.player.vit.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if lowest.rect.left - 10 < self.player.pos.x < lowest.rect.right + 10:
                    if self.player.pos.y < lowest.rect.bottom + 5:
                        self.player.pos.y = lowest.rect.top + 0.3
                        self.player.vit.y = 0
                        self.player.jumping = False
        # si le joueur arrive au 2/3 de la largeur de l'écran
        if self.player.rect.x >= LARGEUR / 3:
            if not self.pass_portal and not self.pass_portal2:
                self.player.pos.x -= max(abs(self.player.vit.x), 2)
                for mob in self.mobs:
                    mob.rect.x -= max(abs(self.player.vit.x), 2)
                for plat in self.platforms:
                    plat.rect.right -= max(abs(self.player.vit.x), 2)
                for portal in self.portals:
                    portal.rect.right -= max(abs(self.player.vit.x), 2)

        # collision entre un object collectable et le joueur
        object_hits = pg.sprite.spritecollide(self.player, self.objects, True)
        for object in object_hits:
            if object.type == 'boost':
                self.boost_son.play()
                self.player.vit.x = SPEED_BOOST
                self.player.vit.y = -JUMP_BOOST
                self.player.walking = False
            if object.type == 'gem':
                self.gem_score += 1

        # créer de nouvelles plateformes
        if self.spawned_portal2 == False:
            while len(self.platforms) < 8:
                if self.spawned_portal == False:
                    Platform(self, random.randrange(LARGEUR, LARGEUR + 240),
                             random.randrange(150, HAUTEUR - 20))
                else:
                    Platform(self, random.randrange(LARGEUR, LARGEUR + 240),
                             random.choice([150, 300, 450]))
        else:
            if not self.spawn_sol:
                Platform(self, LARGEUR + 240, HAUTEUR - 50)
                self.spawn_sol = True

        # déclenchement phase 2
        if self.score > SCORE_LIMIT:
            if now - self.portal_timer > 5000 and not self.spawned_portal and not self.spawned_portal2:
                self.portal_timer = now
                self.portal1 = Portal(self, 'portal1')
                self.spawned_portal = True

        # déclenchement phase 3
        if self.gem_score > SCORE_LIMIT:
            if now - self.portal_timer > 5000 and not self.spawned_portal2:
                self.portal_timer = now
                self.portal2 = Portal(self, 'portal2')
                self.spawned_portal2 = True

        for portal in self.portals:
            # franchissement portails
            if portal.type == 'portal1':
                if self.player.rect.right > portal.rect.centerx + 10:
                    self.pass_portal = True
                else:
                    self.pass_portal = False
            if portal.type == 'portal2':
                if self.player.rect.right > portal.rect.centerx + 10:
                    self.pass_portal2 = True
                else:
                    self.pass_portal2 = False

        if self.pass_portal and not self.pass_portal2:
            # la vitesse est réduite pour ne pas que le joueur aille trop vite par rapport au scrolling
            self.player.vit.x *= 0.75
            # scrolling indépendant du joueur pour la phase 2
            if self.player.vit.x <= 0:
                self.player.pos.x -= VIT_SCROLLING
            for plat in self.platforms:
                if plat.rect.right <= 0:
                    plat.kill()
                else:
                    plat.rect.right -= VIT_SCROLLING
            for portal in self.portals:
                portal.rect.right -= VIT_SCROLLING

        if self.pass_portal2:
            for plat in self.platforms:
                if plat.num_image == 4:
                    if plat.rect.right <= -240:
                        plat.kill()
                    else:
                        plat.rect.right -= VIT_SCROLLING
                if plat.num_image == 1:
                    if plat.rect.right - 20 > LARGEUR:
                        plat.rect.x -= VIT_SCROLLING

            for portal in self.portals:
                portal.rect.right -= VIT_SCROLLING
                if portal.rect.left < 1 and not self.spawned_boss:
                    Boss(self, 700, HAUTEUR - 48)
                    self.spawned_boss = True

        if self.spawned_boss:
            # démarrage combat avec le changement d'animation
            if self.player.rect.x > LARGEUR * 0.6:
                self.combat = True

        if self.combat:
            # combat de boss
            for boss in self.boss:
                if boss.rect.x < self.player.rect.x:
                    boss.vit.x = 2
                if boss.rect.x > self.player.rect.x:
                    boss.vit.x = -2
                if self.player.rect.x - 1 <= boss.rect.x <= self.player.rect.x + 1:
                    boss.vit.x = 0
                # collisions boss - phase 3
                boss_hit = pg.sprite.spritecollide(self.player, self.boss, False, pg.sprite.collide_mask)
                if not self.player.invincible and not boss.protection:
                    if (boss.rect.left + 5 <= self.player.rect.centerx <= boss.rect.right - 5 and \
                        boss.rect.top - 5 <= self.player.rect.bottom <= boss.rect.centery) and self.player.jumping:
                        boss.vie -= 1
                        boss.protection = True
                    if boss_hit and not self.boss_died:
                        self.hurt_son.play()
                        self.player.vie -= 1
                        self.player.invincible = True

        for boss in self.boss:
            # si l'ennemi est à cours de vies
            if boss.vie <= 0:
                self.boss_died = True
                boss.image = boss.died_img
                boss.vit.x = 0
                if boss.rect.bottom < HAUTEUR - 30:
                    boss.vit.y = 1
                if boss.rect.top > HAUTEUR:
                    self.win = True

        # si le joueur tombe dans le vide
        if self.player.rect.top > HAUTEUR:
            self.playing = False

        # si le joueur n'a plus de vies
        if self.player.vie <= 0:
            self.playing = False

        # phase 2 - si le joueur n'arrive plus à suivre
        if self.player.rect.right < -5:
            self.playing = False

    def animation_fond(self):
        # changement du fond selon les phase
        now = pg.time.get_ticks()
        if not self.pass_portal and not self.pass_portal2:
            self.fond = self.list_fond[0]
        else:
            if self.pass_portal and not self.pass_portal2:
                if now - self.last_update > 2000:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.list_fond2)
                    self.fond = self.list_fond2[self.current_frame]
            if self.pass_portal2:
                if now - self.last_update > 2000:
                    self.last_update = now
                    self.current_frame = (self.current_frame + 1) % len(self.list_fond3)
                    self.fond = self.list_fond3[self.current_frame]

    def events(self):
        # actions / événements
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing == True:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()

    def display(self):
        # boucle d'affichage du jeu
        self.fenetre.blit(self.fond, (0, 0))
        self.all_sprites.draw(self.fenetre)
        if self.player.invincible and self.player.vie > 0:
            self.fenetre.blit(self.player.shield, (self.player.rect.x - 10, self.player.rect.y - 3))
        for portal in self.portals:
            if self.pass_portal == True:
                self.fenetre.blit(portal.image, portal.rect)
        if not self.pass_portal and not self.pass_portal2:
            self.affiche_text(str(self.score), 30, BLANC, LARGEUR - 20, 20)
        if self.pass_portal and not self.pass_portal2:
            self.affiche_text(str(self.gem_score), 30, VERT, LARGEUR - 20, 20)
        for i in range(self.player.vie):
            self.fenetre.blit(self.player.coeur, (10 + 35 * i, 10))
        for boss in self.boss:
            if self.combat:
                if boss.vie >= 1:
                    self.fenetre.blit(boss.head, (597, 10))
                for i in range(boss.vie):
                    self.fenetre.blit(boss.coeur, (625 + 35 * i, 10))
        # après affichage de tous les éléments, on rafraîchit l'écran
        pg.display.flip()

    def affiche_text(self, text, size, color, x, y):
        # affiche le nombre d'ennemis tués lors de la phase 1
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
        self.affiche_text('RUNNER', 48, JAUNE, LARGEUR / 2, HAUTEUR / 4)
        self.affiche_text("FLECHES pour BOUGER, ESPACE pour SAUTER", 22, JAUNE, LARGEUR / 2, HAUTEUR / 2)
        self.affiche_text("APPUYEZ sur ENTER pour JOUER", 22, JAUNE, LARGEUR / 2, HAUTEUR * (3 / 4))
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def game_over_screen(self):
        # écran lorsque l'on perd
        if self.running == False:
            return
        pg.mixer.music.load('Runner/son/Son_game_over.ogg')
        pg.mixer.music.play(loops=-1)
        self.fenetre.fill(COULEUR_FOND)
        self.affiche_text('GAME OVER', 48, ROUGE, LARGEUR / 2, HAUTEUR / 4)
        self.affiche_text("APPUYEZ sur ENTER pour REESAYER", 22,
                          ROUGE, LARGEUR / 2, HAUTEUR / 2)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def victory_screen(self):
        # écran de fin - de victoire
        self.fenetre.fill(COULEUR_FOND)
        self.affiche_text('YOU WIN - FELICITATIONS', 48, ORANGE, LARGEUR / 2, HAUTEUR / 4)
        self.affiche_text("APPUYEZ sur LA CROIX pour RETOURNER au menu de Retravel", 22, ORANGE, LARGEUR / 2,
                          HAUTEUR / 2)
        pg.display.flip()
        self.wait_for_key()
        if self.running == False:
            pg.quit()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RETURN:
                        waiting = False
