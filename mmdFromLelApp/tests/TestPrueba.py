from django.test import TestCase


class TestPrueba(TestCase):

    def testHola(self):

        valor1 = 1
        valor2 = 0
        print('***********************************************************')
        print('                UNA PRUEBA                                ')
        try:
            self.assertEqual(valor1, valor2, 'TODO BIEN')
            print("TODO BIEN")
        except AssertionError:
            print("TODO MAL")
        finally:
            print('***********************************************************')



    def testChau(self):
        valor1 = 0
        valor2 = 0
        print('***********************************************************')
        print('                OTRA PRUEBA                                ')
        try:
            self.assertEqual(valor1, valor2, 'TODO BIEN')
            print("TODO BIEN")
        except AssertionError:
            print("TODO MAL")
        finally:
            print('***********************************************************')