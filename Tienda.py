class Acceso:
    def __init__(self):
        self.reiniciarDatos()
        
    def reiniciarDatos(self):
        self.membresia = False
        self.horario = False
        self.esEmpleado = False
        
    def mostrarBienvenida(self):
        print("Bienvenido al Sistema de control de Acceso ")
        print("Problema a resolver: Sistema de control de acceso que permite la entrada a una tienda")
        print("Solo si el cliente tiene una membresía válida y está dentro del horario de atención ")
        print("Ó si el cliente es un empleado")
        
    def ingresarDatos(self):
        while True:
            respuesta = input("¿Tiene una membresía válida? (s/n): ").strip().lower()
            if respuesta == "s":
                self.membresia = True
                break
            elif respuesta == "n":
                self.membresia = False
                break
            else:
                print("Opción inválida, responda con (s/n)")
        
        while True:
            respuesta2 = input("¿Está dentro del horario de atención? (s/n): ").strip().lower()
            if respuesta2 == "s":
                self.horario = True
                break
            elif respuesta2 == "n":
                self.horario = False
                break
            else:
                print("Opción inválida, responda con (s/n)")
                
        while True:
            respuesta3 = input("¿Es empleado? (s/n): ").strip().lower()
            if respuesta3 == "s":
                self.esEmpleado = True
                break
            elif respuesta3 == "n":
                self.esEmpleado = False
                break
            else:
                print("Opción inválida, responda con (s/n)")

    def verificarAcceso(self):
        if (self.membresia and self.horario) or self.esEmpleado:
            print("\nAcceso PERMITIDO\n")
        else:
            print("\nAcceso DENEGADO\n")
        
    def menu(self):
        self.mostrarBienvenida()
        while True:
            print("--------- Menú De Opciones ---------")
            print("1. Verificar acceso")
            print("2. Reiniciar")
            print("3. Salir del programa")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ingresarDatos()
                self.verificarAcceso()
            elif opcion == "2":
                self.reiniciarDatos()
            elif opcion == "3":
                print("\nSaliendo del programa. ¡Adioooooooooooos!\n")
                break
            else:
                print("Opción inválida. Intente de nuevo.\n")
                
                
#-------------- Código Principal ------------
acc = Acceso()
acc.menu()
