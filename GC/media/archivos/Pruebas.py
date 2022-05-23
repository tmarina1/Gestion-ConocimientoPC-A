import re

archivo = 'Add.asm'
file = open(archivo, 'r')
lineas = file.readlines()

ArchivoCambiado = []

for linea in lineas:
    #linea = linea.replace(' ', '')
    linea = linea.replace("\n","")
    linea = linea.split("//", 1)
    #linea = linea[0]
    #linea = linea.split("\n", 1)
    #linea = linea[0]
  

    ArchivoCambiado.append(linea)
print(ArchivoCambiado)

COMP = {
    '0': '0101010',
    '1': '0111111',
    '-1': '0111010',
    'D': '0001100',
    'A': '0110000',
    '!D': '0001101',
    '!A': '0110001',
    '-D': '0001111',
    '-A': '0110011',
    'D+1': '0011111',
    'A+1': '0110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'D+A': '0000010',
    'D-A': '0010011',
    'A-D': '0000111',
    'D&A': '0000000',
    'D|A': '0010101',

    'M': '1110000',
    '!M': '1110001',
    'M+1': '1110111',
    'M-1': '1110010',
    'D+M': '1000010',
    'D-M': '1010011',
    'M-D': '1000111',
    'D&M': '1000000',
    'D|M': '1010101'
  }

for i in ArchivoCambiado:
  for j in i:
    #print(j)
    for k in j:
      if k in COMP:
        #Remplazar clase
        ArchivoCambiado[1] = COMP[k]
print(ArchivoCambiado)