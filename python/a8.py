
precio = int(input("ingrese el precio del producto: "))

descuento = int(input("ingrese el porcentaje de descuento: "))

descuento = precio * (descuento / 100)

precio_final = precio - descuento 

print("el valor del descuento es: ", descuento,"el precio final es:",precio_final )

