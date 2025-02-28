#1.- SO Y Python

FROM python:3.12-slim

#2.- Crear carpeta de trabajo

WORKDIR /app

#3.- Importar proyecto a la carpeta

COPY . /app

#EL . significa que copiará todo

# 4.- Instalar dependencias.

RUN pip install --no-cache-dir -r requirements.txt

#5.- Exponer el puerto

EXPOSE 5000

# Ejecutar el proyecto

CMD ["python", "app.py"]