#       Импорты
from bs4 import BeautifulSoup
from colorama import Fore , Back , init , Style
import requests
from defs import * #ЭТО НЕ АНИМЕ
import time
import os
init()
#       Стандартные переменные
ROOT_DIR = os.path.dirname(__file__)
ROOT_DIR1 = ROOT_DIR + '\\'
spisok = 1
url='https://prnt.sc/'
i = int(input('Сколько раз делать парсинг(для бесконечного парсинга используйте 0): '))#        Переменная количества 
path = ROOT_DIR1 + 'result' + '\\'
headers = 'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)'#        ХЕДЕРЫ
#       Логика проверки папок
try:
    os.mkdir(path)
    print(Fore.RED + 'Директория созданна')
except OSError:
    print(Fore.RED + 'Директория существует')
print(Fore.CYAN+Style.BRIGHT+'Begin')
#       Прога
if i == 0:
    while True:#        Режим бесконечного парсинга
        id_pic = rand(6)
        a=url+id_pic
        reque = requests.get(a,headers={'user-agent':headers})
        soup = BeautifulSoup(reque.text, 'lxml')
        azws=soup.find('img').get('src')
        while True:#        Проверка удалённости файла
            if azws[:4] == 'http':
                down(azws,path, id_pic)
                print(Back.GREEN+Style.BRIGHT+'Файл '+id_pic+' успешно скачан')
                spisok+=1
                break
            else:
                print(Back.RED+Style.BRIGHT+'Файла '+id_pic+' не существует генерируем другой')
                id_pic = rand(6)
                a=url+id_pic
                reque = requests.get(a,headers={'user-agent':headers})
                soup = BeautifulSoup(reque.text, 'lxml')
                azws=soup.find('img').get('src')
                continue
else:#      Режим конечного парсинга   
    for i in range(0,i):
        id_pic = rand(6)
        a=url+id_pic
        reque = requests.get(a,headers={'user-agent':headers})
        soup = BeautifulSoup(reque.text, 'lxml')
        azws=soup.find('img').get('src')
        while True:#        Проверка удалённости файла
            if azws[:4] == 'http':
                down(azws,path, id_pic)
                print(Back.GREEN+Style.BRIGHT+str(spisok)+' Файл '+id_pic+' успешно скачан')
                spisok+=1
                break
            else:
                print(Back.RED+Style.BRIGHT+str(spisok)+' Файла '+id_pic +' не существует генерируем другой')
                id_pic = rand(6)
                a=url+id_pic
                reque = requests.get(a,headers={'user-agent':headers})
                soup = BeautifulSoup(reque.text, 'lxml')
                azws=soup.find('img').get('src')
                continue
#       Типо END
    print(Back.CYAN+Style.BRIGHT+'ALL')
    time.sleep(15)

