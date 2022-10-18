from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas=[]
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self,score):
        self._golesMarcados=score
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self,red):
        self._tarjetasRojas=red
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self,leg):
        self._piernaHabil=leg

    def __str__(self):
        return f"Mi nombre es {Persona.getNombre(self)} soy profesional en el deporte {Deportista.getDeporte(self)} Tengo {Persona.getEdad(self)} años de edad y llevo {Deportista.getAñosPracticando(self)} años en el deporte"
