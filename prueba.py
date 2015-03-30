# importamos la libreria xlrd para leer archivos de excel
import xlrd
#importamos la funcion randint de la libreria random
from random import randint

# guardamos la ruta del archivo que queremos leer en una variable
doc = xlrd.open_workbook('prueba.xls')
# guardamos la hoja del archivo que vamos leer
sheet = doc.sheet_by_index(0)

nfilas = sheet.nrows
ncolumnas = sheet.ncols

#for i in range(nfilas):
    #cadena = ''
    #for j in range(ncolumnas):
        #cadena += '%s '%sheet.cell_value(i,j)
    #print(cadena)

#for i in range(nfilas):
    #cadena = ''
    #cadena += '%s '%sheet.cell_value(i,0)
    #print(cadena)

for i in range(nfilas):
    cadena = ''
    columna = 0
    cadena += '%s '%sheet.cell_value(i,randint(0,2))
    print(cadena)