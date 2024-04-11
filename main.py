import random
import string
import os
import platform

from os import system
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
colorama_init()

lettere = string.ascii_lowercase
lettereG = string.ascii_uppercase
numeri = string.digits
char = string.punctuation

def clear():
    if "Windows" in platform.platform():
        os.system("cls")
    else:
        os.system("clear")

system("title " + "PASSGEN BY KriEU (Kristian Tortora)")


clear()

print(f"""

     __    __  _____  
    (  \  /  )(_   _) 
     \ (__) /   | |   
      ) __ (    | |   
     ( (  ) )   | |   
      ) )( (   _| |__ 
     /_/  \_\ /_____( 

    By KriEU (Kristian Tortora)

    Please insert your language 
      
    Language available is:

          {Fore.GREEN}I{Fore.WHITE}T{Fore.RED}A{Fore.WHITE}: Italian
          {Fore.RED}E{Fore.WHITE}N{Fore.BLUE}G{Fore.WHITE}: English

""")

lang = input("Insert your language please: ")

if lang == "ITA":
    def run(grandezza, funzione):
        print(f"La tua password di {grandezza} Chars è {''.join(random.choice(funzione) for i in range(grandezza))}")
    clear()
    print(f"""

    LINGUA SCELTA INGLESE

    {Fore.LIGHTWHITE_EX}

     ______    _____     __      _ __    __   _____     __      _ __    __ ________  ____    
    (_   _ \  / ___/    /  \    / )) )  ( (  / ___/    /  \    / )) )  ( ((___  ___)/ __ \   
      ) (_) )( (__     / /\ \  / /( (    ) )( (__     / /\ \  / /( (    ) )   ) )  / /  \ \  
      \   _/  ) __)    ) ) ) ) ) ) \ \  / /  ) __)    ) ) ) ) ) ) ) )  ( (   ( (  ( ()  () ) 
      /  _ \ ( (      ( ( ( ( ( (   \ \/ /  ( (      ( ( ( ( ( ( ( (    ) )   ) ) ( ()  () ) 
     _) (_) ) \ \___  / /  \ \/ /    \  /    \ \___  / /  \ \/ /  ) \__/ (   ( (   \ \__/ /  
    (______/   \____\(_/    \__/      \/      \____\(_/    \__/   \______/   /__\   \____/   

    By KriEU (Kristian Tortora)

    {Fore.LIGHTCYAN_EX}Seleziona uno dei numeri a sinistra per selezionare la modalità del programma:

    {Fore.LIGHTBLUE_EX}1. {Fore.WHITE}Normale (Genera solo lettere Livello: Non è tanto efficente)
    {Fore.LIGHTBLUE_EX}2. {Fore.WHITE}Alto (Genera Lettere e Numeri Livello: Efficente)
    {Fore.LIGHTBLUE_EX}3. {Fore.WHITE}Elevato (Genera Lettere, Numeri e Caratteri speciali Livello: Elevato)

    {Style.RESET_ALL}               
    """)

    scelta = int(input())

    match scelta:
        case 1:
            run(int(input("Grandezza? ")), lettere + lettereG)
        case 2:
            run(int(input("Grandezza? ")), lettere + lettereG + numeri)
        case 3:
            run(int(input("Grandezza? ")), lettere + lettereG + numeri + char)
        case _:
            print(f"{Fore.RED}Per faovre Inserisci la sintassi giusta! {Style.RESET_ALL}")
elif lang == "ENG":
    def run(grandezza, funzione):
        print(f"Your password of {grandezza} Chars is {''.join(random.choice(funzione) for i in range(grandezza))}")


    clear()
    print(f"""

    LANGUAGE CHOICE ENGLISH

    {Fore.LIGHTWHITE_EX}

     ___       ___  _____   _____       ____  ____    __    __    _____  
    (  (       )  )/ ___/  (_   _)     / ___)/ __ \   \ \  / /   / ___/  
     \  \  _  /  /( (__      | |      / /   / /  \ \  () \/ ()  ( (__    
      \  \/ \/  /  ) __)     | |     ( (   ( ()  () ) / _  _ \   ) __)   
       )   _   (  ( (        | |   __( (   ( ()  () )/ / \/ \ \ ( (      
       \  ( )  /   \ \___  __| |___) )\ \___\ \__/ //_/      \_\ \ \___  
        \_/ \_/     \____\ \________/  \____)\____/(/          \) \____\ 
                                                                       
    By KriEU (Kristian Tortora)

    {Fore.LIGHTCYAN_EX}Select one of the numbers on the left to select the program mode:

    {Fore.LIGHTBLUE_EX}1. {Fore.WHITE}Normal (Generates only letters Level: Not so efficient)
    {Fore.LIGHTBLUE_EX}2. {Fore.WHITE}High (Generates Letters and Numbers Level: Effective)
    {Fore.LIGHTBLUE_EX}3. {Fore.WHITE}Elevated (Generates Letters, Numbers and Special Characters Level: Elevated)

    {Style.RESET_ALL}               
    """)

    scelta = int(input())

    match scelta:
        case 1:
            run(int(input("Size? ")), lettere + lettereG)
        case 2:
            run(int(input("Size? ")), lettere + lettereG + numeri)
        case 3:
            run(int(input("Size? ")), lettere + lettereG + numeri + char)
        case _:
            print(f"{Fore.RED}Please Enter the right syntax! {Style.RESET_ALL}")

else:
    print(f"{Fore.RED}Please Enter the right syntax! {Style.RESET_ALL}")