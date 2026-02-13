
taller = float(input("ingrese la nota del taller (30%):"))

parcial = float(input("ingrese la nota del examen parcial (30%):"))

final = float(input("ingrese la nota del examen final (40%):"))

nota_final = (taller *  0.30) + (parcial * 0.30) + (final * 0.40)

print("su nota final es:",nota_final)