import time
print("Приветствую! Чтобы загрузить инструмент Хакера тебе нужно скачать файлы! Приступим")
kko=input("Чтобы начать загрузку нажмите Enter! : ")
time.sleep(2)
print("Разрешение получено!")
time.sleep(1)
print("Подключение серверов!")
time.sleep(7)
kkq=input("Выключите WiFi чтобы произошло подключение, затем нажмите Enter : ")
time.sleep(2)
print("Подключаем сервера Kali")
time.sleep(4)
print("Подключили!")
time.sleep(1)
print("Перезагружаем Termux")
time.sleep(2)
kkw=input("Нажмите Enter для перезагрузки Termux кэша")
time.sleep(2)
print("Перезагружаем")
time.sleep(4)
print("Перезагружено")
time.sleep(1)
print("Загружаем файлы и интерфэйс")
time.sleep(3)
kke=input("Нажмите Enter для загрузки файлов и интерфэйса")
time.sleep(2)
print("Загрузка")
import os
os.system("pkg update upgrade > dev/null 2>&1 && pkg install python git > dev/null 2>&1 && pip install requests html5lib bs4 phonenumbers argparse urllib3 colorama > dev/null 2>&1")
os.system("pip install db0mb3r")
from colorama import Fore,Back,Style
print(Fore.GREEN + "Загружено!")
time.sleep(14)
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
  print("Введи: python check -n ТУТНОМЕР(С +7)
  quit()
elif dox=="3":
  quit()
elif dox=="4":
  os.system("cd .. && rm -rf Ninety && git clone https://github.com/DADA3000DADA/Ninety > dev/null 2>&1")
  quit()
