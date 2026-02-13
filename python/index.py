from colorama import init, Fore,Style,Back
import os 
import sys 
import subprocess


while True:
    print(Fore.RED+"=========================================") 
    print(" Taller 1 - algoritmos Basicos en python ") 
    print("       By Mateo Franco Buriticá")
    print("            Menú Principal")   
    print("=========================================") 
    
    for i in range(1, 26):
        print(f"{i}.Ejecutar algoritmos {i}")
    print("0 . salir\n")
    
    opcion = input("seleccione una opcion:")
    
    if opcion == "0":
        print("saliendo ...")
        break
    if opcion. isdigit() and 1 <= int(opcion) <= 25:
        archivo = f"a{opcion}.py"
        
        if os.path.exists(archivo):
            subprocess.run([sys.executable, archivo])
        else:
            print(f"no existe {archivo}")
    
    else:
        print("opcion no valida")
        
        input("\n Presione ENTER para continuar")
    
    
