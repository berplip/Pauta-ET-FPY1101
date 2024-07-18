import random
import csv
import statistics
import math

trabjadores = [
    "Juan Pérez", "María García", "carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
]

sueldos = []

def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range (10)]
    print("Sueldos asignados aleatoriamente.")

def clasificar_sueldos():
    menor_800k = []
    entre_800k_y_2m =[]
    mayor_2m = []
    total_sueldos = 0

    for empleado, sueldo in zip(trabjadores, sueldos):
        total_sueldos += sueldo
        if sueldo < 800000:
            menor_800k.append((empleado, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800k_y_2m.append((empleado, sueldo))
        else:
            mayor_2m.append((empleado, sueldo))
        
        print("\nSueldos menores a $800.000")
        print(f"Total: {len(menor_800k)}")
        for empleado, sueldo in menor_800k:
            print(f"{empleado} ${sueldo}")

        print("\nSueldos entre $800.000 y $2.000.000")
        print(f"Total: {len(entre_800k_y_2m)}")
        for empleado, sueldo in entre_800k_y_2m:
            print(f"{empleado} $[sueldo]") 

        print(f"\nTOTAL SUELDOS: ${total_sueldos}")

def ver_estadisticas():
               sueldo_mas_alto = max(sueldos)
               sueldo_mas_bajo = min(sueldos)
               promedio = statistics.mean(sueldos)
               media_geometrica = math.exp(statistics.mean([math.log(sueldo) for sueldo in sueldos]))      
                                         
               print("\nEstadísticas de Sueldos:")
               print(f"Sueldo más alto: ${sueldo_mas_alto}")
               print(f"Sueldo más bajo: ${sueldo_mas_bajo}")
               print(f"Promedio de sueldos: ${promedio:.2f}")
               print(f"Media geométrica: ${media_geometrica:.2f}:")

def reporte_sueldos():
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])

        for empleado, sueldo in zip(trabjadores, sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([empleado, sueldo, descuento_salud, descuento_afp, sueldo_liquido])

        print(f"{empleado} | Sueldo base: ${sueldo} | Descuento Salud: ${descuento_salud:.2f} | Descuento AFP: ${descuento_afp} | Sueldo Líquido: ${sueldo_liquido:.2f}")

        print("\nReporte de sueldos generado en 'reporte_sueldos.csv'.")

def main():
    while True:
       print("\nMenú:")
       print("1. Asignar sueldos aleatorios")
       print("2. Clasificar sueldos")
       print("3. Estadisticas")
       print("4. Reporte de sueldos")
       print("5. Salir")

       opcion = input("Seleccione una opción: ")

       if opcion == '1':
           asignar_sueldos()
       elif opcion == '2':
           clasificar_sueldos()
       elif opcion == '3':
           ver_estadisticas()
       elif opcion == '4':
           reporte_sueldos()
       elif opcion == '5':
           print("Finalizando Programa.")
           print("Desarrollado por Jefferson Rojas")
           print("RUT 21.684.345-2")
           break
    else:
             print("Opción no válida. Intente Nuevamente.")

if __name__ == "__main__":
     main()                                    




            
               












