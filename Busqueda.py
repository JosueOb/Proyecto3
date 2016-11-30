## EPN-ESFOT-ASI Programacion Avanzada

## Busqueda.py
## Versión: 2.1
## Buscar la concurrencia de una palabara en un determinado texto

## Autor: Josué Obaco y Mishel Centeno
## Fecha: 29-Nov-2016

## Listas Globales 
lista_multiple = []
lista_simple = []
guardar_resultados = []
## Funcion que permite la lectura del decumento.txt donde cada linea sea minuscula
## se la separa donde se presente espacios y las añadimos a la lista global multiple
def lectura():
    archivo = open("harry2.txt","r")
    linea = archivo.readline()
    while linea != "":
        minusc = linea.lower()
        eliminar = minusc.replace("\n","")
        separar = eliminar.split()
        lista_multiple.append(separar)
        linea = archivo.readline()
    archivo.close()
    
## Funcion que transfroma una lista multiple a una lista simple ya que en el caso anterior
## la funcion split separa la line en una lista pero esto se le añada a otra lista donde
## se froma una lista multiple
def transformar(lista):
    for i in range(0,len(lista)):
        for j in range(0,len(lista[i])):
            palabra = lista[i][j]
            lista_simple.append(palabra)

## Funcion que realiza la ejecucion de la funcion de limpieza de palabra donde quita los
## signos de puntuacion y de expresion del todo el texto ya que recibe una lista que
## que contenga todo el texto y el signo no desea a eliminar
def limpieza_texto(lista,simbolo):
    limpieza_texto = []
    for i in range(0,len(lista)):
        palabra = lista[i]
        nuevo = limpieza_palabra(palabra,simbolo)
        limpieza_texto.append(nuevo)
    return limpieza_texto

## Funcion que retira los simbolos no deseados de una palabra ya que recibe como parametro
## la palabra y el simbolo a eliminar de la palabara.
def limpieza_palabra(palabra,simbolo):
    limpieza_palabra = []
    for i in range(0,len(palabra)):
        limpieza_palabra.append(palabra[i])
        if limpieza_palabra[i] == simbolo:
            limpieza_palabra.remove(limpieza_palabra[i])
            caracter = ""
            palabra = caracter.join(limpieza_palabra)
    return palabra

## Funcion que permite la busque de la palabara en toda la lista
def busqueda(lista,palabra):
    contador = 0
    busqueda = False
    for i in range(0,len(lista)):
        if lista[i] == palabra:
            contador = contador+1
            busqueda = True
    if busqueda == True:
        print(palabra,"se repite",contador)
        guardar_resultados.append(guardar(palabra,contador))
    else:
        print("No existe")

## Funcion que guarda las busquedas realizadas en una lista      
def guardar (palabra,cantidad):
    lista = []
    lista.append(palabra)
    lista.append(cantidad)
    return lista

## Graba la lista que contiene el historial de busqueda en un archivo.txt           
def grabar(lista):
    archivo = open("resultado.txt","w")
    archivo.close()
    archivo = open("resultado.txt","a")
    archivo.writelines(lista)
    archivo.close()
    
## Funcion que permite que el usuario puede realizar varias busquedas y observar el scrip del
## historial de busqueda que haya realizado
def main():
    lectura()  
    transformar(lista_multiple)
    sin_comas = limpieza_texto(lista_simple,",")
    sin_puntos = limpieza_texto(sin_comas,".")
    sin_expre = limpieza_texto(sin_puntos,"!")
    sin_punto_coma = limpieza_texto(sin_expre,";")
    texto_limpio = limpieza_texto(sin_punto_coma,"?")
    print("TEXTO\n"+str(texto_limpio)+"\n\nBUSQUEDA DE PALABRAS EN UN DOCUMENTO: \nPresione ENTER para terminar")
    palabra = input("Busqueda: ")
    while palabra !="":
        busqueda(texto_limpio,palabra)
        palabra = input("Busqueda: ")
    if len(guardar_resultados) !=0:
        print("\nTermino! \nHistorial:"+"\n"+str(guardar_resultados)+"\nSe generó un scrip de su busqueda")
        grabar(str(guardar_resultados))
    else:
        print("No realizó ninguna busqueda!")
    
main()
