def saludo(nombre,apellido):
    return f"Hola {nombre} {apellido}, ¿Como te encuentras?"

valor = input("Escribe tu nombre: ")
valor2 = input("Escrino tu apellido: ")
print(saludo(valor,valor2))