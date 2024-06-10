from prefect import task, flow

from orderline_dw.scripts import oltp2staging
from orderline_dw.my_prefect.prefect_dbt_runner import run_dbt, DBTCommands

@task
def task_oltp2staging():    
    oltp2staging.execute()
        

@task
def staging2dmsales_full():
    run_dbt(DBTCommands.SNAPSHOT)
    run_dbt(DBTCommands.RUN, vars={"sales_materialization": "table"})


@task
def staging2dmsales_incremental():
    run_dbt(DBTCommands.SNAPSHOT)
    run_dbt(DBTCommands.RUN)


@flow
def full_load_flow():
    dependency_task_oltp2staging = task_oltp2staging()
    staging2dmsales_full(wait_for=[dependency_task_oltp2staging])


@flow
def incremental_load_flow():
    dependency_task_oltp2staging = task_oltp2staging()
    staging2dmsales_incremental(wait_for=[dependency_task_oltp2staging])


if __name__ == "__main__":
    full_load_flow()
    # incremental_load_flow()
