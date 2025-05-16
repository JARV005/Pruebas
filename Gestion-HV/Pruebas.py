# reportes.py

import json
import csv
from datetime import datetime
from tabulate import tabulate
from collections import Counter


def calcular_experiencia_total(experiencias):
    total_meses = 0
    for exp in experiencias:
        duracion = exp.get("duracion", "0")
        try:
            total_meses += int(duracion)
        except ValueError:
            continue
    return total_meses // 12  # Convertir a años

#
def reporte_experiencia(hojas_vida, anios_minimos):
    resultado = []
    for hv in hojas_vida:
        anios = calcular_experiencia_total(hv.get("experiencia_profesional", []))
        if anios >= anios_minimos:
            resultado.append([hv["datos_personales"]["nombre"], anios])
    print(tabulate(resultado, headers=["Nombre", "Años de experiencia"], tablefmt="grid"))

#
def reporte_por_certificacion(hojas_vida, cert_busqueda):
    resultado = []
    for hv in hojas_vida:
        habilidades = hv.get("habilidades", [])
        if cert_busqueda.lower() in map(str.lower, habilidades):
            resultado.append([hv["datos_personales"]["nombre"], ", ".join(habilidades)])
    print(tabulate(resultado, headers=["Nombre", "Habilidades/Certificaciones"], tablefmt="fancy_grid"))


def exportar_json(hojas_vida, archivo="exportado.json", resumido=False):
    with open(archivo, "w", encoding="utf-8") as f:
        if resumido:
            resumen = [{"nombre": hv["datos_personales"]["nombre"],
                        "correo": hv["datos_personales"]["correo"],
                        "documento": hv["datos_personales"]["documento"]} for hv in hojas_vida]
            json.dump(resumen, f, indent=4, ensure_ascii=False)
        else:
            json.dump(hojas_vida, f, indent=4, ensure_ascii=False)


def exportar_csv(hojas_vida, archivo="exportado.csv"):
    with open(archivo, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Correo", "Documento", "Total Años de Experiencia"])
        for hv in hojas_vida:
            nombre = hv["datos_personales"]["nombre"]
            correo = hv["datos_personales"]["correo"]
            doc = hv["datos_personales"]["documento"]
            anios = calcular_experiencia_total(hv.get("experiencia_profesional", []))
            writer.writerow([nombre, correo, doc, anios])


def exportar_txt(hojas_vida, archivo="exportado.txt"):
    with open(archivo, "w", encoding="utf-8") as f:
        for hv in hojas_vida:
            f.write(f"Nombre: {hv['datos_personales']['nombre']}\n")
            f.write(f"Correo: {hv['datos_personales']['correo']}\n")
            f.write(f"Documento: {hv['datos_personales']['documento']}\n")
            f.write("="*40 + "\n")


def analizar_habilidades_comunes(hojas_vida):
    todas = []
    for hv in hojas_vida:
        todas.extend(hv.get("habilidades", []))
    conteo = Counter(todas)
    print(tabulate(conteo.most_common(10), headers=["Habilidad", "Frecuencia"], tablefmt="simple_grid"))