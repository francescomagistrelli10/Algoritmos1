def clasificar_nota(nota):
    if nota >= 9:
        calificacion = "Sobresaliente"
    elif nota >= 7:
        calificacion = "Notable"
    elif nota >= 5:
        calificacion = "Aprobado"
    else:
        calificacion = "Suspenso"
    return calificacion


print(clasificar_nota(8))
print(clasificar_nota(4))
print(clasificar_nota(6))