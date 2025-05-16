# main.py

from HV import registrar_HV, buscar_hoja_vida, actualizar_hoja_vida
from Generar_Reportes import (
    reporte_experiencia,
    reporte_por_certificacion,
    exportar_json,
    exportar_csv,
    exportar_txt,
    analizar_habilidades_comunes
)

hojas_vida = []

def menu_principal():
    while True:
        print("\n=== VitaeConsole - Gestión de Hojas de Vida ===")
        print("1. Registrar nueva hoja de vida")
        print("2. Buscar hoja de vida")
        print("3. Actualizar hoja de vida")
        print("4. Generar reportes")
        print("5. Exportar hojas de vida")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nueva = registrar_HV()
            if nueva:
                hojas_vida.append(nueva)
                print("Hoja de vida registrada correctamente.")

        elif opcion == "2":
            criterio = input("Buscar por (nombre, documento, correo): ").lower()
            valor = input(f"Ingrese el {criterio}: ")
            resultado = buscar_hoja_vida(hojas_vida, criterio, valor)
            if resultado:
                print(f"\n=== Hoja de Vida: {resultado['datos_personales']['nombre']} ===")
                for clave, valor in resultado.items():
                    print(f"\n{clave.upper()}:")
                    print(valor)
            else:
                print("Hoja de vida no encontrada.")

        elif opcion == "3":
            documento = input("Ingrese el documento de la persona: ")
            hv = buscar_hoja_vida(hojas_vida, "documento", documento)
            if hv:
                actualizar_hoja_vida(hv)
                print("Actualización completada.")
            else:
                print("Hoja de vida no encontrada.")

        elif opcion == "4":
            menu_reportes()

        elif opcion == "5":
            menu_exportacion()

        elif opcion == "6":
            print("Gracias por usar VitaeConsole. Hasta pronto.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

def menu_reportes():
    while True:
        print("\n=== Reportes ===")
        print("1. Listado por años de experiencia")
        print("2. Candidatos con una certificación")
        print("3. Habilidades más comunes")
        print("4. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            anios = int(input("Ingrese el mínimo de años de experiencia: "))
            reporte_experiencia(hojas_vida, anios)

        elif opcion == "2":
            cert = input("Ingrese el nombre de la certificación o habilidad: ")
            reporte_por_certificacion(hojas_vida, cert)

        elif opcion == "3":
            analizar_habilidades_comunes(hojas_vida)

        elif opcion == "4":
            break

        else:
            print("Opción inválida.")

def menu_exportacion():
    while True:
        print("\n=== Exportación de Datos ===")
        print("1. Exportar a JSON completo")
        print("2. Exportar a JSON resumido")
        print("3. Exportar a CSV")
        print("4. Exportar a TXT")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            exportar_json(hojas_vida, resumido=False)
            print("Exportado como exportado.json")

        elif opcion == "2":
            exportar_json(hojas_vida, resumido=True)
            print("Exportado como exportado.json (resumen)")

        elif opcion == "3":
            exportar_csv(hojas_vida)
            print("Exportado como exportado.csv")

        elif opcion == "4":
            exportar_txt(hojas_vida)
            print("Exportado como exportado.txt")

        elif opcion == "5":
            break

        else:
            print("Opción inválida.")



menu_principal()