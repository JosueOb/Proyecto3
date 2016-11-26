#funcion que reconoce el texto y los separa en elemnetos de una lista
lista_multiple = []
lista_simple = []

def lectura():
    archivo = open("Integrantes.txt","r")
    linea = archivo.readline()
    while linea != "":
        minusc = linea.lower()
        eliminar = minusc.replace("\n","")
        separar = eliminar.split()
        lista_multiple.append(separar)
        linea = archivo.readline()
    archivo.close()
    
def transformar(lista):
    for i in range(0,len(lista)):
        for j in range(0,len(lista[i])):
            palabra = lista[i][j]
            lista_simple.append(palabra)
            
def limpieza_texto(lista,simbolo):
    limpieza_texto = []
    for i in range(0,len(lista)):
        palabra = lista[i]
        nuevo = limpieza_palabra(palabra,simbolo)
        limpieza_texto.append(nuevo)
    return limpieza_texto
    
def limpieza_palabra(palabra,simbolo):
    limpieza_palabra = []
    for i in range(0,len(palabra)):
        limpieza_palabra.append(palabra[i])
        if limpieza_palabra[i] == simbolo:
            limpieza_palabra.remove(limpieza_palabra[i])
            caracter = ""
            palabra = caracter.join(limpieza_palabra)
    return palabra
    
lectura()  
transformar(lista_multiple)
sin_comas = limpieza_texto(lista_simple,",")
sin_puntos = limpieza_texto(sin_comas,".")
sin_expre = limpieza_texto(sin_puntos,"!")
texto_limpio = limpieza_texto(sin_expre,"?")
print(lista_multiple,"\n",lista_simple,"\n",texto_limpio)

