class Sensor:
    def __init__(self):
        self.reiniciarDatos()
        
    def reiniciarDatos(self):
        self.estado = "Inactivo"
        
    def mostrarBienvenida(self):
        print("  Bienvenido al Sistema de Control de Temperatura ")
        print("Problema a resolver: Simular el control de un invernadero:")
        print("- Si la temperatura es menor a 10°C → Se activa el calefactor")
        print("- Si está entre 10°C y 25°C → Sistema inactivo")
        print("- Si es mayor a 25°C → Se activa el ventilador")

    def controlarTemperatura(self, temperatura):
        if temperatura < 10:
            self.estado = "Calefactor Encendido"
        elif temperatura > 25:
            self.estado = "Ventilador Encendido"
        else:
            self.estado = "Inactivo"

    def menu(self):
        self.mostrarBienvenida()
        while True:
            print("\nMenú de opciones:")
            print("1. Ingresar temperatura y verificar estado")
            print("2. Volver a realizar otro verificación")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                for i in range(3):  
                    temperatura = float(input("Ingrese la temperatura en °C: "))
                    self.controlarTemperatura(temperatura)
                    print("Estado del sistema:", self.estado)
                    print("Simulación de espera de 5 segundos (presione Enter para continuar)")
                    input()
            elif opcion == "2":
                self.reiniciarDatos()
            elif opcion == "3":
                print("Saliendo del programa. ¡Adioooooooooossss!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

temp = Sensor()
temp.menu()
