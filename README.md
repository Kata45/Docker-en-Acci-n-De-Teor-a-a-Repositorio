![Docker Logo](https://www.docker.com/app/uploads/2024/02/docker-default-meta-image.png)

---

<div align="center">

<h1>🐳 Docker en Acción </h1>

> ## 👩🏻‍💻**Kata**
> **Objetivo:** Crear un informe que recopile fundamentos claves sobre Docker, mostrar algunas reflexiones personales al respecto y desarrollar un ejercicio práctico donde se muestre la utilización de los conceptos aprendidos.

</div>

---

<div align="center">
<h2>🐳 Docker</h2>
</div>

**Definición**

Docker es una plataforma de software que permite crear, desplegar y ejecutar aplicaciones dentro de contenedores.
Un contenedor es una unidad ligera y portátil que incluye todo lo necesario para ejecutar una aplicación: código, dependencias, bibliotecas, y configuraciones del sistema, de forma aislada del sistema operativo anfitrión.
En otras palabras, Docker permite que una aplicación funcione igual en cualquier entorno, ya sea en tu computadora, en un servidor o en la nube.

**Función**

El objetivo de Docker es aislar aplicaciones para asegurar que se ejecuten de manera consistente y reproducible.
Algunas funciones clave son:
- Estandarización del entorno: evita el típico problema de “en mi máquina sí funciona”.
- Portabilidad: los contenedores se pueden mover fácilmente entre entornos.

**Eficiencia**

Los contenedores son más ligeros que las máquinas virtuales, porque comparten el mismo kernel del sistema operativo.

**Escalabilidad** 

Se integra fácilmente con sistemas de orquestación como Kubernetes para manejar múltiples contenedores.

Automatización del despliegue: permite definir entornos y servicios mediante archivos de configuración.

---

<div align="center">
<h2>💻 Modo de uso básico</h2>
</div>


El flujo de uso de Docker suele seguir estos pasos:

1. Es necesario [instalar Docker](https://www.docker.com) en nuestro dispositivo, no importa si somos usuarios de sistemas Windows, macOS o Linux. En la [página oficial](https://www.docker.com/products/docker-desktop/) podemos encontrar una breve guía con el paso a paso para su instalación. 
2. Luego de la instalación exitosa de Docker haremos uso de los comandos en consola, por ejemplo: docker pull, run, ps, stop, rm, etc.
  
---

<div align="center">
<h2>📌 Conceptos fundamentales</h2>
</div>

* **Contenedores:** Empaquetan la aplicación y sus dependencias. Portables, reproducibles y ligeros.
* **Imágenes:** Plantillas inmutables formadas por capas.
* **Repositorios:** Lugares donde se almacenan imágenes (Docker Hub público y privados).
* **Comparativa con máquinas virtuales:** Docker virtualiza a nivel de aplicación y usa el kernel del host → mucho más rápido y liviano.
* **Docker Desktop:** Incluye CLI, Docker Engine y Docker Compose. Se instala fácilmente en Windows, Mac o Linux.

---

<div align="center">
<h2>💭 Reflexiones personales</h2>
</div>

**Ventajas:**

* Portabilidad total entre equipos y entornos.
* Fácil despliegue y replicación de configuraciones.
* Estandariza los entornos de desarrollo.

**Desafíos:**

* Aprender el manejo correcto de redes y volúmenes.
* Mantener buenas prácticas de seguridad (no usar imágenes sin verificar).
* Comprender la persistencia de datos, ya que los contenedores son efímeros.

**Usos prácticos:**

* Montar entornos de desarrollo reproducibles.
* Ejecutar servicios de forma ligera sin depender de configuraciones locales.
* Preparar pipelines CI/CD automatizados.

---

<div align="center">
<h2>📤 Comandos Docker</h2>
</div>

| Categoría                    | Comando                                 | Descripción / Ejemplo                                               |
| ---------------------------- | --------------------------------------- | ------------------------------------------------------------------- |
| **Gestión de imágenes**      | `docker pull <imagen>[:tag]`            | Descarga una imagen desde Docker Hub. Ej: `docker pull python:3.11` |
|                              | `docker images`                         | Lista las imágenes locales.                                         |
|                              | `docker rmi <imagen>`                   | Elimina una imagen local.                                           |
| **Construcción de imágenes** | `docker build -t <nombre>:<tag> <ruta>` | Crea una imagen a partir de un Dockerfile.                          |
| **Contenedores**             | `docker create [opciones] <imagen>`     | Crea un contenedor sin ejecutarlo.                                  |
|                              | `docker start <nombre/id>`              | Inicia un contenedor ya creado.                                     |
|                              | `docker run [opciones] <imagen>`        | Crea y ejecuta un contenedor en un solo paso.                       |
|                              | `docker run -d`                         | Ejecuta el contenedor en modo background.                           |
|                              | `docker run --name <nombre>`            | Asigna un nombre personalizado.                                     |
|                              | `docker run -p <host:container>`        | Mapea puertos entre host y contenedor.                              |
|                              | `docker run -v <host:container>`        | Monta volúmenes.                                                    |
|                              | `docker ps`                             | Lista contenedores activos.                                         |
|                              | `docker ps -a`                          | Lista todos los contenedores.                                       |
|                              | `docker stop <nombre>`                  | Detiene un contenedor.                                              |
|                              | `docker rm <nombre>`                    | Elimina un contenedor detenido.                                     |
|                              | `docker logs <nombre>`                  | Muestra los logs de un contenedor.                                  |
|                              | `docker exec -it <nombre> /bin/sh`      | Accede al shell del contenedor.                                     |
| **Redes**                    | `docker network ls`                     | Lista redes creadas.                                                |
|                              | `docker network create <nombre>`        | Crea una nueva red.                                                 |
|                              | `docker run --network <nombre>`         | Conecta el contenedor a una red.                                    |
| **Volúmenes**                | `docker volume create <nombre>`         | Crea un volumen persistente.                                        |
|                              | `docker volume ls`                      | Lista volúmenes existentes.                                         |
|                              | `docker run -v <nombre>:/ruta`          | Usa un volumen dentro del contenedor.                               |
| **Docker Compose**           | `docker compose up`                     | Levanta los servicios definidos.                                    |
|                              | `docker compose up -d --build`          | Reconstruye y ejecuta en modo detached.                             |
|                              | `docker compose down`                   | Detiene y limpia los servicios.                                     |
| **Limpieza**                 | `docker system prune`                   | Limpia recursos no usados.                                          |
|                              | `docker image prune`                    | Elimina imágenes no usadas.                                         |

---
<div align="center">
<h1>🏃🏻‍♀️‍➡️ Ejemplo práctico </h1>
  
> ## **🧮 Calculadora simple en 🐍 Python + Docker 🐳**
> **Objetivo:** Este ejercicio demuestra cómo **crear un contenedor Docker que ejecute un script Python**.

</div>

### 🛠️ Estructura del proyecto

```
docker-calculadora/
├── calculadora.py
└── Dockerfile
```

### 🔨 Pasos para construir y ejecutar

1. **Construir la imagen:**

   ```bash
   docker build -t calculadora:1 .
   ```

2. **Ejecutar el contenedor:**

   ```bash
   docker run --name mi_calculadora calculadora:1
   ```

3. **Ver la salida:**
   La calculadora se ejecuta dentro del contenedor y muestra los resultados directamente en la terminal.

---

<h2>🌐 Webgrafía</h2>

* [Documentación oficial de Docker](https://docs.docker.com/get-started/)
* [Referencia Dockerfile](https://docs.docker.com/engine/reference/builder/)
* [Docker Hub](https://hub.docker.com/)
* [Python Oficial](https://www.python.org/doc/)
* [Aprende Docker ahora!](https://youtu.be/4Dko5W96WHg?si=gOCMmey2k8sk17xz)
* [DOCKER De NOVATO a PRO! ](https://youtu.be/CV_Uf3Dq-EU?si=Y6uUiK1eHwK0xveF)
  
---
##### © **2025** Creado por *Kata* — Todos los derechos reservados.
---
