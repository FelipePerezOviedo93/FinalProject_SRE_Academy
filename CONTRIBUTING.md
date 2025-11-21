# Contributing Guide

¡Gracias por tu interés en contribuir a este proyecto! Este repositorio
integra **Python (FastAPI), Docker, Kubernetes, Prometheus y Grafana**,
por lo que este documento describe el proceso para poder colaborar
------------------------------------------------------------------------

## Requisitos Previos

-   Python 3.10+
-   pip y venv
-   Docker 
-   Git
-   kubectl
-   Minikube o un clúster Kubernetes compatible

Para clonar el proyecto:

``` bash
git clone https://github.com/<your-user>/<repo>.git
cd <repo>
```

------------------------------------------------------------------------

##  2. Configuración del Entorno

### Crear entorno virtual

``` bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Ejecutar el proyecto localmente

``` bash
uvicorn main:app --reload
```

------------------------------------------------------------------------

## 3. Ejecución con Docker

### Construir imagen

``` bash
docker build -t library-app:dev .
```

### Ejecutar contenedor

``` bash
docker run -p 8000:8000 library-app:dev
```

------------------------------------------------------------------------

##  Kubernetes: Cómo probar tus cambios

### Iniciar Minikube

``` bash
minikube start --driver=docker
```

### Aplicar los manifiestos

``` bash
kubectl apply -f k8s/
```

### Verificar Pods

``` bash
kubectl get pods -A
```

### Exponer servicios en Minikube

Prometheus:

``` bash
minikube service prometheus-service -n monitoring --url
```

Grafana:

``` bash
minikube service grafana-service -n monitoring --url
```

------------------------------------------------------------------------

## 5. Métricas y Observabilidad

Si agregas métricas o dashboards:

### Confirmar scrap de Prometheus

``` bash
kubectl port-forward svc/prometheus-service -n monitoring 9090:9090
```

Entrar a:

    http://localhost:9090

### Confirmar dashboards en Grafana

``` bash
kubectl port-forward svc/grafana-service -n monitoring 3000:3000
```

Entrar a:

    http://localhost:3000

------------------------------------------------------------------------

## 6. Seguridad

No envíes:

-   Webhooks
-   Tokens
-   Contraseñas
-   Credenciales
-   Configuración sensible

Usa variables de entorno o Kubernetes Secrets.

------------------------------------------------------------------------

## 7. Flujo de Branches

### Crear una rama

``` bash
git checkout -b feature/<nombre>
```

Convenciones:

-   `feature/...`
-   `fix/...`
-   `hotfix/...`
-   `docs/...`

------------------------------------------------------------------------

##  8. Pull Requests

1.  Rebase antes de enviar:

``` bash
git fetch origin
git rebase origin/main
```

2.  Commit:

``` bash
git add .
git commit -m "feat: descripción clara del cambio"
```

3.  Push:

``` bash
git push origin feature/<nombre>
```

4.  Crea el PR con:

-   Descripción del cambio
-   Cómo probarlo
-   Impacto en K8s/Prometheus/Grafana
-   Evidencia si aplica

------------------------------------------------------------------------

## 9. Código de Conducta

Este proyecto sigue principios de:

-   Respeto mutuo
-   Comunicación clara
-   Críticas constructivas
-   Trabajo colaborativo

------------------------------------------------------------------------

## 10. Gracias por Contribuir

Tu ayuda es valiosa, ya sea con:

-   Código
-   Tests
-   Documentación
-   Dashboards
-   Config K8s
-   Métricas

Para dudas, abre un Issue.
