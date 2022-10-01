class Automovil: 
    
    def __init__(self,nombre,velocidad_max,kilometraje):
        
        self.nombre=nombre
        self.velocidad_max=velocidad_max
        self.kilometraje=kilometraje
    
    def nombre(self):
        print(f"hola soy" self.nombre)
    
    def velocidad(self):
        print(f"tengo una velocidad de max de" self.velocidad_max"km x hr" )
        
    def kilometraje(self):
        print(f"este es"self.kilometraje "mi kilometraje")
        
    def en_marcha(self,km):
        self.kilometraje+=km
        return self.kilometraje
        
        