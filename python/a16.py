
import math

radio = float(input("ingrese el radio del circulo:"))

area = math.pi * math.pow (radio,2)

perimetro = 2 * math.pi * radio 

print("el area es:" ,round(area), "y el perimetro", round(perimetro))