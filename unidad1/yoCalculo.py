from unidad1 import calculadora

num1 = input("numero 1 = ")

num2 = input("numero 2 = ")

print(num1, " + ", num2, " = ", calculadora.suma(int(num1), int(num2)))
print(num1, " - ", num2, " = ", calculadora.resta(int(num1), int(num2)))