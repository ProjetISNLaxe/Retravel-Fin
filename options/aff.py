from pygame.locals import *


def affichetouche(tch):
    keys = open("options\keys\\" + tch, "r")
    touche = keys.read()
    keys.close()
    if touche == "1":
        return "BackSpace"
    elif touche == "2":
        return "Tab"
    elif touche == "3":
        return "Clear"  # K_CLEAR
    elif touche == "4":
        return "Return"  # K_RETURN
    elif touche == "5":
        return "Pause"  # K_PAUSE
    elif touche == "6":
        return "Escape"  # K_ESCAPE
    elif touche == "7":
        return "Space"  # K_SPACE
    elif touche == "8":
        return "!"  # K_EXCLAIM
    elif touche == "9":
        return "\""  # K_QUOTEDBL
    elif touche == "10":
        return "#"  # K_HASH
    elif touche == "11":
        return "$"  # K_DOLLAR
    elif touche == "12":
        return "&"  # K_AMPERSAND
    elif touche == "13":
        return "\'"  # K_QUOTE
    elif touche == "14":
        return "("  # K_LEFTPAREN
    elif touche == "15":
        return ")"  # K_RIGHTPAREN
    elif touche == "16":
        return "*"  # K_ASTERISK
    elif touche == "17":
        return "+"  # K_PLUS
    elif touche == "18":
        return ","  # K_COMMA
    elif touche == "19":
        return "-"  # K_MINUS
    elif touche == "20":
        return "."  # K_PERIOD
    elif touche == "21":
        return "/"  # K_SLASH
    elif touche == "22":
        return "0"  # K_0
    elif touche == "23":
        return "1"  # K_1
    elif touche == "24":
        return "2"  # K_2
    elif touche == "25":
        return "3"  # K_3
    elif touche == "26":
        return "4"  # K_4
    elif touche == "27":
        return "5"  # K_5
    elif touche == "28":
        return "6"  # K_6
    elif touche == "29":
        return "7"  # K_7
    elif touche == "30":
        return "8"  # K_8
    elif touche == "31":
        return "9"  # K_9
    elif touche == "32":
        return ":"  # K_COLON
    elif touche == "33":
        return ";"  # K_SEMICOLON
    elif touche == "34":
        return "<"  # K_LESS
    elif touche == "35":
        return "="  # K_EQUALS
    elif touche == "36":
        return ">"  # K_GREATER
    elif touche == "37":
        return "?"  # K_QUESTION
    elif touche == "38":
        return "@"  # K_AT
    elif touche == "39":
        return "["  # K_LEFTBRACKET
    elif touche == "40":
        return "\\"  # K_BACKSLASH
    elif touche == "41":
        return "]"  # K_RIGHTBRACKET
    elif touche == "42":
        return "^"  # K_CARET
    elif touche == "43":
        return "_"  # K_UNDERSCORE
    elif touche == "44":
        return "a"  # K_a
    elif touche == "45":
        return "b"  # K_b
    elif touche == "46":
        return "c"  # K_c
    elif touche == "47":
        return "d"  # K_d
    elif touche == "48":
        return "e"  # K_e
    elif touche == "49":
        return "f"  # K_f
    elif touche == "50":
        return "g"  # K_g
    elif touche == "51":
        return "h"  # K_h
    elif touche == "52":
        return "i"  # K_i
    elif touche == "53":
        return "j"  # K_j
    elif touche == "54":
        return "k"  # K_k
    elif touche == "55":
        return "l"  # K_l
    elif touche == "56":
        return "m"  # K_m
    elif touche == "57":
        return "n"  # K_n
    elif touche == "58":
        return "o"  # K_o
    elif touche == "59":
        return "p"  # K_p
    elif touche == "60":
        return "q"  # K_q
    elif touche == "61":
        return "r"  # K_r
    elif touche == "62":
        return "s"  # K_s
    elif touche == "63":
        return "t"  # K_t
    elif touche == "64":
        return "u"  # K_u
    elif touche == "65":
        return "v"  # K_v
    elif touche == "66":
        return "w"  # K_w
    elif touche == "67":
        return "x"  # K_x
    elif touche == "68":
        return "y"  # K_y
    elif touche == "69":
        return "z"  # K_z
    elif touche == "70":
        return "Suppr"  # K_DELETE
    elif touche == "71":
        return "Num 0"  # K_KP0
    elif touche == "72":
        return "Num 1"  # K_KP1
    elif touche == "73":
        return "Num 2"  # K_KP2
    elif touche == "74":
        return "Num 3"  # K_KP3
    elif touche == "75":
        return "Num 4"  # K_KP4
    elif touche == "76":
        return "Num 5"  # K_KP5
    elif touche == "77":
        return "Num 6"  # K_KP6
    elif touche == "78":
        return "Num 7"  # K_KP7
    elif touche == "79":
        return "Num 8"  # K_KP8
    elif touche == "80":
        return "Num 9"  # K_KP9
    elif touche == "81":
        return "Num ."  # K_KP_PERIOD
    elif touche == "82":
        return "Num /"  # K_KP_DIVIDE
    elif touche == "83":
        return "Num *"  # K_KP_MULTIPLY
    elif touche == "84":
        return "Num -"  # K_KP_MINUS
    elif touche == "85":
        return "Num +"  # K_KP_PLUS
    elif touche == "86":
        return "Num Enter"  # K_KP_ENTER
    elif touche == "87":
        return "Num ="  # K_KP_EQUALS
    elif touche == "88":
        return "↑"  # K_UP
    elif touche == "89":
        return "↓"  # K_DOWN
    elif touche == "90":
        return "→"  # K_RIGHT
    elif touche == "91":
        return "←"  # K_LEFT
    elif touche == "92":
        return "Inser"  # K_INSERT
    elif touche == "93":
        return "Home"  # K_HOME
    elif touche == "94":
        return "End"  # K_END
    elif touche == "95":
        return "⇞"  # K_PAGEUP
    elif touche == "96":
        return "⇟"  # K_PAGEDOWN
    elif touche == "97":
        return "F1"  # K_F1
    elif touche == "98":
        return "F2"  # K_F2
    elif touche == "99":
        return "F3"  # K_F3
    elif touche == "100":
        return "F4"  # K_F4
    elif touche == "101":
        return "F5"  # K_F5
    elif touche == "102":
        return "F6"  # K_F6
    elif touche == "103":
        return "F7"  # K_F7
    elif touche == "104":
        return "F8"  # K_F8
    elif touche == "105":
        return "F9"  # K_F9
    elif touche == "106":
        return "F10"  # K_F10
    elif touche == "107":
        return "F11"  # K_F11
    elif touche == "108":
        return "F12"  # K_F12
    elif touche == "109":
        return "F13"  # K_F13
    elif touche == "110":
        return "F14"  # K_F14
    elif touche == "111":
        return "F15"  # K_F15
    elif touche == "112":
        return "Num Lock"  # K_NUMLOCK
    elif touche == "113":
        return "Caps Lock"  # K_CAPSLOCK
    elif touche == "114":
        return "Scroll Lock"  # K_SCROLLOCK
    elif touche == "115":
        return "R ⇑"  # K_RSHIFT
    elif touche == "116":
        return "L ⇑"  # K_LSHIFT
    elif touche == "117":
        return "R Ctrl"  # K_RCTRL
    elif touche == "118":
        return "L Ctrl"  # K_LCTRL
    elif touche == "119":
        return "R Alt"  # K_RALT
    elif touche == "120":
        return "L ALt"  # K_LALT
    elif touche == "121":
        return "R Meta"  # K_RMETA
    elif touche == "122":
        return "L Meta"  # K_LMETA
    elif touche == "123":
        return "L Windows"  # K_LSUPER
    elif touche == "124":
        return "R Windows"  # K_RSUPER
    elif touche == "125":
        return "Mode"  # K_MODE
    elif touche == "126":
        return "Help"  # K_HELP
    elif touche == "127":
        return "Screen"  # K_PRINT
    elif touche == "128":
        return "Sysrq"  # K_SYSREQ
    elif touche == "129":
        return "Break"  # K_BREAK
    elif touche == "130":
        return "Menu"  # K_MENU
    elif touche == "131":
        return "Power"  # K_POWER
    elif touche == "132":
        return "Euro"  # K_EURO
    elif touche == "133":
        return "`"  # K_BACKQUOTE
