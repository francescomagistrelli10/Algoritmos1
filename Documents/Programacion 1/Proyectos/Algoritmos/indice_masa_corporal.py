def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"

print(calcular_imc(70, 1.75))
print(calcular_imc(45, 1.85))
print(calcular_imc(105, 1.70))

