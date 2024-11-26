# Usamos una imagen base de Python
FROM python:3.12-slim

# Seteamos el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copiamos los requisitos del proyecto y los instalamos
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código del proyecto
COPY . /code/

# Exponemos el puerto para el servidor
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
