# FinalProject_SRE_Academy

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

## Prerequisitos
Para realizar la ejecución de este ejercicio, se require de herramientas tales como:
* Python
* Minikube
* Prometheus
* Grafana
* Docker



### Instalaciones

## Explicacion de archivos
### Prometheus.yaml
* Al definir el namespace de tipo *monitoring, permitira mantener los recursos del mismo tipo aislados del resto del cluster y de forma ordenada
* La seccion de configmap, contiene la configuracion 

## Crear una cuenta en Docker Hub
1. Visite https://hub.docker.com
2. Click Sign Up y siga las instrucciones
3. Confirme el email y haga login


## Configuración de la aplicación

### Iniciar docker
minikube start --driver=docker

### Construccción de la imagen
docker build -t library_costarica-app .
docker tag library_costarica-app:latest felipeperezo/library_costarica-app:latest

### Push de la imagen
docker push felipeperezo/library_costarica-app:latest

### Correr la imagen
docker run --rm -it -p 5000:5000 felipeperezo/library_costarica-app

### Aplicar un deployment
kubectl apply -f deployment.yaml

### Aplicar el servicio
---------------------------------------------------------------------------------------
kubectl apply -f service.yaml
kubectl get service library-costarica-app-service

### Acceder a la aplicación the 
---------------------------------------------------------------------------------------
minikube service library-costarica-app-service --url

---------------------------------------------------------------------------------------
Opening Grafana
---------------------------------------------------------------------------------------
minikube service grafana-service -n monitoring
---------------------------------------------------------------------------------------

Accessing Prometheus

minikube service prometheus-service -n monitoring

 kubectl get pods -n monitoring
