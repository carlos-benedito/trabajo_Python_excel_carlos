import json
from datetime import date
import pandas as pd

# Función para leer el archivo JSON
def leer_json(nombre_archivo):
    with open(nombre_archivo, "r") as file:
        empleados = json.load(file)
    return empleados

# Nombre del archivo JSON
nombre_archivo_json = "empleados.json"

# Función para procesar los empleados y crear el DataFrame
def procesar_empleados(empleados):
    datos_procesados = {
        'Salario': [],
        'Edad': [],
        'Nombre': [],
        'Genero': [],
        'Proyecto': [],
        'Correo': []
    }
    for empleado in empleados:
        if empleado['proyect'] != 'GRONK':
            salario = float(empleado['salary'].replace("$", "").replace(",", ""))
            if empleado['age'] < 30:
                salario *= 1.1  # Aplicar aumento del 10% al salario para empleados menores de 30 años
            salario_str = f"{salario:.2f}€"  # Convertir salario y añadir el símbolo del euro
            datos_procesados['Salario'].append(salario_str)
            datos_procesados['Edad'].append(empleado['age'])
            datos_procesados['Nombre'].append(empleado['name'])
            datos_procesados['Genero'].append(empleado['gender'])
            datos_procesados['Proyecto'].append(empleado['proyect'])
            datos_procesados['Correo'].append(empleado['email'])
    return datos_procesados

# Leer el archivo JSON
empleados = leer_json(nombre_archivo_json)

# Procesar los empleados y obtener los datos procesados
datos_procesados = procesar_empleados(empleados)

# Crear DataFrame de pandas con los datos procesados
df = pd.DataFrame(datos_procesados)

# Generar el nombre del archivo Excel
nombre_archivo_excel = f'pagos-empleados-{date.today().month}-{date.today().year}.xlsx'

# Escribir los datos en un archivo Excel
df.to_excel(nombre_archivo_excel, index=False)

print(f'Se ha creado el archivo Excel "{nombre_archivo_excel}" exitosamente.')

