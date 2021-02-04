import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Blue text on  Yellow Background
print(Fore.BLUE+Back.YELLOW+"Hi, My name is Prabhav Bajaj")
# Yellow text on Blue Background
print(Fore.YELLOW+Back.BLUE+"I am a first year mechanical engineering student at Punjab Engineering College")
# White Text On Cyan Colored Background
print(Back.CYAN+"I am passionate dreamer.")
#Bright text
print(Style.BRIGHT+Back.RED+"I am From Saharanpur")

