print()
text= 'Mi primera daceda de texto'
print(text)
print()

# Usando comillas "" o '', caracteres de escape '/', etc
comillas = 'Los llamados "strings" son secuencias de caracteres'
print(comillas)
print()

# Comillas simples escapadas con "/" y con comillas simples
comillas2 = 'Mas texto con escapes de \'strings\' como sub cadenas'
print(comillas2)
print()

# El uso de comillas triples ''' '''
poema = ''' Todavía tengo casi todos mis dientes
casi todos mis cabellos y poquísimas canas
puedo hacer y deshacer el amor
trepar una escalera de dos en dos
y correr cuarenta metros detrás del ómnibus
o sea que no debería sentirme viejo
pero el grave problema es que antes
no me fijaba en estos detalles.'''
print(poema)
print()

# Dentro de las cadenas de texto se puede usar la "conversión" de cualquier valor a un string.
conver1 = str(True)
print(conver1)
print()

# Secuencias de escape \n (salto de linea) o \t (tabulación)
salto = 'Texto con saltos de varias lineas \nSegunda linea de texto y van mas \nTercera linea de texto'
print(salto)
print()

# Expresiones literales "RAW DATA (r)"
dato1 = 'abc \ndef'
print(dato1)
print()

dato2 = r'abc\ndef'
print(dato2)
print()

dato3 = 'a\tb\tc\td\te\tf'
print(dato3)
print()

# La función PRINT más a fondo
msg1 = '¿Sabes por qué estoy acá?'
msg2 = ' Por qué me gusta'
# Utilizaremos condiciones como SEP, END para agrgar condiciones a la salida de print
print(msg1, msg2, sep=' , ')
print(msg1, msg2, sep=', ', end='..!!')
print()