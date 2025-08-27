class Saludo:
    # metodo constructor
    # inicializar obj
    def __init__(self, dato_texto):
        # Atributo
        self.mensaje = dato_texto
        print(self.mensaje)

    def get_mensaje(self):
        return self.mensaje
    
    def set_atributo(self, dato_nuevo_mensaje):
        self.mensaje = dato_nuevo_mensaje

    def tomar_nombre(self):
        nombre_usuario = input("Escriba el nombre del usuario: ")
        return nombre_usuario
    
    def hacer_mensaje(self, dato_usuario):
        self.mensaje = "Hola usuario " + dato_usuario
        self.imprimir_mensaje(self.mensaje)

    def imprimir_mensaje(self, dato_mensaje):
        print(dato_mensaje)

# Código principal

texto = "Hola usuario"
obj_mensaje = Saludo(texto)
aux_dato=obj_mensaje.tomar_nombre()
obj_mensaje.hacer_mensaje(aux_dato)