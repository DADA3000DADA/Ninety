import time
import os
os.system("clear")

print()
print("Загрузка")
print("Первая загрузка может длиться больше 5 минут! Время загрузки зависит от вашей скорости интернета")
os.system("pkg update && pkg upgrade > dev/null 2>&1 && pkg install python git > dev/null 2>&1 && pip install requests html5lib bs4 phonenumbers argparse urllib3 colorama > dev/null 2>&1")
os.system("n")
os.system("pip install db0mb3r")
from colorama import Fore, Back, Style
print(Fore.GREEN + "Загружено!")
time.sleep(14)
kkr = input(Fore.RESET + "Нажмите Enter для продолжения")
time.sleep(2)
print("1) Спаммер")
print("2) Пробив по номеру")
print("3) Выход")
print("4) Обновить")
time.sleep(1)
dox = input("Выберите пункт : ")
if dox == "1":
    print(Fore.RED + "Мы не несём ответственность за ваши действия!")
    time.sleep(3)
    os.system("bomber")
elif dox == "2":
    print(Fore.RED + "Мы не несём ответственность за ваши действия!")
    Fore.RESET
    os.system("cd req")
    l=os.system("python check.py -n ") + str(input("Введи номер (С +7): "))
    os.system(l)
    quit()
elif dox == "3":
    quit()
elif dox == "4":
    os.system(
        "cd .. && mv Ninety temp && git clone https://github.com/DADA3000DADA/Ninety && rm -rf temp > dev/null 2>&1")
    quit()
