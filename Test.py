from dataclasses import dataclass
from typing import List, ClassVar

@dataclass
class Elemento:
    nombre:str

    def __eq__(self, other):
        return self.nombre == other.nombre

class Conjunto:

    contador: ClassVar[int] = 0

    def __init__(self, nombre: str):
        self.elementos = []
        self.nombre = nombre
        self.__id = type(self).contador
        type(self).contador += 1

    def contiene(self, elemento: Elemento) -> bool:
        return elemento in self.elementos

    def agregar_elemento(self, elemento: Elemento) -> None:
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto: "Conjunto") -> "Conjunto":
        nuevos_elementos = [elemento for elemento in otro_conjunto.elementos if not self.contiene(elemento)]
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO CON {otro_conjunto.nombre}")
        nuevo_conjunto.elementos = self.elementos + nuevos_elementos
        return nuevo_conjunto

    def __add__(self, otro_conjunto: "Conjunto") -> "Conjunto":
        return self.unir(otro_conjunto)

    @classmethod
    def intersectar(cls, conjunto1: "Conjunto", conjunto2: "Conjunto") -> "Conjunto":
        nuevos_elementos = [elemento for elemento in conjunto1.elementos if conjunto2.contiene(elemento)]
        nuevo_conjunto = Conjunto(f"{conjunto1.nombre} INTERSECTADO CON {conjunto2.nombre}")
        nuevo_conjunto.elementos = nuevos_elementos
        return nuevo_conjunto

    def __str__(self) -> str:
        elementos_str = ", ".join([elemento.nombre for elemento in self.elementos])
        return f"{self.nombre}: ({elementos_str})"
    @classmethod
    def get_contador(cls):
        return cls.contador


    @property
    def id(self):
        return self.__id


p1 = Elemento("Matias")
p2 = Elemento("Matias")
p3 = Elemento("Maria")

print(f"P1 es igual a p2?", p1 == p2)
conjunto1 = Conjunto("Conjunto 1")
conjunto2 = Conjunto("Conjunto 2")

print(f"Atributo contador: ",Conjunto.contador)
print(f"Id del conjunto 1: ",conjunto1.id)
print(f"Id del conjunto 2: ",conjunto2.id)


conjunto1.agregar_elemento(p1)
conjunto1.agregar_elemento(p2)

conjunto2.agregar_elemento(p1)
conjunto2.agregar_elemento(p3)

conjunto3 = conjunto1 + conjunto2

print(conjunto1)
print(conjunto2)
print(conjunto3)
print(f"Id del conjunto 3: ", conjunto3.id)
conjunto4 = Conjunto.intersectar(conjunto1, conjunto2)
print(conjunto4)
