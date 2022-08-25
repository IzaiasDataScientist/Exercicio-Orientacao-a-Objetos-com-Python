class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome: str = nome
        self.__idade: int = idade
        self.__altura: float = altura

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, new_name):
        self.__nome = new_name

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, new_idade):
        self.__idade = new_idade

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, new_altura):
        self.__altura = new_altura

    def imprimir(self):
        #return f'Seu nome eh {self.__nome}, sua idade eh de {self.__idade} e a sua altura eh de {self.__altura}'  # Com test
        return print(f'seu nome eh {self.__nome}, sua idade eh de {self.__idade} e a sua altura eh de {self.__altura}')  # Sem test


if __name__ == '__main__':
    pessoa = Pessoa("Carla", 25, 1.6)
    pessoa.altura = 2
    pessoa.imprimir()


