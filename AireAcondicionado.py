class AireAcondicionado:
    def __init__(self):
        self.reiniciarDatos()
        
    def reiniciarDatos(self):
        self.temperatura = 0
        self.humedad = 0
        self.encendido = False

    def mostrarBienvenida(self):
        print("Bienvenido al Sistema de control de Aire Acondicionado ")
        print("Problema a resolver: El sistema de aire se activa si:")
        print("Temperatura > 28°C y Humedad > 60%")
        print("Ó si la Temperatura > 30°C sin importar la humedad.")

    def leerSensores(self):
        self.temperatura = float(input("Ingrese la temperatura (°C): "))
        self.humedad = float(input("Ingrese la humedad (%): "))

    def verificarEstado(self):
        if (self.temperatura > 28 and self.humedad > 60) or self.temperatura > 30:
            self.encendido = True
        else:
            self.encendido = False

    def mostrarEstado(self):
        print(f"Temperatura: {self.temperatura}°C | Humedad: {self.humedad}%")
        if self.encendido:
            print("El aire acondicionado está ENCENDIDO.")
        else:
            print("El aire acondicionado está APAGADO.")

    def menu(self):
        self.mostrarBienvenida()
        while True:
            print("\n--------- Menú De Opciones ---------")
            print("1. Hacer lectura de los sensores")
            print("2. Volver hacer la lectura")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                for i in range(5):
                    print(f"\nLectura {i+1}:")
                    self.leerSensores()
                    self.verificarEstado()
                    self.mostrarEstado()
            elif opcion == "2":
                print("\nReiniciando sistema...")
                self.reiniciarDatos()
            elif opcion == "3":
                print("Saliendo del programa. ¡Adiooooooossssss!")
                break
            else:
                print("Opción no válida, intente nuevamente.")


# --------------- Código Principal --------------
aire = AireAcondicionado()
aire.menu()