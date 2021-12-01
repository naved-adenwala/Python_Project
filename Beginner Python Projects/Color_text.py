#Module
import colorama
from colorama import Fore,Back,Style
#initializing
colorama.init(autoreset=True)
#setting background color and foreground color
print(Fore.BLACK + Back.RED+"My Name IS "+Fore.BLACK + Back.GREEN + "Naved")
print(Fore.BLUE + 'Blue Color')
print('Normal text')
print(Style.RESET_ALL)