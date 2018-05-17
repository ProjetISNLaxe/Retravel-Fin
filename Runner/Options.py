# géréral
TITRE = "Retravel - Runner"
LARGEUR = 800
HAUTEUR = 600
FPS = 60
COULEUR_FOND = (9,0,38)
FONT_NAME = 'arial'

#  propriétés personnage
PLAYER_ACC = 1
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.5
PLAYER_JUMP = 15
PLAYER_SHORT_JUMP = 5
PLAYER_INVINCIBLE_TIME = 180
BOSS_PROTECTION_TIME = 120

# propriétés jeu
SPEED_BOOST  = 120
JUMP_BOOST = 12
BOOST_SPAWN_PCT = 5
GEM_SPAWN_PCT = 15
OBSTACLE_SPAWN_PCT = 10
MOQ_FREQ = 7000
VIT_SCROLLING = 4
SCORE_LIMIT = 9

# calques pour les différentes images
PLAYER_LAYER = 4
PORTAL_LAYER = 3
BOSS_LAYER = 3
MOB_LAYER = 2
PLATFORM_LAYER  = 1
OBJECT_LAYER = 1
OBSTACLE_LAYER = 1

# propriétés plateformes de départ
PLATFORM_LIST = [(LARGEUR / 2 - 50, HAUTEUR * 3 / 4),
                (5, HAUTEUR-305),
                (350,200),
                (175, 100),
                (LARGEUR+100, 250)]

#couleurs
VERT = (28, 157, 11)
ORANGE = (239, 139, 3)
BLANC = (228, 228, 228)
JAUNE = (235, 223, 32)
ROUGE = (228, 6, 6)
BLACK = (0, 0, 0)
