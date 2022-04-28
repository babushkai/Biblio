#!/bin/bash
# https://cloud.google.com/composer/docs/how-to/using/testing-dags

export ENV=
export REGION=
GKE=$(gcloud composer environments describe ENV --location REGION | grep gkeCluster: | grep -oE '[^/]+$')
gcloud containers clusters get-credentials $GKE --region REGION
kubectl get pods --all-namespaces | grep worker 

kubectl -n $NAME_SPACE exec -it WORKER_NAME bash


# print the list of active DAGS
airflow dags list
# print the lists of tasks in the "Composer_sample_quickstart" dag_id
airflow tasks list DAG
# print the hierarchy of tasks in the "Composer_sample_quickstart" dag_id
airflow tasks list Composer_sample_quickstart --tree

# command layout: command sucommand dag_id task_id date
airflow test DAG task date