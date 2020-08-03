import pandas as pd
import pdftables_api
import os
if not os.path.exists('test'):
    os.makedirs('test')
if not os.path.exists('excel'):
    os.makedirs('excel')
from parser_pdf import download_pdf
print("Файлы в формате pdf можете найти в папке test")
print("Файлы в формате xlsx можете найти в папке excel")
absdwdirname = os.path.abspath('test')
with open("settings.txt", 'r') as file:
    f = file.read().split("\n")
    key=f[0]
if key=='':key='00xa7kk2eja9'
print("ключ",key)
c = pdftables_api.Client(key)
dfs = pd.read_excel('inn.xlsx')
for i in dfs['ИНН'].tolist():
    if len(str(i))==12 or len(str(i))==10:
        download_pdf(i)

print("Завершено скачивание pdf файлов...Начинаем преобразование в xlsx")

for filename in os.listdir(absdwdirname):
    c.xlsx(os.path.join(absdwdirname,filename), os.path.join('excel',filename[:len(filename)-4]))

print("Процесс закончен!")