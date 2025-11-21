# FinalProject_SRE_Academy
---
## Objetivo

El objetivo de este proyecto es crear una aplicacion en el lenguaje de programación de Python, esta consiste en una Librería, donde se podrán consultar por medio de métodos, todos los libros, por autor, o por categoría.
Con un objetivo de aprendar más sobre APIs, he decidido realizarlo en FAST API. En la aplicación existen métodos anteriormente descritos, estos pueden ser consumidos o utilizados mediante /docs, donde se explicará posteriormente

¿Qué es FAST API?
De acuerdo al sitio Tiangolo, FastAPI es un framework web moderno, rápido (de alto rendimiento), para construir APIs con Python basado en las anotaciones de tipos estándar de Python.
Las características clave son:
* Rápido: Muy alto rendimiento, a la par con NodeJS y Go (gracias a Starlette y Pydantic). Uno de los frameworks Python más rápidos disponibles.
* Rápido de programar: Aumenta la velocidad para desarrollar funcionalidades en aproximadamente un 200% a 300%. *
* Menos bugs: Reduce en aproximadamente un 40% los errores inducidos por humanos (desarrolladores). *
* Intuitivo: Gran soporte para editores. Autocompletado en todas partes. Menos tiempo depurando.
* Fácil: Diseñado para ser fácil de usar y aprender. Menos tiempo leyendo documentación.
* Corto: Minimiza la duplicación de código. Múltiples funcionalidades desde cada declaración de parámetro. Menos bugs.
* Robusto: Obtén código listo para producción. Con documentación interactiva automática.
* Basado en estándares: Basado (y completamente compatible) con los estándares abiertos para APIs: OpenAPI (anteriormente conocido como Swagger) y JSON Schema.

¿Qué es Swagger UI?

Swagger UI permite que cualquier persona ya sea su equipo de desarrollo o sus consumidores finales, visualice e interactúe con los recursos de la API sin tener ninguna lógica de implementación implementada. Se genera automáticamente a partir de su especificación OpenAPI (anteriormente conocida como Swagger), y la documentación visual facilita la implementación del back-end y el consumo del lado del cliente.
Al ejecutar FASTAPI, se puede acceder yendo a /docs
http://127.0.0.1:8000/docs

---

## Prerequisitos
Para realizar la ejecución de este ejercicio, se require de herramientas tales como:
* Python
* Minikube
* Prometheus
* Grafana
* Docker

### Crear una cuenta en Docker Hub
1. Visite https://hub.docker.com
2. Click Sign Up y siga las instrucciones
3. Confirme el email y haga login
   
---

## Instalaciones

### Python
* sudo apt update
* sudo apt install -y python3 python3-pip python3-venv

### Docker
* sudo mkdir -p /etc/apt/keyrings
* curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
* echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
* sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

### Minikube
* curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
* sudo install minikube-linux-amd64 /usr/local/bin/minikube

### Kubectl

* curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
* chmod +x kubectl
* sudo mv kubectl /usr/local/bin/

## Verificacion de aplicaciones instaladas

* python3 --version
* pip3 --version
* docker run hello-world
* kubectl version --client
* minikube version


---

## Explicacion de archivos

### Dockerfile

* Crea un contenedor basado en Python 3.10
* Copia dependencias y ademas las instala
* Copia tu código
* Expone el puerto 8000
* Ejecuta FastAPI con Uvicorn cuando arranca el contenedor
* [Ver Archivo](https://github.com/FelipePerezOviedo93/FinalProject_SRE_Academy/blob/main/app/Dockerfile)

### Deployment.yaml

* Despliega la aplicación library-costarica-app
* Mantiene 3 réplicas siempre corriendo
* Aplica la etiqueta app: library-costarica-app
* Usa la imagen Docker:felipeperezo/library_costarica-app:latest
* Expone internamente el puerto 8000 (dentro del Pod)
* [Ver Archivo](https://github.com/FelipePerezOviedo93/FinalProject_SRE_Academy/blob/main/deployment.yaml)

### Service.yaml

* Kubernetes busca todos los Pods con app: library-costarica-app.
* Los agrupa bajo un solo "endpoint virtual" llamado library-costarica-app-service.
* Expone el puerto 8000 del contenedor al Service
* Como es NodePort, lo expone fuera del cluster en un puerto 
* [Ver Archivo](https://github.com/FelipePerezOviedo93/FinalProject_SRE_Academy/blob/main/service.yaml)

### Prometheus.yaml
* Namespace	Crea un espacio para Prometheus y otros sistemas de monitoreo
* ConfigMap	Define el archivo de configuración prometheus.yml
* Deployment	Ejecuta Prometheus con esa configuración
* Service NodePort	Te permite acceder a Prometheus desde tu PC
* [Ver Archivo](https://github.com/FelipePerezOviedo93/FinalProject_SRE_Academy/blob/main/prometheus.yaml)

### Grafana.yaml

* Deployment	Levanta el servidor Grafana
* Service NodePort	Lo expone en el puerto 3000 hacia tu PC
* ConfigMap datasources	Configura Prometheus y Loki automáticamente
* ConfigMap dashboards	Carga dashboards listos para usarse
*  [Ver Archivo](https://github.com/FelipePerezOviedo93/FinalProject_SRE_Academy/blob/main/grafana.yaml)

### cAdvisor.yaml
* Instala cAdvisor en todas las máquinas del clúster.
* Expone métricas en puerto 8080.
* Permite que Prometheus las lea.
* Monta volúmenes del host para obtener información real del contenedor.
* Usa un DaemonSet porque las métricas deben obtenerse de cada nodo.
* [Ver Archivo](https://github.com/FelipePerezOviedo93/FinalProject_SRE_Academy/blob/main/cadvisor.yaml)
 
### Prometheus-rbac-cluster.yaml
* Este archivo define los permisos (RBAC) necesarios para que Prometheus pueda descubrir y leer información del clúster Kubernetes.
* ServiceAccount	Identidad del Pod de Prometheus
* ClusterRole	Lista de permisos de lectura sobre el clúster
* ClusterRoleBinding	Conecta la identidad con los permisos
* [Ver Archivo](https://github.com/FelipePerezOviedo93/FinalProject_SRE_Academy/blob/main/prometheus-rbac-cluster.yaml)

---
## Configuración de la aplicación

* ### Iniciar docker
minikube start --driver=docker

* ### Construccción de la imagen
docker build -t library_costarica-app .
docker tag library_costarica-app:latest felipeperezo/library_costarica-app:latest

* ### Push de la imagen
docker push felipeperezo/library_costarica-app:latest

* ### Correr la imagen
docker run --rm -it -p 5000:5000 felipeperezo/library_costarica-app

* ### Aplicar un deployment
kubectl apply -f deployment.yaml

* ### Aplicar el servicio
kubectl apply -f service.yaml

* ### Listar  todos los pods
kubectl get pods -A

* ### Revisar los pods de monitoreo
kubectl get pods -n monitoring

* ### Acceder a la aplicación
minikube service library-costarica-app-service --url

* ### Revisar el role creado
kubectl get clusterrolebinding prometheus-pod-reader-binding-cluster
 
* ### Acceder a Grafana
minikube service grafana-service -n monitoring

* ### Acceder a Prometheus
minikube service prometheus-service -n monitoring
---
