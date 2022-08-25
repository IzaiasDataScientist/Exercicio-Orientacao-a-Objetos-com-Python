class Elevador:

    __quantas_pessoas: int = 0
    __andar_atual: int = 0
    __total_andar: int = 0
    __excluir_andar: int = 1
    __capacidade_elevador: int = 0

    @property
    def capacidade_elevador(self):
        return self.__capacidade_elevador

    @capacidade_elevador.setter
    def capacidade_elevador(self, new):
        self.__capacidade_elevador = new

    @property
    def total_andar(self):
        return self.__total_andar

    @total_andar.setter
    def total_andar(self, new):
        self.__total_andar = new

    def inicializa(self, capacidade_elevador: int, total_andar: int) -> None:
        self.__capacidade_elevador = capacidade_elevador
        self.__total_andar = total_andar
        self.__quantas_pessoas = 0
        self.__andar_atual = 0

    def entrar(self):
        if self.__quantas_pessoas < self.__capacidade_elevador:
            self.__quantas_pessoas += 1
        return self.__quantas_pessoas

    def sair(self):
        if self.__quantas_pessoas > 0:
            self.__quantas_pessoas -= 1
        return self.__quantas_pessoas

    def sobe(self):
        if self.__andar_atual < self.__total_andar:
            self.__andar_atual += 1
        return self.__andar_atual

    def desce(self):
        if self.__andar_atual >= 1:
            self.__andar_atual -= self.__excluir_andar
        return self.__andar_atual


obj = Elevador()
obj.inicializa(10, 10)
#obj.capacidade_elevador = 20
#obj.total_andar = 20
print(obj.total_andar)
print(obj.capacidade_elevador)
print(obj.entrar())
print(obj.entrar())
print(obj.entrar())
print(obj.entrar())
print(obj.entrar())
print(obj.entrar())
print(obj.entrar())
print(obj.entrar())
print(obj.entrar())
print(obj.entrar())
print(obj.entrar())
print(obj.entrar())
print(obj.sair())
print(obj.sair())
print(obj.sair())
print(obj.sair())
print(obj.sair())
print(obj.sair())
print(obj.sair())
print(obj.sair())
print(obj.sair())
print(obj.sair())
print(obj.sair())
print(obj.sobe())
print(obj.sobe())
print(obj.sobe())
print(obj.sobe())
print(obj.sobe())
print(obj.sobe())
print(obj.sobe())
print(obj.sobe())
print(obj.sobe())
print(obj.sobe())
print(obj.sobe())
print(obj.sobe())
print(obj.desce())
print(obj.desce())
print(obj.desce())
print(obj.desce())
print(obj.desce())
print(obj.desce())
print(obj.desce())
print(obj.desce())
print(obj.desce())
print(obj.desce())
print(obj.desce())
