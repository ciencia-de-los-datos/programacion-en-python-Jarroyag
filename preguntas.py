"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    date = open("data.csv", "r").readlines()
    col = [int(row[2]) for row in date]
    suma = sum(col)
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    from typing import Counter
    date = open("data.csv", "r").readlines()
    col = [(row[0]) for row in date]
    contador =Counter(list(col))
    
    tupla = [(key,valor) for key,valor in contador.items()]
    tupla.sort()
    return tupla


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    date = open("data.csv", "r").readlines()
    dato2 = [(x.split("\t")[0],int(x.split("\t")[1])) for x in date]
    dato3 = sorted(set([x[0] for x in date]))
    resul=[]
    conta =0
    for dos in dato3:
      for tres in dato2:
         if tres[0]==dos:
          conta +=tres[1]
     
      resul.append((dos,conta))
      conta=0
    return resul
    
    


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    date = open("data.csv", "r").readlines()
    dato2 = [(x.split("\t")[2][5:7]) for x in date]
    dato_mes = sorted(set([x for x in dato2]))
    cant = [(x,dato2.count(x)) for x in dato_mes]

    return cant


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    dato = open("data.csv", "r").readlines()
    dato=[f.replace("\n","")for f in dato]
    dato=[f.split("\t") for f in dato]
    
    id_list=sorted(set([f[0] for f in dato]))
    lista_datos=[(f[0],int(f[1])) for f in dato]
    valores=[]
    tupla4=[]

    for y in id_list:
        for x in lista_datos:
            if x[0]== y:
                valores.append(x[1])

        tupla4.append((y, max(valores),min(valores)))
        valores.clear()  

    return tupla4


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    date = open("data.csv", "r").readlines()
    date = [val.replace("\n","") for val in date]
    date = [val.split("\t") for val in date]
    date = [clave[4].split(",") for clave in date]

    result=[]

    for clave in date:
      for val in clave:
        result.append(val.split(":"))
    dic3 = {clave[0]:[] for clave in sorted(result)}

    for clave in result:
      dic3[clave[0]].append(int(clave[1]))

    Total = list(zip(dic3.keys(),[min(clave) for clave in dic3.values()],[max(clave) for clave in dic3.values()]))

    return Total


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    date = open("data.csv", "r").readlines()
    date = [val.replace("\n", "") for val in date]
    date = [val.split("\t") for val in date]

    letras = sorted(set([int(x[1]) for x in date]))
    dic2 = {x:[] for x in letras}
    for x in date:
      dic2[int(x[1])].append(x[0])
    total = list(zip(dic2.keys(),dic2.values())) 

    return total


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    date = open("data.csv", "r").readlines()
    date = [val.replace("\n", "") for val in date]
    date = [val.split("\t") for val in date]

    dic4 = dict()
    for x in date:
      if int(x[1]) not in dic4.keys():
       dic4[int(x[1])]=[x[0]]
      else:
         dic4[int(x[1])].append(x[0])
    total2 = sorted(list(dic4.items())) 
    total2 = [(i[0],sorted(set(i[1]))) for i in total2]

    return total2


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    date = open("data.csv", "r").readlines()
    date=[f.replace("\n","") for f in date]
    date=[f.split("\t") for f in date]
    date=[f[4].split(",") for f in date]
    
    
    lista_clave= [(y[:3])for x in date for y in x]
    keys_dict=sorted(set( elem for elem in lista_clave ))
   
    tupla8=[(x,lista_clave.count(x))for x in keys_dict]
    dict1=dict(tupla8)
           
    return dict1


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    date = open("data.csv", "r").readlines()
    date = [val.replace("\n", "") for val in date]
    date = [val.split("\t") for val in date]

    tupl = [(row[0],len(row[3].split(",")),len(row[4].split(","))) for row in date]

    return tupl


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    date = open("data.csv", "r").readlines()
    date = [val.replace("\n", "") for val in date]
    date = [val.split("\t") for val in date]

    date = [[val[3].split(","),val[1]] for val in date]
    date = [[val[0], int(val[1])] for val in date]

    resul2 = []

    for x,y in date:
      for i in x:
        resul2.append([i,y])
    dic5={}

    for x in resul2:
      if x[0] in dic5:
       dic5[x[0]]= dic5[x[0]] + x[1]
      else:
        dic5[x[0]] = x[1]

    return dic5


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    date = open("data.csv", "r").readlines()
    date=[f.replace("\n","")for f in date]
    date=[f.split("\t") for f in date]

    col5=[f[4].split(",")for f in date]
    col1=[(f[0]) for f in date]
    datos_letras=list(zip(col1,col5))

    dict3_keys=sorted(set(col1))
    
    dict3={}
    for llave in dict3_keys:  
        dict3[llave]= 0
   
    for x, y in datos_letras:
       for z in y:
           dict3[x]+= int(z[4:])
         
    return dict3
