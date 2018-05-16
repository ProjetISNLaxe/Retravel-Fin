from pygame.constants import *
import sys
sys.path.append("options")
from selkey import key

# CONSTANTES TOUCHES
TIR = key("shtt")
HAUT = key("fw")
DROITE = key("rght")
GAUCHE = key("lft")
BAS = key("bw")
PAUSE = key("pause")

# CONSTANTES SCORE
SCORE_BASE = 0
SCORE_ENNEMI_2 = 10
ENNEMI_1_ZIGZAG = 20
SCORE_MINIBOSS = 50

# VITESSE DEPLACEMENT
VITESSE_PERSO = 6
VITESSE_ENNEMI_1 = 3.25
VITESSE_ENNEMI_2_Y = 3.25
VITESSE_ENNEMI_2_X = 2
VITESSE_FOND = 2

# VIE
VIE_PERSO = 5
