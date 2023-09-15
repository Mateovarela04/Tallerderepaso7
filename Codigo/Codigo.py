from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return self.nombre == other.nombre


class Conjunto:

    contador = 0

    def __init__(self, nombre):
        self.elementos: list = []
        self.nombre: str = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    def contiene(self, elemento):
        return any(elemento == e for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNION {otro_conjunto.nombre}")
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_interseccion = [e for e in conjunto1.elementos if conjunto2.contiene(e)]
        nombre_conjunto = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        nuevo_conjunto = Conjunto(nombre_conjunto)
        nuevo_conjunto.elementos = elementos_interseccion
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join(e.nombre for e in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"
