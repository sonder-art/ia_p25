# 1) Seleccionamos una imagen base ligera de Python
FROM python:3.11-slim

# 2) Ajustamos variables de entorno para evitar prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# 3) Actualizamos paquetes básicos
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4) Actualizamos pip
RUN pip install --upgrade pip

# 5) Creamos un usuario no-root para seguir buenas prácticas
RUN useradd -ms /bin/bash jupyter
USER jupyter

# 6) Establecemos el directorio de trabajo (HOME del usuario)
WORKDIR /home/jupyter

# 7) Copiamos el archivo de requerimientos
COPY --chown=jupyter:jupyter requirements.txt .

# 8) Instalamos dependencias y jupyterlab
RUN pip install -r requirements.txt \
    && pip install jupyterlab

# 9) Configuramos JupyterLab para tema oscuro
RUN mkdir -p /home/jupyter/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/ \
    && echo '{ \
  "theme": "JupyterLab Dark" \
}' > /home/jupyter/.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings

# 10) Exponemos el puerto de JupyterLab
EXPOSE 8888

# 11) Comando para lanzar JupyterLab sin password o token
CMD ["jupyter", "lab", \
     "--ip=0.0.0.0", \
     "--no-browser", \
     "--NotebookApp.token=''", \
     "--NotebookApp.password=''"]
