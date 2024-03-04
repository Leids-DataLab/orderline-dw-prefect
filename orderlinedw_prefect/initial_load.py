from prefect import task, flow

from orderlinedw_scripts import oltp2staging
from orderlinedw_prefect.prefect_dbt_runner import run_dbt, DBTCommands

@task
def task_oltp2staging():    
    oltp2staging.execute()
        

@task
def staging2dmsales():
    run_dbt(DBTCommands.RUN)


@flow
def initial_load_flow():
    dependency_task_oltp2staging = task_oltp2staging()
    staging2dmsales(wait_for=[dependency_task_oltp2staging])


if __name__ == "__main__":
    initial_load_flow()
