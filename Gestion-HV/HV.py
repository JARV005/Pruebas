# HV.py

from datetime import datetime
from collections import defaultdict

correos_registrados = set()
documentos_registrados = set()

def registrar_HV():
    print("\n=== Registro de nueva hoja de vida ===")
    nombre = input("Nombre completo: ")
    documento = input("Número de documento: ")
    if documento in documentos_registrados:
        print("Documento ya registrado.")
        return None

    correo = input("Correo electrónico: ")
    if correo in correos_registrados:
        print("Correo ya registrado.")
        return None

    telefono = input("Teléfono de contacto: ")
    direccion = input("Dirección: ")
    fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ")

    datos_personales = {
        "nombre": nombre,
        "documento": documento,
        "correo": correo,
        "telefono": telefono,
        "direccion": direccion,
        "fecha_nacimiento": fecha_nac
    }

    formacion = []
    while True:
        inst = input("Institución académica: ")
        titulo = input("Título obtenido: ")
        anios = input("Años (ej. 2015-2019): ")
        formacion.append({"institucion": inst, "titulo": titulo, "anios": anios})
        if input("¿Agregar otra formación? (s/n): ").lower() != "s":
            break

    experiencia = []
    while True:
        empresa = input("Empresa: ")
        cargo = input("Cargo: ")
        funciones = input("Funciones: ")
        duracion = input("Duración en meses: ")
        experiencia.append({"empresa": empresa, "cargo": cargo, "funciones": funciones, "duracion": duracion})
        if input("¿Agregar otra experiencia? (s/n): ").lower() != "s":
            break

    referencias = []
    while True:
        nombre_ref = input("Nombre de referencia: ")
        relacion = input("Relación: ")
        tel = input("Teléfono: ")
        referencias.append({"nombre": nombre_ref, "relacion": relacion, "telefono": tel})
        if input("¿Agregar otra referencia? (s/n): ").lower() != "s":
            break

    habilidades = set()
    while True:
        habilidad = input("Habilidad o certificación: ")
        habilidades.add(habilidad)
        if input("¿Agregar otra habilidad? (s/n): ").lower() != "s":
            break

    hoja_vida = {
        "datos_personales": datos_personales,
        "formacion_academica": formacion,
        "experiencia_profesional": experiencia,
        "referencias": referencias,
        "habilidades": list(habilidades)
    }

    correos_registrados.add(correo)
    documentos_registrados.add(documento)
    return hoja_vida


def buscar_hoja_vida(hojas_vida, criterio, valor):
    for hv in hojas_vida:
        if hv["datos_personales"].get(criterio, "").lower() == valor.lower():
            return hv
    return None


def actualizar_hoja_vida(hoja_vida):
    print("\n=== Actualización de hoja de vida ===")
    print("1. Añadir formación\n2. Añadir experiencia\n3. Editar datos personales\n4. Agregar habilidad\n5. Agregar referencia")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        inst = input("Institución: ")
        titulo = input("Título: ")
        anios = input("Años: ")
        hoja_vida["formacion_academica"].append({"institucion": inst, "titulo": titulo, "anios": anios})

    elif opcion == "2":
        empresa = input("Empresa: ")
        cargo = input("Cargo: ")
        funciones = input("Funciones: ")
        duracion = input("Duración en meses: ")
        hoja_vida["experiencia_profesional"].append({"empresa": empresa, "cargo": cargo, "funciones": funciones, "duracion": duracion})

    elif opcion == "3":
        campo = input("Campo a editar (nombre, correo, telefono, direccion): ")
        nuevo_valor = input(f"Nuevo valor para {campo}: ")
        hoja_vida["datos_personales"][campo] = nuevo_valor

    elif opcion == "4":
        habilidad = input("Nueva habilidad o certificación: ")
        hoja_vida["habilidades"].append(habilidad)

    elif opcion == "5":
        nombre_ref = input("Nombre de referencia: ")
        relacion = input("Relación: ")
        tel = input("Teléfono: ")
        hoja_vida["referencias"].append({"nombre": nombre_ref, "relacion": relacion, "telefono": tel})

    else:
        print("Opción no válida.")