import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.RED + Back.YELLOW + " Bu Sarı, Kırmızı bir yazıdır.")
print("Varsayılan yazı örneği.")