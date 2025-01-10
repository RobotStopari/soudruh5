MOVE_EMAIL = '''Milý soudruhu,
            
Jsi na tahu v naší úžasné partii Soudruhu, nezlob se. 
            
Na provedení svého tahu máš 24 hodin, jinak budeš nemilosrdně přeskočen.
            
S pozdravem,
Ivan Mládek and Tchýně'''

SAD = [7, 16, 21, 33, 45, 55, 70, 73, 81, 101, 120, 145, 165, 170, 205, 254, 275, 289, 305, 310, 347, 356, 394, 395, 397, 398, 399, 430, 432, 434]
HAPPY = [26, 64, 91, 106, 113, 129, 142, 148, 156, 178, 188, 217, 234, 248, 264, 268, 295, 322, 336, 362, 370, 384, 410, 422]
NO_PROVS = [132, 134, 136, 158, 160, 162]
PROVS = [131, 133, 135, 159, 161, 163]
MONEY_PLACES = [15, 29, 43, 56, 72, 86, 100, 115, 128, 143, 172, 186, 201, 215, 230, 244, 259, 273, 288, 303, 317, 332, 346, 361, 376, 390, 405, 419]
MONEY_PLACES_VALUES = [700, 750, 800, 850, 900, 950, 1000, 2500, 3500, 5000, 10000, 12000, 14000, 16000, 18000, 20000, 22000, 24000, 28000, 32000, 40000, 46000, 50000, 100000, 100000, 100000, 100000, 100000]

CATEGORIES = {
        ('1-BEZ', 'Bezpartijní'),
        ('2-KAN', 'Kandidát'),
        ('3-KOM', 'Člen Strany'),
        ('4-POS', 'Poslanec'),
        ('5-UV', 'Člen Ústředního Výboru'),
        ('6-POL', 'Člen Politbyra ÚV'),
        ('7-GEN', 'Generální Tajemník ÚV Strany'),
        }

EFFECTS = {
        ('happy', 'Vylepšení'),
        ('sad', 'Postih'),
        }

MAX_DICE = 6
KICK_OUT_MONEY = 100000
GAME_START_MONEY = 2000