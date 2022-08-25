import unittest

from exercicio_pessoa import Pessoa


class MyTestCase(unittest.TestCase):
    def test_nome(self):
        test = Pessoa(nome="Marcela", idade=25, altura=1.60)
        self.assertEqual(
            test.nome, "Marcela"
        )  # add assertion here

    def test_idade(self):
        test = Pessoa(nome="Marcela", idade=25, altura=1.60)
        self.assertEqual(
            test.idade, 25
        )

    def test_altura(self):
        test = Pessoa(nome="Marcela", idade=25, altura=1.60)
        self.assertEqual(
            test.altura, 1.60
        )

    def test_imprimir(self):
        test = Pessoa(nome="Marcela", idade=25, altura=1.60)
        self.assertEqual(
            test.imprimir(), "Seu nome eh Marcela, sua idade eh de 25 e a sua altura eh de 1.6"
        )


if __name__ == '__main__':
    unittest.main()

