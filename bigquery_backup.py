from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess, json

gcs_bucket = '<gcs bucket name>'
default_arguments = {"owner": "<dag owner>", "retries": 0}

def bq_backup():
   backup_contents = subprocess.run(['bq', '--format=json', 'ls', '--max_results', '10000'], stdout=subprocess.PIPE, universal_newlines=True)
   backup_contents = json.loads(backup_contents.stdout) # array of dicts
   for a_dataset in backup_contents:
     dataset_contents = subprocess.run(['bq', '--format=json', 'ls', '--max_results', '10000', a_dataset['id']], stdout=subprocess.PIPE, universal_newlines=True)
     if len(dataset_contents.stdout) > 0:  # Check if there are any schema objects in the dataset
       dataset_contents = json.loads(dataset_contents.stdout)
       for schema_obj in dataset_contents:
         if schema_obj['type'] == 'TABLE':  #Backup only tables
           # Build backup file name
           backup_file = 'gs://{}/{}/{}-*.avro'.format(gcs_bucket, datetime.now().strftime("%Y_%m_%d"), schema_obj['id'])
           backup_job = subprocess.run(['bq', 'extract', '--destination_format=AVRO', '--use_avro_logical_types', schema_obj['id'], backup_file], stdout=subprocess.PIPE, universal_newlines=True)
	     # End if backup only tables
       # End schema_obj for loop
     # End if len() check
   # End outer for

with DAG('bq_backup_dag', default_args = default_arguments, description='backup bigquery data to gcs bucket', schedule_interval='*/5 * * * *', start_date=datetime(2022, 7, 28), catchup=False) as dag:
  backup_task	= PythonOperator(task_id='bq_backup_task', python_callable=bq_backup)

backup_task

