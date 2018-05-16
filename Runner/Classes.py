import pygame as pg
from random import randint, randrange, choice
from Runner.Options import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.walking = False
        self.jumping = False
        self.invincible = False
        self.invincible_timer = 0
        self.shield = pg.image.load('Runner/img/N-Ship_shield.png').convert_alpha()
        self.current_frame = 0
        self.last_update = 0
        self.vie = 3
        self.coeur = pg.image.load('Runner/img/coeur.png').convert_alpha()
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.pos = vec(10, HAUTEUR/2)
        self.vit = vec(0, 0)
        self.acc = vec(0, 0)

    def load_images(self) :
        self.standing_frames = [pg.image.load('Runner/img/R1.png').convert_alpha()]

        self.walk_frames_r = [pg.image.load('Runner/img/R1.png'),
                              pg.image.load('Runner/img/R2.png'),
                              pg.image.load('Runner/img/R3.png')]
        self.walk_frames_l = []
        for frame in self.walk_frames_r :
            frame.convert_alpha()
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))

        self.jump_frame_r = self.walk_frames_r[2]
        self.jump_frame_l = self.walk_frames_l[2]

    def jump_cut(self) :
        # la hauteur du saut s'adapte au temps d'appui sur la barre ESPACE
        if self.jumping :
            if self.vit.y < -PLAYER_SHORT_JUMP :
                self.vit.y = -PLAYER_SHORT_JUMP

    def jump(self):
        # on saute seulemnt si l'on est au sol ou sur une plateforme
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits and not self.jumping:
            self.game.jump_son.play()
            self.jumping = True
            self.vit.y = -PLAYER_JUMP

    def update(self):
        self.animate()
        self.acc = vec(0,PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # on applique les frottements du sol
        self.acc.x += self.vit.x * PLAYER_FRICTION
        #équations du mouvement
        self.vit += self.acc
        if abs(self.vit.x) < 0.1 :
            self.vit.x = 0
        self.pos += self.vit + 0.5 * self.acc

        if self.pos.x <= 20 :
            self.pos.x = 20
        if self.pos.x >= 780 :
            self.pos.x = 780
        self.rect.midbottom = self.pos

        if self.invincible :
            self.invincible_timer += 1
            if self.invincible_timer > PLAYER_INVINCIBLE_TIME :
                self.invincible_timer = 0
                self.invincible = False

    def animate(self):
        now = pg.time.get_ticks()

        if self.vit.x != 0 :
            self.walking = True
        else :
            self.walking = False

        if self.vit.y != 0 :
            self.jumping = True
        else :
            self.jumping = False

        if self.jumping :
        # animation personnage pendant le saut
            bottom = self.rect.bottom
            if self.vit.x >= 0 :
                self.image = self.jump_frame_r
            else :
                self.image = self.jump_frame_l
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom

        if self.walking and not self.jumping :
            # animation personnage pendant la course
            if now - self.last_update > 180 :
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vit.x > 0 :
                    self.image = self.walk_frames_r[self.current_frame]
                else :
                    self.image = self.walk_frames_l[self.current_frame]
                self.rect =self.image.get_rect()
                self.rect.bottom = bottom

        # animation du personnage lorsqu'il n'y a pas de mouvement
        if not self.jumping and not self.walking :
             if now - self.last_update > 350 :
                 self.last_update = now
                 self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                 bottom = self.rect.bottom
                 self.image = self.standing_frames[self.current_frame]
                 self.rect = self.image.get_rect()
                 self.rect.bottom = bottom

        self.mask = pg.mask.from_surface(self.image)

class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLATFORM_LAYER
        self.groups = game.all_sprites, game.platforms
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        if self.game.spawned_portal :
            self.num_image = 4
        else :
            self.num_image = 1
        self.create_plat()
        self.image = self.plat_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        if self.game.pass_portal :
            if randrange(100) < POW_SPAWN_PCT :
                Powerup(self.game, self)

    def create_plat(self) :

        n = int(randint(2, 10))
        rect_img = []
        self.platform = [pg.image.load('Runner/img/plateforme' + str(self.num_image) + '.png')]
        for i in range (n) :
            self.platform.append(pg.image.load('Runner/img/plateforme' + str(self.num_image+1) + '.png'))
        self.platform.append(pg.image.load('Runner/img/plateforme' + str(self.num_image+2) + '.png'))
        self.plat_image = pg.Surface((40+n*20, 20))
        self.plat_image.set_colorkey(BLACK)
        for i in range (0, len(self.platform)) :
            rect_img.append(self.platform[i].get_rect())
            rect_img[i][0] = rect_img[i-1][0]+ rect_img[i-1][2]
            if i == 0 :
                rect_img[i][0] = 0
            self.plat_image.blit(self.platform[i], (rect_img[i][0], 0))

class Powerup(pg.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = POW_LAYER
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = choice(['boost'])
        self.image = pg.image.load('Runner/img/pow_boost.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top-3

    def update(self):
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top-3
        if not self.game.platforms.has(self.plat) :
            self.kill()

class Mob_ship(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = MOB_LAYER
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = LARGEUR+100
        self.rect.y = randrange(100, HAUTEUR-100)
        self.vx = -randrange(3, 4)
        self.vy = 0
        self.dy = 0.5

    def load_images(self) :
        self.frames = []
        for i in range (1, 5) :
            for j in range (3) :
                self.frames.append(pg.image.load('Runner/img/ship0.png'))
            self.frames.append(pg.image.load('Runner/img/ship' + str(i) + '.png'))
        for frame in self.frames :
            frame.convert_alpha()

    def update(self):
        self.animate()
        self.rect.x += self.vx
        self.vy += self.dy
        if self.vy < -3 or self.vy > 3 :
            self.dy *= -1
        self.rect.y += self.vy
        if self.rect.left < -100 :
            self.kill()

    def animate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 150 :
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            center = self.rect.center
            self.image = self.frames[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.center = center
        self.mask = pg.mask.from_surface(self.image)

class Portal(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = PORTAL_LAYER
        self.groups = game.all_sprites, game.portals
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.pass_portal = False
        self.image = pg.image.load('Runner/img/portal.png')
        self.rect = self.image.get_rect()
        self.rect.x = LARGEUR
        self.rect.y = 10
