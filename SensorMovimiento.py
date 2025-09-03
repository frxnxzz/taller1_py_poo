class Seguridad:
    def __init__(self):
        self.reiniciarDatos()
        
    def reiniciarDatos(self):
        self.alarmaActiva = False
        self.esNoche = True  
        self.sensores = [False, False, False]  

    def mostrarBienvenida(self):
        print("\nBienvenido al Sistema de Seguridad")
        print("Problema a resolver: simula un sistema con 3 sensores de movimiento.")
        print("La alarma se activa si al menos 2 sensores detectan movimiento y es de noche.\n")

    def activarAlarma(self):
        self.alarmaActiva = True
        print("\nLa alarma ha sido ACTIVADA.")

    def desactivarAlarma(self):
        self.alarmaActiva = False
        print("\nLa alarma ha sido DESACTIVADA.")

    def leerSensores(self):
        for i in range(3):
            entrada = input(f"Ingrese 1 si el sensor {i+1} detecta movimiento, 0 si no: ")
            self.sensores[i] = True if entrada == "1" else False

    def verificarAlarma(self):
        if not self.alarmaActiva:
            print("\nEl sistema está desactivado. No se disparará la alarma.\n")
            return

        movimientos = sum(self.sensores)
        if movimientos >= 2 and self.esNoche:
            print("ALARMA ACTIVADA: Intruso detectado.")
        else:
            print("Todo en orden. No hay intrusos.")

    def menu(self):
        self.mostrarBienvenida()
        while True:
            print("\n--------- Menú De Opciones ---------")
            print("1. Activar alarma")
            print("2. Desactivar alarma")
            print("3. Simular sensores")
            print("4. Reiniciar")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.activarAlarma()
            elif opcion == "2":
                self.desactivarAlarma()
            elif opcion == "3":
                self.leerSensores()
                self.verificarAlarma()
            elif opcion == "4":
                self.reiniciarDatos()
            elif opcion == "5":
                print("\nSaliendo del sistema de seguridad. ¡Adiooooooooooossss!")
                break
            else:
                print("\nOpción no válida. Intente de nuevo.")


# ------------------- Código Principal ---------------------
sistema = Seguridad()
sistema.menu()