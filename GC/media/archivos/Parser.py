typeC = True

Diccionario = {}
Diccionario['='] = 0
Diccionario['@'] = 1
Diccionario['D'] = '001100'
Diccionario['A'] = '110000'
Diccionario['M'] = '110000'


if typeC is True:
  Diccionario['null'] = '000'
  Diccionario['M'] = '001'
  Diccionario['D'] = '010'
  Diccionario['DM'] = '011'
  Diccionario['A'] = '100'
  Diccionario['AM'] = '101'
  Diccionario['AD'] = '110'
  Diccionario['ADM'] = '111'
  Diccionario['JGT'] = '001'
  Diccionario['JEQ'] = '010'
  Diccionario['JGE'] = '011'
  Diccionario['JLT'] = '100'
  Diccionario['JNE'] = '101'
  Diccionario['JLE'] = '110'
  Diccionario['JMP'] = '111'

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

  DEST = {
    'null': '000',
    'M': '001',
    'D': '010',
    'MD': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'AMD': '111'
  }

  JMP = {
    'null': '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111'
  }

  Simbolos = {
    'R0': '0',
    'R1': '1',
    'R2': '2',
    'R3': '3',
    'R4': '4',
    'R5': '5',
    'R6': '6',
    'R7': '7',
    'R8': '8',
    'R9': '9',
    'R10': '10',
    'R11': '11',
    'R12': '12',
    'R13': '13',
    'R14': '14',
    'R15': '15',
    'SCREEN': '16384',
    'KBD': '24576',
  }

  
  archivo = 'programa.py'
  file = open(archivo, 'r')
  lineas = file.readlines()

  ArchivoCambiado = []

  for linea in lineas:
    linea = linea.replace(' ', '')
    linea = linea.split("//", 1)
    linea = splitLine[0]
    splitLine = linea.split('\n', 1)
    linea = splitLine[0]

    ArchivoCambiado.append(linea.line)

  if '@' in linea:
    print('instruccion tipo A')
  else:
    print('instruccion tipo C')

    DiccionarioC = COMP.comp
    DiccionarioD = DEST.dest
    DiccionarioJ = JMP.jump

    comp = DiccionarioC[comp]
    dest = DiccionarioD[dest]
    jump = DiccionarioJ[jump]

    traduccion = '111' + comp + dest + jump