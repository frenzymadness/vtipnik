import sys
import glob
import random


def nacti_vtip(cesta_ke_vtipu):
    """
    Když této funkci dáš jméno textového souboru ze složky vtipy,
    tak vrátí text vtipu jako řetězec.
    """
    try:
        with open(cesta_ke_vtipu, 'r', encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        sys.exit('Bohuzel soubor s vtipem neexistuje: {}'.format(cesta_ke_vtipu))


def seznam_vtipu():
    """
    Funkce načtě obsah složky a vrátí seznam všech dostupných vtipů
    """
    return glob.glob("vtipy/*")


def main():
    """
    Vypíše jeden náhodný vtip ze seznamu a po stisknutí Enteru vypíše další
    """
    ls_vtip=seznam_vtipu()
    for x in range(len(ls_vtip)):
       print("=" * 80) 
       vtip=random.choice(ls_vtip)
       print(nacti_vtip(vtip))
       ls_vtip.remove(vtip)
       if len(ls_vtip)==0:
           print('\n\nBohuzel jsi uz vsechny vtipy videl\n')
           break
        
       input("\nStisni Enter pro dalsi vtip\n")

if __name__ == "__main__":
    main()
