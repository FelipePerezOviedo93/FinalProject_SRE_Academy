# FinalProject_SRE_Academy

## Objetivo

El objetivo de este proyecto es crear una aplicacion en el lenguaje de programación de Python, esta consiste en una Librería, donde se podrán consultar por medio de métodos, todos los libros, por autor, o por categoría.
Con un objetivo de aprendar más sobre APIs, he decidido realizarlo en FAST API. En la aplicación existen métodos para consulta de los métodos anteriormente descritos, estos pueden ser consumidos o utilizados mediante /docs, donde se explicará posteriormente

## Prerequisitos
### Ambiente virtual

1. Asegurese de que Python esta instalado en su equipo
> python3 --version
2. Clone el repositorio
> git clone git@github.com:FelipePerezOviedo93/FinalProject_SRE_Academy.git <<Set a name to your folder>>
3.Cree un ambiente virtual y activelo
> python -m venv .venv
Activación del ambiente
* Windows - Powershell
> .venv\Scripts\Activate.ps1
* Windows - Bash
> source .venv/Scripts/activate
* Linux/MacOS
source .venv/bin/activate

### Instalaciones


## Crear una cuenta en Docker Hub
1. Visit https://hub.docker.com
2. Click Sign Up and follow the instructions
3. Confirm your email and login


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



---------------------------------------------------------------------------------------
Applying the deployment
---------------------------------------------------------------------------------------
kubectl apply -f deployment.yaml

---------------------------------------------------------------------------------------
Applying the service
---------------------------------------------------------------------------------------
kubectl apply -f service.yaml
kubectl get service library-costarica-app-service

---------------------------------------------------------------------------------------
Accesing the application
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
