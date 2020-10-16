'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.8 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.6 #? měsíční gravitace
SPEED_OF_LIGHT = 1079252848.8 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 1235 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''
def zvukOkolo(SPEED_OF_SOUND):
    obvodZeme = 40003.2 #km
    cas = obvodZeme / SPEED_OF_SOUND
    print("Teoreticky by zvuku trvalo", cas, 'hodin, nez by obletel zemekouli.')

def velkeSvetlo(SPEED_OF_LIGHT):
    vzdalenost = 384400 #mesice od zeme
    casSvetla = vzdalenost / SPEED_OF_LIGHT
    casCelkovy = casSvetla * 60 * 60
    print("Kdyby jsme meli dost vykonny zdroj svetla dokazalo by se svetlo dostat na mesic za", casCelkovy, "sekund!")

zvukOkolo(SPEED_OF_SOUND)
velkeSvetlo(SPEED_OF_LIGHT)