import numpy as np
import matplotlib.pyplot as plt
def canicas(P, estado_inicial, pasos):
    # Iteramos a través de los pasos de tiempo
    estado_actual = estado_inicial
    for i in range(pasos):
        estado_actual = np.dot(P,estado_actual)
    # Devolvemos el estado del sistema después de los pasos de tiempo
    return estado_actual


def Experimento_doble_rendija_cuantico(P, estado_inicial, pasos):
    # Iteramos a través de los pasos de tiempo
    estado_actual = estado_inicial
    for i in range(pasos):
        estado_actual = np.dot(P,estado_actual)
    # Devolvemos el estado del sistema después de los pasos de tiempo
    return estado_actual


def Experimento_doble_rendija_clasico(P, estado_inicial, pasos):
    # Iteramos a través de los pasos de tiempo
    estado_actual = estado_inicial
    for i in range(pasos):
        estado_actual = np.dot(P,estado_actual)
    # Devolvemos el estado del sistema después de los pasos de tiempo
    return estado_actual


def graficacion(estado_final):
    print('El vector estado final es {}'.format(estado_final))
    probabilidades=np.abs(estado_final)
    i = 0
    for probabilidad in probabilidades:
        print('la probabilidad en el estado {} es {}%:'.format(i,probabilidad))
        i+=1
    cajas = np.arange(len(estado_final))
    plt.bar(cajas, probabilidades)
    plt.xlabel('Caja')
    plt.ylabel('Número de canicas')
    plt.show()
    plt.savefig('grfico.png')
