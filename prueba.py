class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def imprimirDatos(self):
        print(f"Se llama {self.nombre} y tiene {self.edad} años")
        