from prefect import task, flow

from orderlinedw_prefect.prefect_dbt_runner import run_dbt, DBTCommands

@task
def load_datum_dimensie():
    run_dbt(DBTCommands.SEED)


@flow
def init_flow():
    load_datum_dimensie()


if __name__ == "__main__":
    init_flow()

