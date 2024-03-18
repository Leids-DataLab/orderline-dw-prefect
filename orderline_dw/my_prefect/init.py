from prefect import task, flow

from orderline_dw.my_prefect.prefect_dbt_runner import run_dbt, DBTCommands

@task
def load_datum_dimensie():
    run_dbt(DBTCommands.SEED)


@flow
def init_flow():
    load_datum_dimensie()


if __name__ == "__main__":
    init_flow()

