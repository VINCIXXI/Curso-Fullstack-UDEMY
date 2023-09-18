from io import open
import pathlib
import shutil #modulo para copiar archivos
import os #modulo para borrar

#abrir archivos
ruta=str(pathlib.Path().absolute())+"/nombre_archivo.txt"
archivo=open(ruta,"a+")

#abrir archivos para lectura
ruta=str(pathlib.Path().absolute())+"/nombre_archivo.txt"
archivo=open(ruta,"r")