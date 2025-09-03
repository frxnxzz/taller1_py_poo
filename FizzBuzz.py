class FizzBuzz:
    def __init__(self):
        pass  

    def mostrarBienvenida(self):
        print("\n Bienvenido al Juego FizzBuzz")
        print("Problema a resolver: Recorrer los números del 1 al 100 e imprimir:")
        print("- 'Fizz' si el número es divisible por 3")
        print("- 'Buzz' si el número es divisible por 5")
        print("- 'FizzBuzz' si el número es divisible por ambos")
        print("- El número en caso contrario\n")

    def jugar(self):
        for num in range(1, 101):  
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)
        print("\n Juego FizzBuzz finalizado.\n")

    def menu(self):
        self.mostrarBienvenida()
        while True:
            print("--------- Menú De Opciones ---------")
            print("1. Jugar FizzBuzz")
            print("2. Repetir el juego")
            print("3. Salir del programa")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.jugar()
            elif opcion == "2":
                print("\n Reiniciando el juego...\n")
                self.jugar()
            elif opcion == "3":
                print("\n Gracias por jugar FizzBuzz. ¡Adioooooooosssss!\n")
                break
            else:
                print(" Opción inválida. Intente de nuevo.\n")


# -------- Código Principal --------
juego = FizzBuzz()
juego.menu()
