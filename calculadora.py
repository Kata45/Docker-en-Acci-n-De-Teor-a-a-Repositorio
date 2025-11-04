# 🧮 Calculadora simple en 🐍 Python + Docker 🐳

print("=== CALCULADORA SIMPLE ===")
print("Operaciones disponibles: +  -  *  /")

try:
num1 = float(input("Ingresa el primer número: "))
oper = input("Ingresa la operación (+, -, *, /): ")
num2 = float(input("Ingresa el segundo número: "))

```
if oper == '+':
    resultado = num1 + num2
elif oper == '-':
    resultado = num1 - num2
elif oper == '*':
    resultado = num1 * num2
elif oper == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División por cero"
else:
    resultado = "Operación no válida"

print(f"Resultado: {resultado}")
```

except ValueError:
print("Por favor, introduce números válidos.")

print("\nGracias por usar la calculadora 🧮")

