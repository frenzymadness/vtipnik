import sys
from glob import glob
import random


def nacti_vtip(cesta_ke_vtipu):
    """
    Když této funkci dáš jméno textového souboru ze složky vtipy,
    tak vrátí text vtipu jako řetězec.
    """
    try:
        with open(cesta_ke_vtipu, 'r', encoding = "utf-8") as f:
            return f.read()
    except FileNotFoundError:
        sys.exit('Bohuzel soubor s vtipem neexistuje: {}'.format(cesta_ke_vtipu))


def seznam_vtipu():
    """
    Funkce načtě obsah složky a vrátí seznam všech dostupných vtipů
    """
    return glob("vtipy/*")


def main():
    """
    Vypíše jeden náhodný vtip ze seznamu a po stisknutí Enteru vypíše další
    """
    list_vtipu = seznam_vtipu()
    while len(list_vtipu)>0:
       print("=" * 80) 
       vtip = random.choice(list_vtipu)
       print(nacti_vtip(vtip))
       list_vtipu.remove(vtip)
       input("\nStiskni Enter pro dalsi vtip\n")
    print('\n\nBohuzel jsi uz vsechny vtipy videl\n')
        
if __name__ == "__main__":
    main()
