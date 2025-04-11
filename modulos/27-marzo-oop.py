#!/usr/bin/env python3
# -*- coding: utf-8 -*

from modulo_carro import Coche # Importamos la clase Coche

mi_nuevo_coche = Coche('audi', 'a4', 2024)
print(mi_nuevo_coche.obtener_nombre_descriptivo())

mi_nuevo_coche.lectura_odometro = 23
mi_nuevo_coche.leer_odometro()


from modulo_carro import CocheElectrico

mi_leaf = CocheElectrico('nissan', 'leaf', 2024)
print(mi_leaf.obtener_nombre_descriptivo())
mi_leaf.bateria.describir_bateria()
mi_leaf.bateria.obtener_autonomia()
"""

# Podemos importar la clase Coche y CocheElectrico en una sola línea
from modulo_carro import CocheElectrico,Coche|
#Podemos importar todas las clases de un módulo

#Podemos importar un módulo completo y darle un alias
from modulo_carro import *

Ejercicio 1
Usando tu última clase Restaurante, guárdala en un módulo. 
Crea un archivo separado que importe Restaurante. 
Crea una instancia de Restaurante y llama a uno de los métodos 
de Restaurante para mostrar que la instrucción de importación 
está funcionando correctamente.
"""