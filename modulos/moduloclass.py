
import json
from pathlib import Path
import os

# Inicialización de la tupla con nombre User
class usser:
    def __init__(self, Ussername, Password, Email) -> None:
        self.Ussername = Ussername
        self.Password = Password
        self.Email = Email
        

# Inicializacion de clase cliente que hereda usser
class Cliente(usser):
    def __init__(self, Nombre, Apellido, Edad, Pais, Metodo_pago, Ussername, Password, Email) -> None:
        super().__init__(Ussername, Password, Email)  
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        self.Pais = Pais
        self.Metodo_pago = Metodo_pago
    
    #operacion de muestra de productos
    def lista_products(self):#intentar mostrar los productos que tengo en la carpeta datos, json
        #armado de ruta para encontrar el archivo BD.json
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = Path(ruta_actual) / "BD.json"
        #lectura del mismo
        with open(ruta_archivo,"r") as file:
                archivo = json.load(file)
        #proceso del mismo
        for product in archivo['Productos']:
            print('ID_producto ', product['ID_producto'])
            print('Nombre_producto: ', product['Nombre_producto'])
            print('Precio: ', product['Precio'])
            print('Tienda', product['Tienda'])
            print("***************************************************")
        #operacion de compra de la clase cliente
    def ejecutar_compra(self,Nombre_producto, Tienda):#ejecutar la compra y retornar informacion de la misma
        self.Nombre_producto = Nombre_producto
        self.Tienda = Tienda
        print(f'El ciente: {self.Nombre} {self.Apellido} acaba de comprar: \nPRODUCTO: {self.Nombre_producto}\nTIENDA: {self.Tienda.capitalize()}')
    
    #utilizacion del metodo __str__
    def __str__(self):
        return f"Nombre: {self.Nombre}\nApellido: {self.Apellido}\nEdad: {self.Edad}\nPaís: {self.Pais}\nMétodo de pago: {self.Metodo_pago}\nUsername: {self.Ussername}\nPassword: {self.Password}\nEmail: {self.Email}"

 
  
#Inicializacion de clase admin que hereda usser
class Admin(usser):
   def __init__(self,ID_admin, Ussername, Password, Email) -> None:
       super().__init__(Ussername, Password, Email)
       self.ID_admin = ID_admin
    

cliente1 = Cliente("Lucas", "Chaparro", 22, "Argentina", "Efectivo", "Lucas123", "****", "Lucas.thomas@gmail.com")

print(cliente1.ejecutar_compra("Notebook", "fravega"))


