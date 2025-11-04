# Imagen base de Python

FROM python:3.9-slim

# Crear carpeta de trabajo dentro del contenedor

WORKDIR /app

# Copiar el archivo de la aplicación

COPY calculadora.py .

# Ejecutar el script de Python

CMD ["python", "calculadora.py"]

