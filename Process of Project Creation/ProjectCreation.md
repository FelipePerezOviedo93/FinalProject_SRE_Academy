# Desarrollo de Proyecto por pasos

## Creación del repositorio 
![alt text](image.png)

![alt text](image-1.png)

## Construcción de la imagen
![alt text](image-4.png)

## Agregar un tag a la imagen

docker tag library_costarica-app:latest felipeperezo/library_costarica-app:latest

docker push docker push felipeperezo/library_costarica-app:latest

![alt text](image-5.png)

Confirmar que Minikube este corriendo y muestre sus pods y replicas

![alt text](image-6.png)

Revisión de Ansible 
 ansible-inventory -i inventory.ini --list
![alt text](image-7.png)

Ansible allhosts -m ping -i inventory.ini
![alt text](image-8.png)

Aplicación de todos los archivos de configuración
<img width="1352" height="897" alt="Applying configuration files" src="https://github.com/user-attachments/assets/8a71ef75-0a79-450b-b7c1-7f637462e2da" />

Aplicación y confirmación del role
![alt text](image-13.png)

Confirmar que los pods de Prometheous esten en ejecución
![alt text](image-9.png)

Métricas de Promeheous
<img width="2192" height="593" alt="image" src="https://github.com/user-attachments/assets/e3aec226-b41e-4165-946c-2bc99c1d61fd" />

Revisión del servicio de Grafana
![alt text](image-10.png)

Visualización de Grafana
![alt text](image-11.png)

Grafana scraping
![alt text](image-14.png)
![alt text](image-15.png)

Lectura de libros, por medio de swagger
<img width="2477" height="1118" alt="FastAPI docs site" src="https://github.com/user-attachments/assets/1810c612-2822-4638-a77f-1cae269d478b" />
