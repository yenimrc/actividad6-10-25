class Lista:
    def __init__(self):
        self.elementos_lista=[]

    def datos(self,datos):
        datos=input('Inserta un dato: ')
        self.elementos_lista.append(datos)
        print(f'Dato: {datos} añadido con éxito 😎')
    
    def eliminar_dato(self):
        busqueda_dato=input('¿Qué dato quieres eliminar?: ')
        