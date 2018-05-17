import pygame as pg
from random import randint, randrange, choice
from Options import *
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
        self.shield = pg.image.load('img/N-Ship_shield.png').convert_alpha()
        self.current_frame = 0
        self.last_update = 0
        self.vie = 3
        self.coeur = pg.image.load('img/coeur.png').convert_alpha()
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.pos = vec(10, HAUTEUR/2)
        self.vit = vec(0, 0)
        self.acc = vec(0, 0)

    def load_images(self) :
        self.standing_frames = [pg.image.load('img/R1.png').convert_alpha()]

        self.walk_frames_r = [pg.image.load('img/R1.png'),
                              pg.image.load('img/R2.png'),
                              pg.image.load('img/R3.png')]
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

        if not self.game.pass_portal or self.game.pass_portal2 :
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
            if now - self.last_update > 125 :
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
        if self.game.spawned_portal == True and self.game.spawned_portal2 == False :
            self.num_image = 4
        if (self.game.spawned_portal == False and self.game.spawned_portal2 == False) or self.game.spawned_portal2 == True :
            self.num_image = 1
        self.create_plat()
        self.image = self.plat_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        for hit in hits:
            if hit != self:
                self.kill()

        if self.game.spawned_portal :
            if self.game.gem_score <= SCORE_LIMIT :
                if randrange(100) < OBSTACLE_SPAWN_PCT :
                    Obstacle(self.game, self)
                if randrange(100) < GEM_SPAWN_PCT :
                    Object(self.game, self, 'gem')
        if not self.game.spawned_portal and not self.game.spawned_portal2 :
            if randrange(100) < BOOST_SPAWN_PCT :
                Object(self.game, self, 'boost')


    def create_plat(self) :

        if self.game.spawned_portal2 == True :
            n = 40
        else :
            n = randint(2, 10)
        rect_img = []
        self.platform = [pg.image.load('img/plateforme' + str(self.num_image) + '.png')]
        for i in range (n) :
            self.platform.append(pg.image.load('img/plateforme' + str(self.num_image+1) + '.png'))
        self.platform.append(pg.image.load('img/plateforme' + str(self.num_image+2) + '.png'))
        self.plat_image = pg.Surface((40+n*20, 20))
        self.plat_image.set_colorkey(BLACK)
        for i in range (0, len(self.platform)) :
            rect_img.append(self.platform[i].get_rect())
            rect_img[i][0] = rect_img[i-1][0]+ rect_img[i-1][2]
            if i == 0 :
                rect_img[i][0] = 0
            self.plat_image.blit(self.platform[i], (rect_img[i][0], 0))

    def update(self):
        if self.rect.right <= 0 :
            self.kill()

class Object(pg.sprite.Sprite):
    def __init__(self, game, plat, type_o):
        self._layer = OBJECT_LAYER
        self.groups = game.all_sprites, game.objects
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = type_o
        if self.type == 'boost' :
            self.image = pg.image.load('img/pow_boost.png').convert_alpha()
        if self.type == 'gem' :
            self.image = pg.image.load('img/gem.png').convert_alpha()
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
                self.frames.append(pg.image.load('img/ship0.png'))
            self.frames.append(pg.image.load('img/ship' + str(i) + '.png'))
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
    def __init__(self, game, type_portal):
        self._layer = PORTAL_LAYER
        self.groups = game.all_sprites, game.portals
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.type = type_portal
        if self.type == 'portal1' :
            self.image = pg.image.load('img/portal.png').convert_alpha()
        if self.type == 'portal2' :
            self.image = pg.image.load('img/portal2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = LARGEUR+5
        self.rect.y = 10

    def update(self):
        if self.rect.right <= 0 :
            self.kill()

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = OBSTACLE_LAYER
        self.groups = game.all_sprites, game.obstacles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = choice(['champ_elec', 'pics'])
        self.current_frame = 0
        self.last_update = 0
        self.champ_elec_img()
        self.pics_img()
        self.image = self.pic_img
        if self.type == 'champ_elec' and self.plat.rect.width >= 150 :
            self.image = self.frames[0]
        if self.type == 'pics':
            self.image = self.pic_img
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top
        self.mask = pg.mask.from_surface(self.image)

    def champ_elec_img(self) :
        self.frames = []
        for i in range (5) :
            for j in range (3) :
                self.frames.append(pg.image.load('img/champelec_none.png'))
            self.frames.append(pg.image.load('img/champ_elec' + str(i) + '.png'))
        for frame in self.frames :
            frame.convert_alpha()

    def update(self):
        if self.type == 'champ_elec' and self.plat.rect.width >= 150 :
            self.animate()
            self.rect.centerx = self.plat.rect.centerx-5
        else :
            self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top
        if not self.game.platforms.has(self.plat) :
            self.kill()

    def animate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 300 :
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            center = self.rect.center
            self.image = self.frames[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.center = center
        self.mask = pg.mask.from_surface(self.image)

    def pics_img(self) :
        n = int(randint(1, self.plat.rect.width/20))
        rect_img = []
        self.pic = [pg.image.load('img/pic.png').convert_alpha()]
        for i in range (n) :
            self.pic.append(self.pic[0])
        self.pic_img = pg.Surface((20*n, 29))
        self.pic_img.set_colorkey(BLACK)
        for i in range (0, len(self.pic)) :
            rect_img.append(self.pic[i].get_rect())
            rect_img[i][0] = rect_img[i-1][0]+ rect_img[i-1][2]
            if i == 0 :
                rect_img[i][0] = 0
            self.pic_img.blit(self.pic[i], (rect_img[i][0], 0))

class Boss(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = BOSS_LAYER
        self.groups = game.all_sprites, game.boss
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.current_frame = 0
        self.last_update = 0
        self.protection = False
        self.protection_timer = 0
        self.vie = 5
        self.coeur = pg.image.load('img/coeur_boss.png').convert_alpha()
        self.head = pg.image.load('img/boss_head.png').convert_alpha()
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.vit = vec(0, 0)

    def load_images(self) :
            self.standing_frames = []
            self.walk_frames_r = []
            self.walk_frames_l = []

            for i in range (14) :
                self.standing_frames.append(pg.image.load('img/boss' + str(i) +'.png').convert_alpha())
            for i in range (5) :
                self.walk_frames_r.append(pg.image.load('img/boss_move' + str(i) +'.png').convert_alpha())
            for frame in self.walk_frames_r :
                self.walk_frames_l.append(pg.transform.flip(frame, True, False))
            self.died_img = pg.image.load('img/boss_died.png').convert_alpha()

    def update(self):
        if self.vie > 0 :
            if self.game.combat :
                self.animate_fight()
            if not self.game.combat :
                self.animate_intro()

        self.pos += self.vit

        if self.pos.x <= 50 :
            self.pos.x = 50
        if self.pos.x >= 750 :
            self.pos.x = 750
        self.rect.midbottom = self.pos

        if self.protection :
            self.protection_timer += 1
            if self.protection_timer > BOSS_PROTECTION_TIME :
                self.protection_timer = 0
                self.protection = False

    def animate_intro(self):
        now = pg.time.get_ticks()
        # animation d'introduction du boss
        if now - self.last_update > 150 :
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
            bottom = self.rect.bottom
            self.image = self.standing_frames[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom

        self.mask = pg.mask.from_surface(self.image)

    def animate_fight(self):
        now = pg.time.get_ticks()
        # animation boss pendant le combat
        if now - self.last_update > 125 :
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
            bottom = self.rect.bottom
            if self.vit.x > 0 :
                self.image = self.walk_frames_r[self.current_frame]
            else :
                self.image = self.walk_frames_l[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom

        self.mask = pg.mask.from_surface(self.image)
