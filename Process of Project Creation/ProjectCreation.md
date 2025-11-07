# Project Development

## Repository Creation
![alt text](image.png)

![alt text](image-1.png)

Building image
![alt text](image-4.png)


![alt text](image-5.png)
Taging the image
 docker tag library_costarica-app:latest felipeperezo/library_costarica-app:latest

 docker push docker push felipeperezo/library_costarica-app:latest

Minikube dashboard
![alt text](image-6.png)

Testing ansible
 ansible-inventory -i inventory.ini --list
![alt text](image-7.png)


ansible allhosts -m ping -i inventory.ini
![alt text](image-8.png)

Prometheous pods running
![alt text](image-9.png)

Grafana service
![alt text](image-10.png)

Grafana dashboard
![alt text](image-11.png)

Applying cAdvisor
![alt text](image-12.png)

Applying and confirming role
![alt text](image-13.png)

Grafana scraping data
![alt text](image-14.png)
![alt text](image-15.png)

Configuration of otel-collector and jaeger
![alt text](image-16.png)



Slack channel
![alt text](image-17.png)

![alt text](image-18.png)