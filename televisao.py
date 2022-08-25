class Televisao(object):

    def __init__(self):
        self.__volume = 0
        self.__canal = 0

    def imprimir_volume(self):
        print(self.__volume)
        return self.__volume

    def imprimir_canal(self):
        print(self.__canal)
        return self.__canal


class ControleRemoto(Televisao):

    def __int__(self):
        super().__init__().__canal
        super().__init__().__volume

    def aumenta_volume(self):
        if self._Televisao__volume <= 10:
            self._Televisao__volume += 1

    def diminui_volume(self):
        if self._Televisao__volume > 0:
            self._Televisao__volume -= 1

    def aumentar_canal(self):
        if self._Televisao__canal <= 10:
            self._Televisao__canal += 1

    def diminuir_canal(self):
        if self._Televisao__canal > 0:
            self._Televisao__canal -= 1

    def trocar_canal(self, canal):
        self._Televisao__canal = canal


obj = Televisao()
obj.imprimir_volume()
obj2 = ControleRemoto()
obj2.aumenta_volume()
obj2.imprimir_volume()
obj.imprimir_volume()
obj2.diminui_volume()
obj2.diminui_volume()
obj2.diminui_volume()
obj2.imprimir_volume()
obj2.aumentar_canal()
obj2.aumentar_canal()
obj2.aumentar_canal()
obj2.imprimir_canal()
obj2.diminuir_canal()
obj2.imprimir_canal()
obj2.trocar_canal(4)
obj2.imprimir_canal()
obj.imprimir_canal()
