"""
Datum vytvorenia: 18.8.2020
Autor: Brian Turza
"""

import os
from colorama import *

HOME_PATH = '/home/student01/BrianTurza/znamky/'

def login():
    name = input("Zadajte pouzivatelske meno:")
    from getpass import getpass
    password = getpass("Zadajte pouzivatelske heslo:")
    if name == "admin" and password == "test123":
        pass
    else:
        print(Fore.RED + "Nespravne meno alebo heslo!" + Fore.WHITE)
        quit()

def check(triedu="", predmet="", meno=""):
    out = False
    count = 0
    predmety, triedy = [], []
    for i in next(os.walk(HOME_PATH))[1]:
        predmety.append(i)

    for i in next(os.walk(HOME_PATH + predmety[0]))[1]:
        triedy.append(i)

    if triedu:
        if triedu in triedy: out = True
        else: return False

    if predmet:
        if predmet in predmety: out = True
        else: return False
    
    if meno:
        for i in triedy:
            try:
                f = open(HOME_PATH + predmety[0] + "/" + i + "/" + meno.lower() + ".txt", "r") 
                out = True
                count += 1
            except FileNotFoundError:
                pass
    
    if count == 0 and meno:
        return False
    return out

def vstup(inp, kat=""):
    i = ""
    i = input(inp)
    print("-", i)
    while i == "":
        print(Fore.RED + "Vstup nesmie byt prazdny" + Fore.WHITE)
        i = input(inp)

    if kat == "triedu":
        if check(triedu=i):
            return i
        else:
            print(Fore.RED + "Nespravny vstup!" + Fore.WHITE)

        while check(triedu=i) != True:
            i = input(inp)
            print(Fore.RED + "Nespravny vstup!" + Fore.WHITE)  
    
    elif kat == "predmet":
        if check(predmet=i):
            return i 
        else:
            print(Fore.RED + "Nespravny vstup!" + Fore.WHITE)

        while check(predmet=i) != True:  
            i = input(inp)
            print(Fore.RED + "Nespravny vstup!" + Fore.WHITE) 


    elif kat == "meno":
        if check(meno=i):
            return i
        else:
            print(Fore.RED + "Nespravny vstup!" + Fore.WHITE)

        while check(meno=i) != True:
            i = input(inp)
            print(Fore.RED + "Nespravny vstup!" + Fore.WHITE) 

    return i

################################# Ziaci #######################################

def ukaz_znamky(trieda, predmet, meno):
    if check(triedu=trieda, predmet=predmet, meno=meno) == False:
        return "\nNespravne parametre!"
    try:
        path = "znamky/" + predmet + "/" + trieda + "/" + meno + ".txt"
        f = open(path, "r")
    except FileNotFoundError:
        return "Ziak s menom '" + meno + "' sa nenasiel v triede '" + trieda + "'"
    znamky = f.read().split()
    if len(znamky) == 0: return "\nTento ziak nema ziadne znamky v tomto predmete"
    else:
        return "Znamky: {}".format ("".join([str(i) + " " for i in znamky]))

def pridaj_znamku(trieda, predmet, meno):
    if check(triedu=trieda, predmet=predmet, meno=meno) == False:
        return "\nNespravne parametre!"
    
    try:
        path = "znamky/" + predmet + "/" + trieda + "/" + meno + ".txt"
        f = open(path, "a")
    except FileNotFoundError:
        f = open(path, "w")
    
    znamky = vstup("zadaj nove znamky (odel medzerou):")
    for i in znamky.split():
        f.write(f"{i} ")
    return "Hotovo"

def zmen_znamky(trieda, predmet, meno):
    if check(triedu=trieda, predmet=predmet, meno=meno) == False:
        return "\nNespravne parametre!"

    path = "znamky/" + predmet + "/" + trieda + "/" + meno + ".txt"
    f = open(path, "w")
    
    znamky = vstup("zadaj znamky (odel medzerou):")
    for i in znamky.split():
        f.write(f"{i} ")
    return "Hotovo"

def vytvor_ziaka(meno, trieda):
    predmety = []
    for i in next(os.walk('/home/student01/BrianTurza/znamky'))[1]:
        predmety.append(HOME_PATH + i + "/")
    
    for x in predmety:
        f = open(x + trieda + "/" + meno.lower() + ".txt", "w")
    
    return f"Hotovo. Ziak '{meno}' bol vytvoreny"

def zmaz_ziaka(meno, trieda):

    predmety = []
    for i in next(os.walk('/home/student01/BrianTurza/znamky'))[1]:
        predmety.append(HOME_PATH + i + "/")
    
    for x in predmety:
        shutil.rmtree(x + trieda + "/" + meno.lower() + ".txt")
    
    return f"Hotovo. Ziak '{meno}' bol zmazany"


def zobraz_ziakov(trieda):
    ziaci, predmety = [], []
    for i in next(os.walk(HOME_PATH))[1]:
        predmety.append(i)
        break
    for i in os.listdir(HOME_PATH + predmety[0] + "/" + trieda):
        ziaci.append(i[:-4])
    
    return ziaci 

def premenuj_ziaka(meno, nove, trieda):
    try:
        os.rename(f"{HOME_PATH}Informatika/{meno}", f"{HOME_PATH}Informatika/{nove}")
    except:
        return "Nespravne parametre!"

#-----------------------------------------------------------------------------

############################## PREDMET ######################################

def zobraz_predmety():
    return next(os.walk(HOME_PATH))[1]

def vytvor_predmet(predmet):
    if isinstance(predmet, int):
        return "\nNespravne parametre!"

    os.makedirs("znamky/" + predmet)
    for trieda in next(os.walk(HOME_PATH + Matematika))[1]:
        os.makedirs("znamky/" + predmet + "/" + trieda)

    return f"Predmet '{predmet}' vytvoreny"

def zmaz_predmet(predmet):
    if isinstance(predmet, int):
        return "\nNespravne parametre!"

    shutil.rmtree(HOME_PATH + predmet)

    return "Hotovo"

def premenuj_predmet(predmet, novy_predmet):
    if check(predmet=predmet):
        return "\nNespravne parametre!"
    try:
        os.rename(f"{HOME_PATH}{predmet}", f"{HOME_PATH}{novy_predmet}")
    except:
        return "Nespravne parametre!"
    return "Hotovo"

#----------------------------------------------------------------------------

############################## TRIEDA #######################################
def vytvor_triedu(triedu):
    if isinstance(triedu, int):
        return "\nNespravne parametre!"


    for predmet in next(os.walk('/home/student01/BrianTurza/znamky'))[1]:
        os.makedirs("znamky/" + predmet + "/" + triedu)

    return "Hotovo. Trieda '{}' vytvorena".format (triedu)

def zmaz_triedu(trieda):
    if isinstance(trieda, int):
        return "\nNespravne parametre!"

    for predmet in next(os.walk('/home/student01/BrianTurza/znamky'))[1]:
        os.remove("znamky/" + predmet + "/" + trieda)

def premenuj_triedu(trieda, nova_trieda):
    if isinstance(trieda, int) or isinstance(nova_trieda, int):
        return "\nNespravne parametre!"

    for predmet in next(os.walk('/home/student01/BrianTurza/znamky'))[1]:
        os.rename(f"{predmet}{trieda}", f"{predmet}{nova_trieda}")
    return "Hotovo"

def zobraz_triedy():
    triedy, predmety = [], []
    for i in next(os.walk(HOME_PATH))[1]:
        predmety.append(i)
        break

    for i in next(os.walk(HOME_PATH + predmety[0]))[1]:
        triedy.append(i)
    return triedy

#--------------------------------------------------------------------------

def main():
    login()
    kategoria = ""

    while kategoria != "exit":
        art = """
  ______            _           _  __      _     _         
 |__  (_) __ _  ___| | ____ _  | |/ /_ __ (_)___| | ____ _ 
   / /| |/ _` |/ __| |/ / _` | | ' /| '_ \| |_  / |/ / _` |
  / /_| | (_| | (__|   < (_| | | . \| | | | |/ /|   < (_| |
 /____|_|\__,_|\___|_|\_\__,_| |_|\_\_| |_|_/___|_|\_\__,_|
"""
        print(art)
        print("-------------------------------------\n")
        print("Vyberte is z nasledujucich kategorii:")
        print("1. Ziaci\n" + "2. Predmety\n" + "3. Triedy\n")
    
        kategoria = vstup("Kategoria:")

        if kategoria in ["1.", "1"]:
            print("1. Vytvor ziaka\n" + "2. Zmaz ziaka\n" + "3. Ukaz znamky ziaka\n" + "4. Pridaj znamky ziakovi\n" +  "5. Zmen znamky ziaka\n" + "6. Spat")

        elif kategoria in ["2.", "2"]:
            print("1. Vytvor predmet\n" + "2. Zmaz predmet\n" + "3. Premenuj predmet\n" + "4. Zobraz Predmety" + "5. Spat")
        
        elif kategoria in ["3.", "3"]:
            print("1. Vytvor triedu\n" + "2. Zmaz triedu\n" + "3. Premenuj triedu\n" + "4. Spat")
        
        elif kategoria == "exit": quit()

        else:
            print(Fore.RED + "Nespravny vstup!" + Fore.WHITE)
            continue

        m = False
        while m != True and kategoria in ["1.", "1"]:
            moznost = vstup("Vyberte moznost:", kat="mozost")

            if moznost in ["1.", "1"]:
                meno, trieda = "", ""
                def m1():
                    meno = vstup("Zadajte meno ziaka:", kat="moznost")
                    trieda = vstup("Zadajte triedu:", kat="triedu")
                m1()
                print(vytvor_ziaka(meno, trieda))
                break
                continue

            elif moznost in ["2.", "2"]:
                meno, trieda = "", ""
                def m2():
                    trieda = vstup("Vyberte si triedu ({}):".format(", ".join(zobraz_triedy())), kat="triedu")
                    meno = vstup("Zadajte meno ziaka ({}):".format(", ".join(zobraz_ziakov(trieda))), kat="meno")
                m2()
                print(zmaz_ziaka(meno, trieda))
                break
                continue

                
            elif moznost in ["3.", "3"]:
                meno, trieda, predmet = "", "", ""
                def m3():
                    trieda = vstup("Vyberte si triedu ({}):".format(", ".join(zobraz_triedy())), kat="triedu")
                    predmet = vstup("Vyber predmet ({}):".format(", ".join (zobraz_predmety())), kat="predmet")
                    meno = vstup("Zadajte meno ziaka ({}):".format(", ".join(zobraz_ziakov(trieda))), kat="meno")
                    print(ukaz_znamky(trieda, predmet, meno))
                m3()
                
                break
                continue

            elif moznost in ["4.", "4"]:
                trieda = vstup("Vyberte si triedu ({}):".format(", ".join(zobraz_triedy())), kat="triedu")
                predmet = vstup("Vyber predmet ({}):".format(", ".join (zobraz_predmety())), kat="predmet")
                meno = vstup("Zadajte meno ziaka ({}):".format(", ".join(zobraz_ziakov(trieda))), kat="meno")
                print(pridaj_znamku(trieda, predmet, meno))
                break
                continue

            elif moznost in ["5.", "5"]:
                trieda = vstup("Vyberte si triedu ({}):".format(", ".join(zobraz_triedy())), kat="triedu")
                predmet = vstup("Vyber predmet ({}):".format(", ".join (zobraz_predmety())), kat="predmet")
                meno = vstup("Zadajte meno ziaka ({}):".format(", ".join(zobraz_ziakov(trieda))), kat="meno")
                print(zmen_znamky(trieda, predmet, meno))
                break
                continue
                

            elif moznost in ["6.", "6"]:
                break
                continue


        while m != True and kategoria in ["2.", "2"]:
            moznost = vstup("Vyberte moznost:", kat="mozost")
            if moznost in ["1.", "1"]:
                meno = vstup("Zadajte meno noveho predmetu:", kat="predmet")
                print(vytvor_predmet(meno))
                break
                continue


            elif moznost in ["2.", "2"]:
                predmet = vstup("Vyber predmet ({}):".format(", ".join (zobraz_predmety())), kat="predmet")
                print(zmaz_predmet(predmet))
                break
                continue    
        
            elif moznost in ["3.", "3"]:
                predmet = vstup("Vyber predmet ({}):".format(", ".join (zobraz_predmety())), kat="predmet")
                p2 = vstup("Zadajte nove meno predmetu:")
                print(premenuj_predmet(predmet, p2))
                break
                continue
                

            elif moznost == ["4.", "4"]:
                print(zobraz_predmety()) 
                break
                continue

            elif moznost in ["5.", "5"]:
                break
                continue     

        while m != True and kategoria in ["3.", "3"]:
            moznost = vstup("Vyberte moznost:", kat="mozost")
            if moznost in ["1.", "1"]:
                trieda = vstup("Vyberte si triedu ({}):".format(", ".join(zobraz_triedy())), kat="triedu")
                print(vytvor_triedu(trieda))
                break
                continue

            elif moznost in ["2.", "2"]:
                trieda = vstup("Vyberte si triedu ({}):".format(", ".join(zobraz_triedy())), kat="triedu")
                print(zmaz_predmet(trieda))
                break
                continue

            elif moznost in ["3.", "3"]:
                trieda = vstup("Vyberte si triedu ({}):".format(", ".join(zobraz_triedy())), kat="triedu")
                t2 = vstup("Zadajte nove meno triedy:")
                print(premenuj_predmet(trieda, t2))
                break
                continue

            elif moznost in ["4.", "4"]:
                break
                continue
        
        
        

if __name__ == "__main__":
    main()
