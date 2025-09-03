class Cine:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.asientos = [False] * capacidad  

    def mostrarBienvenida(self):
        print("\nBienvenido al Sistema de Reservas de Cine")
        print("Problema a resolver: Reservar asientos en una sala de cine.")
        print("Puede reservar múltiples asientos hasta que la sala esté llena.\n")

    def mostrarAsientos(self):
        print("\nEstado actual de la sala:")
        for i in range(self.capacidad):  
            if self.asientos[i]:
                print(f"Asiento {i+1}: Ocupado")
            else:
                print(f"Asiento {i+1}: Libre")
        print()

    def reservarAsiento(self):
        if all(self.asientos):
            print("No hay más asientos disponibles.\n")
            return

        while True:
            try:
                self.mostrarAsientos()
                num = int(input(f"Digite el número de asiento (1-{self.capacidad}): "))

                if num < 1 or num > self.capacidad:
                    print("Número de asiento inválido. Intente de nuevo.\n")
                elif self.asientos[num-1]:
                    print("Ese asiento ya está reservado. Intente otro.\n")
                else:
                    self.asientos[num-1] = True
                    print(f"Reserva exitosa. Asiento {num} ha sido reservado.\n")
                    break
            except ValueError:
                print("Entrada inválida. Debe digitar un número.\n")

    def reiniciar(self):
        self.asientos = [False] * self.capacidad
        print("\n El sistema ha sido reiniciado. Puede comenzar de nuevo.\n")

    def menu(self):
        self.mostrarBienvenida()
        while True:
            print("--------- Menú De Opciones ---------")
            print("1. Reservar un asiento")
            print("2. Reiniciar reservas (hacer otro ejercicio)")
            print("3. Salir del programa")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.reservarAsiento()
            elif opcion == "2":
                self.reiniciar()
            elif opcion == "3":
                print("\n Gracias por usar el sistema de reservas. ¡Adioooooooooooos!\n")
                break
            else:
                print(" Opción inválida. Intente de nuevo.\n")



# --------------------- Código Principal ------------------------
sistema = Cine(capacidad=25)  
sistema.menu()
