import random
import requests

def rand(n):#Рандом
    p=''
    sand = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(0,n):
        az = random.choice(sand)
        p+=az
    return p
def down (juz, path, id1d):#Путь с такими слешами /(Функция скачивания)
    filename = id1d+'.png'
    path1 = path + filename
    juz1 = requests.get(juz)
    with open(path1, 'wb')as f:
        f.write(juz1.content)
    pass