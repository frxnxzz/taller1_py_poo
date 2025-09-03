class ControlLuces:
    def __init__(self):
        self.reiniciarDatos()
        
    def reiniciarDatos(self):
        self.esNoche = False
        self.movimiento = False
        self.luzEncendida = False

    def mostrarBienvenida(self):
        print("\nBienvenido al sistema de Control de Luces")
        print("Problema a resolver: Simular un sistema domótico que controla las luces de una casa")

    def detectarMovimiento(self, hayMovimiento):
        self.movimiento = hayMovimiento

    def establecerNoche(self, esNoche):
        self.esNoche = esNoche

    def actualizarLuces(self):
        if self.esNoche and self.movimiento:
            self.luzEncendida = True
        else:
            self.luzEncendida = False

    def mostrarEstado(self):
        if self.luzEncendida:
            print("Las luces están ENCENDIDAS")
        else:
            print("Las luces están APAGADAS")

    def simulacion(self):
        contador = 0
        print("\nIniciando simulación automática de 10 segundos...")
        while True:
            contador += 10
            print(f"\n Han pasado {contador} segundos simulados...")
            self.actualizarLuces()
            self.mostrarEstado()
            seguir = input("¿Continuar la simulación? (s/n): ")
            if seguir.lower() != "s":
                print("Simulación detenida.")
                break

    def menu(self):
        self.mostrarBienvenida()
        while True:
            print("\n---------- Menú De Opciones ----------")
            print("1. Establecer Noche")
            print("2. Establecer Día")
            print("3. Detectar Movimiento")
            print("4. No hay Movimiento")
            print("5. Ver Estado de las Luces")
            print("6. Iniciar Simulación Automática (cada 10s)")
            print("7. Reiniciar")
            print("8. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.establecerNoche(True)
                print("Ahora es de NOCHE")
            elif opcion == "2":
                self.establecerNoche(False)
                print("Ahora es de DÍA")
            elif opcion == "3":
                self.detectarMovimiento(True)
                print("Movimiento detectado en la habitación")
            elif opcion == "4":
                self.detectarMovimiento(False)
                print("No hay movimiento en la habitación")
            elif opcion == "5":
                self.actualizarLuces()
                self.mostrarEstado()
            elif opcion == "6":
                self.simulacion()
            elif opcion == "7":
                self.reiniciarDatos()
                print("Reiniciando sistema...")
            elif opcion == "8":
                print("Saliendo del sistema. ¡Adioooooooooosssss!")
                break
            else:
                print("Opción no válida, intente de nuevo.")


#---------------- Código Principal ---------------
sistema = ControlLuces()
sistema.menu()