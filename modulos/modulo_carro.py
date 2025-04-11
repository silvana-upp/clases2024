#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Coche:
    """Un intento simple de representar un coche."""

    def __init__(self, marca, modelo, año):
        """Inicializa los atributos para describir un coche."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.lectura_odometro = 0

    def obtener_nombre_descriptivo(self):
        """Devuelve un nombre descriptivo formateado ordenadamente."""
        nombre_largo = f"{self.año} {self.marca} {self.modelo}"
        return nombre_largo.title()

    def leer_odometro(self):
        """Imprime una declaración que muestra el kilometraje del coche."""
        print(f"Este coche tiene {self.lectura_odometro} millas en él.")

    def actualizar_odometro(self, kilometraje):
        """
        Establece la lectura del odómetro al valor dado.
        Rechaza el cambio si intenta retroceder el odómetro.
        """
        if kilometraje >= self.lectura_odometro:
            self.lectura_odometro = kilometraje
        else:
            print("¡No puedes retroceder un odómetro!")

    def incrementar_odometro(self, millas):
        """Añade la cantidad dada al odómetro."""
        self.lectura_odometro += millas

class Bateria:
    """Un intento simple de modelar una batería para un coche eléctrico."""

    def __init__(self, tamaño_bateria=40):
        """Inicializa los atributos de la batería."""
        self.tamaño_bateria = tamaño_bateria

    def describir_bateria(self):
        """Imprime una declaración describiendo el tamaño de la batería."""
        print(f"Este coche tiene una batería de {self.tamaño_bateria} kWh.")

    def obtener_autonomia(self):
        """Imprime una declaración sobre la autonomía que proporciona esta batería."""
        if self.tamaño_bateria == 40:
            autonomia = 150
        elif self.tamaño_bateria == 65:
            autonomia = 225
        print(f"Este coche puede recorrer aproximadamente {autonomia} millas con una carga completa.")

class CocheElectrico(Coche):
    """Modela aspectos de un coche, específicos para vehículos eléctricos."""

    def __init__(self, marca, modelo, año):
        """
        Inicializa los atributos de la clase padre.
        Luego inicializa los atributos específicos de un coche eléctrico.
        """
        super().__init__(marca, modelo, año)
        self.bateria = Bateria()