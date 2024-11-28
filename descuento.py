
precio_original = float(input("introduce el precio del producto"))
descuento = float(input("introduce el porcentaje del descuento"))
precio_final = precio_original * (1 - descuento / 100)
print(f"el precio final despues del descuento es: {precio_final}")

