import unittest

def mayor_de_edad(edad):
    if edad>=18:
        return True
    else:
        return False

class test_prueba_de_cristal(unittest.TestCase):
    def test_mayor_de_edad(self):
        edad = 18
        resultado = mayor_de_edad(edad)
        self.assertEqual(resultado,True)

    def test_es_menor_edad(self):
        edad = 17
        resultado = mayor_de_edad(edad)
        self.assertEqual(resultado,False)

if __name__ == '__main__':
    unittest.main()
