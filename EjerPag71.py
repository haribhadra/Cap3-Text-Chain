# Las cadena de texto son de tipo de datos INMUTABLES. Es por ello que no poidemos modificar
# un caracter directamente.
print()
cancion = '''Don't you cry tonight
I still love you baby
Don't you cry tonight
Don't you cry tonight
There's a heaven above you baby
And don't you cry tonight'''

cortar = cancion.split()
contador = len(cancion) # Longitud de una Cadena
print(cortar)
print("El Total de Caracteres ",contador)
print()

# Pertenencia de un Elemento con IN, esta busqueda retorna un valor Booleano
busqueda = 'cry' in cancion
print(busqueda)

