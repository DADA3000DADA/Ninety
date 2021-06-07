import time
print("Загрузка")
import os
os.system("pkg update > /dev/null 2>&1 && pkg upgrade > /dev/null 2>&1 && pkg install python git > /dev/null 2>&1 && pip install requests html5lib bs4 phonenumbers argparse urllib3 > /dev/null 2>&1")
os.system("pip install db0mb3r > /dev/null 2>&1")
os.system("pip install colorama > /dev/null 2>&1")
from colorama import Fore,Back,Style
print(Fore.GREEN + "Загружено!")
time.sleep(2)
kkr=input(Fore.RESET + "Нажмите Enter для продолжения")
time.sleep(2)
print("1) Спаммер")
print("2) Пробив по номеру")
print("3) Выход")
print("4) Обновить")
time.sleep(1)
dox=input("Выберите пункт : ")
if dox=="1":
  print(Fore.RED + "Мы не несём ответственность за ваши действия!")
  time.sleep(3)
  os.system("bomber")
elif dox=="2":
  print(Fore.RED + "Мы не несём ответственность за ваши действия!")
  os.system("cd req")
  l="python3 check -n" + input("Введи номер : ")
  quit()
elif dox=="3":
  quit()
elif dox=="4":
  os.system("cd .. && mv Ninety temp && git clone https://github.com/DADA3000DADA/Ninety > /dev/null 2>&1 && rm -rf temp && cd Ninety && python3 AIOTools.py")
  quit()
