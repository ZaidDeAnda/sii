# Diagnóstico de Centros Comunitarios en Nuevo León

Repositorio para el levantamiento y registro de información relacionada con la valoración de centros comunitarios en Nuevo León.

## Descripción

Este proyecto contiene una aplicación desarrollada en **Streamlit** para capturar información de diagnóstico sobre centros comunitarios. La herramienta permite seleccionar un centro, consultar su dirección, adjuntar evidencia fotográfica y registrar datos sobre recursos, servicios, aulas, materiales y mantenimiento.

El objetivo principal es apoyar los trabajos del gabinete de inclusión de Nuevo León mediante una herramienta sencilla para recopilar información estructurada sobre las condiciones de los centros comunitarios.

## Funcionalidades principales

- Selección de centro comunitario desde una base de datos.
- Visualización de información básica del centro seleccionado.
- Carga de fotografía como evidencia.
- Registro de recursos de cómputo disponibles.
- Captura de información sobre personal y recursos humanos.
- Registro de aulas y espacios especializados.
- Evaluación de servicios disponibles como agua, luz, gas, teléfono e internet.
- Registro de materiales para talleres.
- Evaluación de condiciones de mantenimiento.
- Almacenamiento de respuestas en un archivo CSV.

## Archivos principales

```text
.
├── README.md
├── diagnostico_centros.py
├── centros_comunitarios.csv
├── centros_diagnostico_db.csv
└── Matriz de Centros.xlsx
```

### `diagnostico_centros.py`

Aplicación principal desarrollada en Streamlit. Contiene el formulario interactivo para capturar la valoración de cada centro comunitario.

### `centros_comunitarios.csv`

Base de datos con los centros comunitarios disponibles para seleccionar dentro de la aplicación.

### `centros_diagnostico_db.csv`

Archivo donde se almacenan las respuestas capturadas en el formulario de diagnóstico.

### `Matriz de Centros.xlsx`

Archivo de referencia con información relacionada con los centros comunitarios.

## Requisitos

Para ejecutar el proyecto se recomienda contar con Python 3.8 o superior.

Instala las dependencias principales con:

```bash
pip install pandas numpy streamlit pillow
```

## Ejecución

Para correr la aplicación localmente:

```bash
streamlit run diagnostico_centros.py
```

Después de ejecutar el comando, Streamlit abrirá la aplicación en el navegador.

## Consideraciones

Actualmente el script utiliza rutas locales absolutas de Windows, por ejemplo:

```python
C:\NL\centros_comunitarios\diagnostico
```

Si se desea ejecutar el proyecto en otra computadora, es necesario ajustar estas rutas o reemplazarlas por rutas relativas dentro del repositorio.

Ejemplo recomendado:

```python
centros = pd.read_csv("centros_comunitarios.csv", encoding="latin-1")
```

y

```python
df.to_csv("centros_diagnostico_db.csv", index=False)
```

## Uso esperado

1. Ejecutar la aplicación con Streamlit.
2. Seleccionar el centro comunitario a diagnosticar.
3. Completar las secciones del formulario.
4. Adjuntar evidencia fotográfica.
5. Presionar el botón **Enviar**.
6. Confirmar que la información fue guardada correctamente.

## Objetivo del proyecto

Facilitar la captura, organización y almacenamiento de información sobre el estado operativo, humano, material y físico de los centros comunitarios de Nuevo León.

## Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- NumPy
- Pillow

## Estado del proyecto

Proyecto en desarrollo para uso interno en actividades de diagnóstico y valoración de centros comunitarios.
