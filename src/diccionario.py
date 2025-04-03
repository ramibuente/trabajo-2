
def crear (final,rondas):    
    if len(rondas)>0:  
        for nombre in rondas[0]:                      #recorremos el diccionario para inicializar los valores de cada jugador
            final[nombre]={"kills":0,"assists":0,"deaths":0,"MVP":0,"puntos":0}


def imprimir (diccionario):         #funcion para imprimir el diccionario de manera ordenada
    print("jugador     kills   assists    deaths   MVP    puntos")
    print("========================================================")
    for h in diccionario:
        print(f" {h[0]}{(" ")* (6-len(h[0]))}       {h[1]['kills']}        {h[1]['assists']}         {h[1]['deaths']}       {h[1]["MVP"]}       {h[1]['puntos']}")
    print("========================================================")
    print("=========================================================")

def ordenarP(diccionario):         #funcion para ordenar el diccionario por puntos
    return sorted(diccionario.items(), key=lambda x: x[1]['puntos'], reverse=True)

def ordenarM(diccionario):         #funcion para ordenar el diccionario por MVP
    return sorted(diccionario.items(), key=lambda x: x[1]['MVP'], reverse=True)

def ordenarK(diccionario):         #funcion para ordenar el diccionario por kills
    return sorted(diccionario.items(), key=lambda x: x[1]['kills'], reverse=True)

def ordenarA(diccionario):         #funcion para ordenar el diccionario por assists
    return sorted(diccionario.items(), key=lambda x: x[1]['assists'], reverse=True)

def ordenarD(diccionario):         #funcion para ordenar el diccionario por deaths
    return sorted(diccionario.items(), key=lambda x: x[1]['deaths'], reverse=True)

def ordenarN(diccionario):         #funcion para ordenar el diccionario por nombre
    return sorted(diccionario.items(), key=lambda x: x[0], reverse=False)