from prefect import flow

from orderlinedw_prefect import init, initial_load

@flow
def all_flow():
    init.init_flow()
    initial_load.initial_load_flow()


if __name__ == "__main__":
    all_flow()

