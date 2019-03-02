import sys
from glob import glob


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
    return glob("vtipy/*")


def main():
    """
    Vypíše všechny nalezené vtipy.
    """
    for vtip in seznam_vtipu():
        print("=" * 80)
        print(nacti_vtip(vtip))

if __name__ == "__main__":
    main()
