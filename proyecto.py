from dataclasses import dataclass

@dataclass


class Elemento:
    def _init_(self, nombre:str):
        self.nombre:str = nombre

    def _eq_(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

@classmethod

class Conjunto:
    elementos: list =[]
    def _init_(self, nombre:str):
        self.nombre:str = nombre
        Conjunto.contador += 1
        self.__id= Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        for e in self.elementos:
            if e.nombre == elemento.nombre:
                return True
        return False

    def agregar_elemento(self, elemento):

        if not self.contiene(elemento):
            return self.elementos.append(elemento)

    def unir(self, otro_conjunto):

        for e in otro_conjunto.elementos:

            if self.contiene(e):

                continue

            self.elementos.append(e)

    def _add_(self, otro_conjunto):

        nuevo_conjunto = Conjunto(self.nombre)

        for e in self.elementos:
            nuevo_conjunto.agregar_elemento(e)

        for e in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(e)


        return nuevo_conjunto

    def intersectar(cls, conjunto1, conjunto2):
        nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        resultado = Conjunto(nombre)
        for elemento in conjunto1.elementos:
            if elemento in conjunto2.elementos:
                resultado.agregar_elemento(elemento)
        return resultado

    def _str_(self):
        elementos_str = ", ".join(str(elemento) for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"



