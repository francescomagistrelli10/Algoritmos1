def puede_votar(edad):
    resultado = (edad >= 18) and (edad < 120)
    return resultado

print(puede_votar(15))   
print(puede_votar(20))  
print(puede_votar(130))  