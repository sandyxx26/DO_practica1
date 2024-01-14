import json
import zipfile
import os

api_token = {"username": "sandracisneros", "key": "550d4830e11a99da432b270ac1dc75d4"}
##para conectar a kaggle
with open("C:/Windows/System32/config/systemprofile/.kaggle/kaggle.json","w") as file:
    json.dump(api_token,file)
location = "C:/Users/fcisn/Documents/MURUMURU/practica_do1/data/dataset"

##validar si la carpeta existe
if not os.path.exists(location):
    ##si no existe la carpeta dataset entonces la creo
    os.mkdir(location)
else:
    ##si la carpeta no existe, entonces se borra el contenido
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name))
        for name in dirs:
            os.rmdir(os.path.join(root,name))

##descargar data set de kaggle
os.system("kaggle datasets download -d paakhim10/tweets-and-engagement-metrics -p C:/Users/fcisn/Documents/MURUMURU/practica_do1/dataset")

##descomprimir el archivo de kaggle
os.chdir(location)
for file in os.listdir():
    zip_ref = zipfile.ZipFile(file,"r")
    zip_ref.extractall()
    zip_ref.close()

