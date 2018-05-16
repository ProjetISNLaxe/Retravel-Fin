from pygame.constants import*
import pygame
def key(tch):
    keys=open("options\keys\\"+tch, "r")
    touche=keys.read()
    keys.close()
    if touche=="1":
        return K_BACKSPACE
    elif touche=="2":
        return K_TAB
    elif touche=="3":
        return K_CLEAR
    elif touche=="4":
        return K_RETURN
    elif touche=="5":
        return K_PAUSE
    elif touche=="6":
        return K_ESCAPE
    elif touche=="7":
        return K_SPACE
    elif touche=="8":
        return K_EXCLAIM
    elif touche=="9":
        return K_QUOTEDBL
    elif touche=="10":
        return K_HASH
    elif touche=="11":
        return K_DOLLAR
    elif touche=="12":
        return K_AMPERSAND
    elif touche=="13":
        return K_QUOTE
    elif touche=="14":
        return K_LEFTPAREN
    elif touche=="15":
        return K_RIGHTPAREN
    elif touche=="16":
        return K_ASTERISK
    elif touche=="17":
        return K_PLUS
    elif touche=="18":
        return K_COMMA
    elif touche=="19":
        return K_MINUS
    elif touche=="20":
        return K_PERIOD
    elif touche=="21":
        return K_SLASH
    elif touche=="22":
        return K_0
    elif touche=="23":
        return K_1
    elif touche=="24":
        return K_2
    elif touche=="25":
        return K_3
    elif touche=="26":
        return K_4
    elif touche=="27":
        return K_5
    elif touche=="28":
        return K_6
    elif touche=="29":
        return K_7
    elif touche=="30":
        return K_8
    elif touche=="31":
        return K_9
    elif touche=="32":
        return K_COLON
    elif touche=="33":
        return K_SEMICOLON
    elif touche=="34":
        return K_LESS
    elif touche=="35":
        return K_EQUALS
    elif touche=="36":
        return K_GREATER
    elif touche=="37":
        return K_QUESTION
    elif touche=="38":
        return K_AT
    elif touche=="39":
        return K_LEFTBRACKET
    elif touche=="40":
        return K_BACKSLASH
    elif touche=="41":
        return K_RIGHTBRACKET
    elif touche=="42":
        return K_CARET
    elif touche=="43":
        return K_UNDERSCORE
    elif touche=="44":
        return K_a
    elif touche=="45":
        return K_b
    elif touche=="46":
        return K_c
    elif touche=="47":
        return K_d
    elif touche=="48":
        return K_e
    elif touche=="49":
        return K_f
    elif touche=="50":
        return K_g
    elif touche=="51":
        return K_h
    elif touche=="52":
        return K_i
    elif touche=="53":
        return K_j
    elif touche=="54":
        return K_k
    elif touche=="55":
        return K_l
    elif touche=="56":
        return K_m
    elif touche=="57":
        return K_n
    elif touche=="58":
        return K_o
    elif touche=="59":
        return K_p
    elif touche=="60":
        return K_q
    elif touche=="61":
        return K_r
    elif touche=="62":
        return K_s
    elif touche=="63":
        return K_t
    elif touche=="64":
        return K_u
    elif touche=="65":
        return K_v
    elif touche=="66":
        return K_w
    elif touche=="67":
        return K_x
    elif touche=="68":
        return K_y
    elif touche=="69":
        return K_z
    elif touche=="70":
        return K_DELETE
    elif touche=="71":
        return K_KP0
    elif touche=="72":
        return K_KP1
    elif touche=="73":
        return K_KP2
    elif touche=="74":
        return K_KP3
    elif touche=="75":
        return K_KP4
    elif touche=="76":
        return K_KP5
    elif touche=="77":
        return K_KP6
    elif touche=="78":
        return K_KP7
    elif touche=="79":
        return K_KP8
    elif touche=="80":
        return K_KP9
    elif touche=="81":
        return K_KP_PERIOD
    elif touche=="82":
        return K_KP_DIVIDE
    elif touche=="83":
        return K_KP_MULTIPLY
    elif touche=="84":
        return K_KP_MINUS
    elif touche=="85":
        return K_KP_PLUS
    elif touche=="86":
        return K_KP_ENTER
    elif touche=="87":
        return K_KP_EQUALS
    elif touche == "88":
        return K_UP
    elif touche == "89":
        return K_DOWN
    elif touche == "90":
        return K_RIGHT
    elif touche == "91":
        return K_LEFT
    elif touche == "92":
        return K_INSERT
    elif touche == "93":
        return K_HOME
    elif touche == "94":
        return K_END
    elif touche == "95":
        return K_PAGEUP
    elif touche == "96":
        return K_PAGEDOWN
    elif touche == "97":
        return K_F1
    elif touche == "98":
        return K_F2
    elif touche == "99":
        return K_F3
    elif touche == "100":
        return K_F4
    elif touche == "101":
        return K_F5
    elif touche == "102":
        return K_F6
    elif touche == "103":
        return K_F7
    elif touche == "104":
        return K_F8
    elif touche == "105":
        return K_F9
    elif touche == "106":
        return K_F10
    elif touche == "107":
        return K_F11
    elif touche == "108":
        return K_F12
    elif touche == "109":
        return K_F13
    elif touche == "110":
        return K_F14
    elif touche == "111":
        return K_F15
    elif touche == "112":
        return K_NUMLOCK
    elif touche == "113":
        return K_CAPSLOCK
    elif touche == "114":
        return K_SCROLLOCK
    elif touche == "115":
        return K_RSHIFT
    elif touche == "116":
        return K_LSHIFT
    elif touche == "117":
        return K_RCTRL
    elif touche == "118":
        return K_LCTRL
    elif touche == "119":
        return K_RALT
    elif touche == "120":
        return K_LALT
    elif touche == "121":
        return K_RMETA
    elif touche == "122":
        return K_LMETA
    elif touche == "123":
        return K_LSUPER
    elif touche == "124":
        return K_RSUPER
    elif touche == "125":
        return K_MODE
    elif touche == "126":
        return K_HELP
    elif touche == "127":
        return K_PRINT
    elif touche == "128":
        return K_SYSREQ
    elif touche == "129":
        return K_BREAK
    elif touche == "130":
        return K_MENU
    elif touche == "131":
        return K_POWER
    elif touche == "132":
        return K_EURO
    elif touche == "133":
        return K_BACKQUOTE

