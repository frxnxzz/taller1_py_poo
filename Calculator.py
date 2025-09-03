class Calculator:
    def __init__(self):
        pass

    def mostrarBienvenida(self):
        print("\n Bienvenido a la Calculadora Pro MAX")
        print("Problema a resolver: Calculadora simple")
        print("Puede realizar múltiples cálculos hasta que decida salir.\n")

    def operar(self):
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("\nOperaciones disponibles:")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")

            opcion = input("Seleccione la operación (1-4): ")

            if opcion == "1":
                print(f"Resultado: {num1 + num2}")
            elif opcion == "2":
                print(f"Resultado: {num1 - num2}")
            elif opcion == "3":
                print(f"Resultado: {num1 * num2}")
            elif opcion == "4":
                if num2 != 0:
                    print(f"Resultado: {num1 / num2}")
                else:
                    print("Error: No se puede dividir entre 0.")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor, ingrese solo números válidos.")

    def menu(self):
        self.mostrarBienvenida()
        while True:
            print("\n--------- Menú de Opciones ---------")
            print("1. Ejecutar Calculator Pro MAX")
            print("2. Volver a hacer otro operación")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.operar()
            elif opcion == "2":
                print("Reiniciando ejercicio...")
                self.operar()
            elif opcion == "3":
                print("¡Gracias por usar la calculadora! ¡Adiooooooooooooosss!.")
                break
            else:
                print("Opción inválida, intente de nuevo.")



# ----------- Código Principal-----------
cal = Calculator()
cal.menu()
