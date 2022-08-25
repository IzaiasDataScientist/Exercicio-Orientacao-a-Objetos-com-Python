import unittest

from elevador import Elevador


class MyTestCase(unittest.TestCase):

    def test_inicializa(self):
        obj = Elevador()
        self.assertEqual(obj.inicializa(capacidade_elevador=10, total_andar=25), None)  # add assertion here

    def test_entrar(self):
        obj = Elevador()
        obj.inicializa(capacidade_elevador=10, total_andar=25)
        self.assertEqual(obj.entrar(), 1)

    def test_entrar_maior_numero_pessoa(self):
        obj = Elevador()
        obj.inicializa(capacidade_elevador=10, total_andar=25)
        self.assertEqual(obj.entrar(), 1)
        self.assertEqual(obj.entrar(), 2)

    def test_sair(self):
        obj = Elevador()
        obj.inicializa(capacidade_elevador=10, total_andar=25)
        self.assertEqual(obj.entrar(), 1)
        self.assertEqual(obj.entrar(), 2)
        self.assertEqual(obj.sair(), 1)

    def test_sobe(self):
        obj = Elevador()
        obj.inicializa(capacidade_elevador=10, total_andar=25)
        self.assertEqual(obj.sobe(), 1)

    def test_desce(self):
        obj = Elevador()
        obj.inicializa(capacidade_elevador=10, total_andar=25)
        self.assertEqual(obj.sobe(), 1)
        self.assertEqual(obj.desce(), 0)


if __name__ == '__main__':
    unittest.main()
