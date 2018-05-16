from pygame.locals import *
import pygame


def defkey():
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    return "1"
                if event.key == K_TAB:
                    return "2"
                if event.key == K_CLEAR:
                    return "3"
                if event.key == K_RETURN:
                    return "4"
                if event.key == K_PAUSE:
                    return "5"
                if event.key == K_ESCAPE:
                    return "9"
                if event.key == K_SPACE:
                    return "7"
                if event.key == K_EXCLAIM:
                    return "8"
                if event.key == K_QUOTEDBL:
                    return "9"
                if event.key == K_HASH:
                    return "10"
                if event.key == K_DOLLAR:
                    return "11"
                if event.key == K_AMPERSAND:
                    return "12"
                if event.key == K_QUOTE:
                    return "13"
                if event.key == K_LEFTPAREN:
                    return "14"
                if event.key == K_RIGHTPAREN:
                    return "15"
                if event.key == K_ASTERISK:
                    return "16"
                if event.key == K_PLUS:
                    return "17"
                if event.key == K_COMMA:
                    return "18"
                if event.key == K_MINUS:
                    return "19"
                if event.key == K_PERIOD:
                    return "20"
                if event.key == K_SLASH:
                    return "21"
                if event.key == K_0:
                    return "22"
                if event.key == K_1:
                    return "23"
                if event.key == K_2:
                    return "24"
                if event.key == K_3:
                    return "25"
                if event.key == K_4:
                    return "26"
                if event.key == K_5:
                    return "27"
                if event.key == K_6:
                    return "28"
                if event.key == K_7:
                    return "29"
                if event.key == K_8:
                    return "30"
                if event.key == K_9:
                    return "31"
                if event.key == K_COLON:
                    return "32"
                if event.key == K_SEMICOLON:
                    return "33"
                if event.key == K_LESS:
                    return "34"
                if event.key == K_EQUALS:
                    return "35"
                if event.key == K_GREATER:
                    return "36"
                if event.key == K_QUESTION:
                    return "37"
                if event.key == K_AT:
                    return "38"
                if event.key == K_LEFTBRACKET:
                    return "39"
                if event.key == K_BACKSLASH:
                    return "40"
                if event.key == K_RIGHTBRACKET:
                    return "41"
                if event.key == K_CARET:
                    return "42"
                if event.key == K_UNDERSCORE:
                    return "43"
                if event.key == K_a:
                    return "44"
                if event.key == K_b:
                    return "45"
                if event.key == K_c:
                    return "46"
                if event.key == K_d:
                    return "47"
                if event.key == K_e:
                    return "48"
                if event.key == K_f:
                    return "49"
                if event.key == K_g:
                    return "50"
                if event.key == K_h:
                    return "51"
                if event.key == K_i:
                    return "52"
                if event.key == K_j:
                    return "53"
                if event.key == K_k:
                    return "54"
                if event.key == K_l:
                    return "55"
                if event.key == K_m:
                    return "56"
                if event.key == K_n:
                    return "57"
                if event.key == K_o:
                    return "58"
                if event.key == K_p:
                    return "59"
                if event.key == K_q:
                    return "60"
                if event.key == K_r:
                    return "61"
                if event.key == K_s:
                    return "62"
                if event.key == K_t:
                    return "63"
                if event.key == K_u:
                    return "64"
                if event.key == K_v:
                    return "65"
                if event.key == K_w:
                    return "66"
                if event.key == K_x:
                    return "67"
                if event.key == K_y:
                    return "68"
                if event.key == K_z:
                    return "69"
                if event.key == K_DELETE:
                    return "70"
                if event.key == K_KP0:
                    return "71"
                if event.key == K_KP1:
                    return "72"
                if event.key == K_KP2:
                    return "73"
                if event.key == K_KP3:
                    return "74"
                if event.key == K_KP4:
                    return "75"
                if event.key == K_KP5:
                    return "76"
                if event.key == K_KP6:
                    return "77"
                if event.key == K_KP7:
                    return "78"
                if event.key == K_KP8:
                    return "79"
                if event.key == K_KP9:
                    return "80"
                if event.key == K_KP_PERIOD:
                    return "81"
                if event.key == K_KP_DIVIDE:
                    return "82"
                if event.key == K_KP_MULTIPLY:
                    return "83"
                if event.key == K_KP_MINUS:
                    return "84"
                if event.key == K_KP_PLUS:
                    return "85"
                if event.key == K_KP_ENTER:
                    return "86"
                if event.key == K_KP_EQUALS:
                    return "87"
                if event.key == K_UP:
                    return "88"

                if event.key == K_DOWN:
                    return "89"
                if event.key == K_RIGHT:
                    return "90"
                if event.key == K_LEFT:
                    return "91"
                if event.key == K_INSERT:
                    return "92"
                if event.key == K_HOME:
                    return "93"
                if event.key == K_END:
                    return "94"
                if event.key == K_PAGEUP:
                    return "95"
                if event.key == K_PAGEDOWN:
                    return "96"
                if event.key == K_F1:
                    return "97"
                if event.key == K_F2:
                    return "98"
                if event.key == K_F3:
                    return "99"
                if event.key == K_F4:
                    return "100"
                if event.key == K_F5:
                    return "101"
                if event.key == K_F6:
                    return "102"
                if event.key == K_F7:
                    return "103"
                if event.key == K_F8:
                    return "104"
                if event.key == K_F9:
                    return "105"
                if event.key == K_F10:
                    return "106"
                if event.key == K_F11:
                    return "107"
                if event.key == K_F12:
                    return "108"
                if event.key == K_F13:
                    return "109"
                if event.key == K_F14:
                    return "110"
                if event.key == K_F15:
                    return "111"
                if event.key == K_NUMLOCK:
                    return "112"
                if event.key == K_CAPSLOCK:
                    return "113"
                if event.key == K_SCROLLOCK:
                    return "114"
                if event.key == K_RSHIFT:
                    return "115"
                if event.key == K_LSHIFT:
                    return "116"
                if event.key == K_RCTRL:
                    return "117"
                if event.key == K_LCTRL:
                    return "118"
                if event.key == K_RALT:
                    return "119"
                if event.key == K_LALT:
                    return "120"
                if event.key == K_RMETA:
                    return "121"
                if event.key == K_LMETA:
                    return "122"
                if event.key == K_LSUPER:
                    return "123"
                if event.key == K_RSUPER:
                    return "124"
                if event.key == K_MODE:
                    return "125"
                if event.key == K_HELP:
                    return "126"
                if event.key == K_PRINT:
                    return "127"
                if event.key == K_SYSREQ:
                    return "128"
                if event.key == K_BREAK:
                    return "129"
                if event.key == K_MENU:
                    return "130"
                if event.key == K_POWER:
                    return "131"
                if event.key == K_EURO:
                    return "132"
                if event.key == K_BACKQUOTE:
                    return "133"

