from automovil import Automovil
def main():
    a1=Automovil("vw",250,4500)
    a2=Automovil("volvo",300,8000)
    a3=Automovil("nissan",180,5000)
    a1.saludar()
    a2.saludar()
    a3.saludar()
    a1.en_marcha(100)
    a1.kilometros()