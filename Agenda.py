class Agenda:

    contador: int = 0
    listas: list = []

    def armazenaPessoa(self, nome: str, idade: int, altura: float) -> list:
        Agenda.contador += 1
        if Agenda.contador <= 10:
            self.listas += [[nome, idade, altura]]
        elif Agenda.contador > 10:
            print(f'O limite de pessoa está agenda é de {Agenda.contador-1}')

    def removerPessoa(self, nome: str) -> None:
        for i in range(0, len(self.listas)):
            if nome in self.listas[i]:
                index: int = i
        self.listas.pop(index)

    def buscarPessoa(self, nome: str) -> int:
        for i in range(0, len(self.listas)):
            if nome in self.listas[i]:
                index: int = i
                print(index)
        return index

    def imprimirAgenda(self) -> None:
        print(self.listas)

    def imprimirPessoa(self, index: int) -> None:
        print(self.listas[index])

    def tamanhoAgenda(self) -> None:
        print(len(self.listas))


obj = Agenda()
obj.armazenaPessoa("Leticia", 43, 1.80)
obj.armazenaPessoa("Debora", 35, 1.90)
obj.armazenaPessoa("Carla", 27, 1.60)
obj.armazenaPessoa("Dayane", 28, 1.64)
obj.armazenaPessoa("Daniela", 24, 1.61)
obj.armazenaPessoa("Luana", 21, 1.66)
obj.armazenaPessoa("Camila", 23, 1.50)
obj.armazenaPessoa("Viviane", 30, 1.40)
obj.armazenaPessoa("Barbara", 29, 1.62)
obj.armazenaPessoa("Grabriela", 33, 1.58)
obj.armazenaPessoa("Marina", 34, 1.61)

print('imprimirAgenda')
obj.imprimirAgenda()
print('removerPessoa')
obj.removerPessoa("Luana")
print('imprimirAgenda')
obj.imprimirAgenda()
print('buscarPessoa')
obj.buscarPessoa("Barbara")
print('imprimirPessoa')
obj.imprimirPessoa(2)
obj.imprimirPessoa(obj.buscarPessoa("Daniela"))
print('tamanhoAgenda')
obj.tamanhoAgenda()
