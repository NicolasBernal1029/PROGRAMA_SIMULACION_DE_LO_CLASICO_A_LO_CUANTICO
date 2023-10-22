import unittest
import leaptoquantum
import numpy as np
class LeapToQuantum_Test(unittest.TestCase):
    
    def test_canicas_1(self): #Ejemplo 3.4 del libro
        P = np.array([[False,False,False,False,False,False],
                                 [False,False,False,False,False,False],
                                 [False,True,False,False,False,True],
                                 [False,False,False,True,False,False],
                                 [False,False,True,False,False,False],
                                 [True,False,False,False,True,False]], dtype=bool)
        estado_inicial = np.array([6,2,1,5,3,10])
        pasos = 1
        result = leaptoquantum.canicas(P,estado_inicial,pasos)
        expected=np.array([0,0,12,5,1,9])
        np.testing.assert_array_equal(result, expected)

    def test_canicas_2(self): #Ejercicio 3.1.1 del libro 
        P = np.array([[False,False,False,False,False,False],
                                 [False,False,False,False,False,False],
                                 [False,True,False,False,False,True],
                                 [False,False,False,True,False,False],
                                 [False,False,True,False,False,False],
                                 [True,False,False,False,True,False]], dtype=bool)
        estado_inicial = np.array([5,5,0,2,0,15])
        pasos = 1
        result = leaptoquantum.canicas(P,estado_inicial,pasos)
        expected = np.array([0,0,20,2,0,5])
        np.testing.assert_array_equal(result, expected)

    def test_doble_rendija_clasico_1(self): #Ejemplo 3.32 del libro
        P = np.array([[0,0,0,0,0,0,0,0],
                      [1/2,0,0,0,0,0,0,0],
                      [1/2,0,0,0,0,0,0,0],
                      [0,1/3,0,1,0,0,0,0],
                      [0,1/3,0,0,1,0,0,0],
                      [0,1/3,1/3,0,0,1,0,0],
                      [0,0,1/3,0,0,0,1,0],
                      [0,0,1/3,0,0,0,0,1]])
        estado_inicial = np.array([1,0,0,0,0,0,0,0])
        pasos = 2
        result = leaptoquantum.Experimento_doble_rendija_clasico(P,estado_inicial,pasos)
        expected = np.array([0,0,0,1/6,1/6,1/3,1/6,1/6])
        np.testing.assert_array_equal(result, expected)
        print(leaptoquantum.graficacion(result))


    def test_doble_rendija_clasico_2(self): #Ejemplo billar clasico
        P = np.array([[0,1/2,1/2,0],[1/2,0,0,1/2],[1/2,0,0,1/2],[0,1/2,1/2,0]])
        estado_inicial = np.array([1,0,0,0])
        pasos = 2
        result = leaptoquantum.Experimento_doble_rendija_clasico(P,estado_inicial,pasos)
        expected = np.array([1/2,0,0,1/2])
        np.testing.assert_array_equal(result, expected)
        print(leaptoquantum.graficacion(result))
    
    def test_doble_rendija_cuantico_1(self): #matriz 3.50 del libro
        P = np.array([[0,0,0,0,0,0,0,0],
              [1/np.sqrt(2),0,0,0,0,0,0,0],
              [1/np.sqrt(2),0,0,0,0,0,0,0],
              [0,(-1+1j)/(np.sqrt(6)),0,1,0,0,0,0],
              [0,(-1-1j)/(np.sqrt(6)),0,0,1,0,0,0],
              [0,(1-1j)/(np.sqrt(6)),(-1+1j)/(np.sqrt(6)),0,0,1,0,0],
              [0,0,(-1-1j)/(np.sqrt(6)),0,0,0,1,0],
              [0,0,(1-1j)/(np.sqrt(6)),0,0,0,0,1]], dtype=complex)
        estado_inicial = [1,0,0,0,0,0,0,0]
        pasos = 2
        result = leaptoquantum.Experimento_doble_rendija_cuantico(P,estado_inicial,pasos)
        expected= np.array([0+0j,0+0j,0+0j,-0.28867513+0.28867513j,-0.28867513-0.28867513j,0+0j,-0.28867513-0.28867513j,0.28867513-0.28867513j])
        np.testing.assert_almost_equal(result, expected)
        print(leaptoquantum.graficacion(result))

    def test_doble_rendija_cuantico_2(self): #
        P = np.array([[0,1/np.sqrt(2),1/np.sqrt(2),0],[1/np.sqrt(2),0,0,-1/np.sqrt(2)],[1/np.sqrt(2),0,0,1/np.sqrt(2)],[0,-1/np.sqrt(2),1/np.sqrt(2),0]],dtype=complex)
        estado_inicial = [1,0,0,0]
        pasos = 1
        result = leaptoquantum.Experimento_doble_rendija_cuantico(P,estado_inicial,pasos)
        expected= np.array([0,1/np.sqrt(2),1/np.sqrt(2),0])
        np.testing.assert_almost_equal(result, expected)
        print(leaptoquantum.graficacion(result))



if __name__ == '__main__':
    unittest.main()
