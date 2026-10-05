def calcular_precio_con_impuesto(precio_base, porcentaje_impuesto):
    impuesto = precio_base * (porcentaje_impuesto / 100)
    precio_final = precio_base + impuesto
    return precio_final

print(calcular_precio_con_impuesto(100, 21))
print(calcular_precio_con_impuesto(50, 10))