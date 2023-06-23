# PEER Review Document

# Aswat's code:

### Docker assignment
1. He created a custom airflow image with psycopg-2 installed in it.
2. He used Celery executor.
3. He also mounted dags folder inside the airflow container to a dags folder in his local system.
4. He used kwargs to get dag's current execution time.

* I have used local executor.
* I have used DagRun to get Dag execution time.

### Kubernetes assignment  
1. He used helm chart to create postgres pods and service.
2. He then installed python and airflow inside the postgres container created.
3. He then initialised it as airflow database by running airflow db init inside it.
4. He created airflow deployment by using airflow image.
5. He put his python script inside the dags folder of airflow-scheduler manually.
6. Then he created an airflow service of type LoadBalancer to log in to airflow webserver using local system.

* I have created my own postgres deployment and service instead of using postgres helm chart.
* I have also used my custom airflow image to create airflow deployment.


# Aayush's Approach

### Docker
1. Wrote a python script to create dag in which there were tasks: create a table and insert data into table<br>
2. Created a connection to connect the database to airflow<br>
3. Created docker-compose file with all the different services required.<br>
4. Started the containers.<br>
5. Triggered the dag and verified the data in the postgres container.<br>

### Kubernetes
1. Made a custom postgres image which will be used as airflow database.<br>
2. Add the image to minikube<br>
3. Created a pod using the postgres-deployment.yaml file<br>
4. Initialised the database<br>
5. Created a service using postgres-service.yaml file.<br>
6. Created a persistent volume to mount dag directory in airflow using volumes.yaml file.<br>
7. Created a service using airflow-service.yaml file.<br>
8. Started the airflow webserver using command: <b>minikube service airflow</b> <br>
