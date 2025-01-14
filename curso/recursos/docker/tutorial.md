# Docker de Jupyter-Lab

Este tutorial describe cómo construir y usar una imagen de Docker que:

- Carga JupyterLab en modo oscuro.
- No solicita password ni token.
- Permite montar una carpeta local para guardar tu trabajo.

---
## 0.Como usar
Este dockerfile lo puedes usar para cada uno de los proyectos, pero si lo ejecutas directamente aqui habra problemas, pues no tiene acceso al codigo del curso ademas de que jamas bajo ninguna circustancia deberias de de modifcar archivos en la carpeta del curso. Todo va en tu carpeta de alumnos.  
### Tutorial de Docker
[Link a tutorial de docker](https://www.youtube.com/embed/CV_Uf3Dq-EU?start=74)
<iframe width="560" height="315" 
        src="https://www.youtube.com/embed/CV_Uf3Dq-EU?start=74" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen>
</iframe>
## 1. Requisitos Previos

1. **Docker instalado**  
   - En Windows (WSL2 nunca directo en windows) o macOS, instala [Docker Desktop](https://www.docker.com/products/docker-desktop/).  
   - En Linux, instala Docker según tu distribución (Ubuntu, Fedora, etc.).

2. **Archivos necesarios**  
   - `Dockerfile`  
   - `requirements.txt`  
   Ambos deben estar en la misma carpeta.

3. **Carpeta local**  
   - Asegúrate de tener una carpeta local (por ejemplo, `my_notebooks`) donde quieras guardar los cuadernos de Jupyter. Esta carpeta será montada dentro del contenedor para persistir los cambios.

---

## 2. Construir la Imagen

### Montando Volumen
```bash
docker run -it --rm \
  -p 8888:8888 \
  -v /ruta/a/tu/my_notebooks:/home/jupyter/work \
  jupyter-lab-dark
```

### Sin montar el Volumen (probablemente hay que evitarlo)
1. **Ubícate en la carpeta** donde se encuentren el `Dockerfile` y el `requirements.txt`.  
2. **Ejecuta** el siguiente comando para construir la imagen:

```bash
docker build -t jupyter-lab-dark .
```
Abre tu navegador web y dirígete a:
## 3. Acceder a la imagen construida

```
http://localhost:8888

```