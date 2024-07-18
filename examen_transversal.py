import random
import csv

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def asignar_sueldos():
    return [random.randint(300000, 2500000) for _ in range(10)]

def clasificar_sueldos(sueldos):
    menores = []
    medios = []
    mayores = []

    for i in range(len(sueldos)):
        if sueldos[i] < 800000:
            menores.append((trabajadores[i], sueldos[i]))
        elif sueldos[i] <= 2000000:
            medios.append((trabajadores[i], sueldos[i]))
        else:
            mayores.append((trabajadores[i], sueldos[i]))

    return menores, medios, mayores

def ver_estadisticas(sueldos):
    if not sueldos:
        print("Primero debe asignar sueldos.")
        return
    
    sueldo_mas_alto = max(sueldos)
    sueldo_mas_bajo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)
    media_geometrica = (prod(sueldos))**(1/len(sueldos))
    
    print(f"Sueldo más alto: ${sueldo_mas_alto:.2f}.")
    print("·································")
    print(f"Sueldo más bajo: ${sueldo_mas_bajo:.2f}")
    print("·································")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
    print("·································")
    print(f"Media geométrica: ${media_geometrica:.2f}")

def reporte_sueldos(sueldos):
    if not sueldos:
        print("Primero debe asignar sueldos.")
        return
    
    with open('reporte_sueldos.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])

        for i in range(len(sueldos)):
            descuento_salud = sueldos[i] * 0.07
            descuento_afp = sueldos[i] * 0.12
            sueldo_liquido = sueldos[i] - descuento_salud - descuento_afp
            nombre_empleado = trabajadores[i]
            sueldo_base = f"${sueldos[i]:,.0f}"
            descuento_salud = f"${descuento_salud:,.0f}"
            descuento_afp = f"${descuento_afp:,.0f}"
            sueldo_liquido = f"${sueldo_liquido:,.0f}"
            writer.writerow([nombre_empleado, sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])

    print("Reporte de sueldos generado en 'reporte_sueldos.csv'.")

def menu():
    sueldos = []
    continuar = True  
    while continuar:
        print(f"""
            ---------  MENU  ---------
            1. Asignar sueldos aleatorios
            2. Clasificar sueldos
            3. Ver estadísticas
            4. Reporte de sueldos
            5. Salir del programa
        """)

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Por favor ingrese un número válido.")
            continue

        if opcion == 1:
            sueldos = asignar_sueldos()
            print("Sueldos asignados.")
        elif opcion == 2:
            if sueldos:
                menores, medios, mayores = clasificar_sueldos(sueldos)
                print("·································")
                print("\nSueldos menores a $800.000:")
                print("                                      ")
                for empleado, sueldo in menores:
                    print(f"{empleado}: ${sueldo:,.0f}")
                print("·································")
                print("\nSueldos entre $800.000 y $2.000.000:")
                print("                                      ")
                for empleado, sueldo in medios:
                    print(f"{empleado}: ${sueldo:,.0f}")
                print("·································")
                print("\nSueldos superiores a $2.000.000:")
                print("                                      ")
                for empleado, sueldo in mayores:
                    print(f"{empleado}: ${sueldo:,.0f}")
            else:
                print("Primero debe asignar sueldos.")
        elif opcion == 3:
            ver_estadisticas(sueldos)
        elif opcion == 4:
            reporte_sueldos(sueldos)
            print("Reporte de sueldos generado en 'reporte_sueldos.csv'.")
        elif opcion == 5:
            print("Saliendo del programa..")
            print("Desarrollado por Isaac Orellana Leiva")
            print("RUT 22.087.013-8")
            continuar = False 
        else:
            print("Opción no válida. Intente nuevamente.")

def prod(iterable):
    product = 1
    for num in iterable:
        product *= num
    return product

menu()
