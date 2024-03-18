from prefect import flow

from orderline_dw.my_prefect import initial_load
from orderline_dw.my_prefect import init

@flow
def all_flow():
    init.init_flow()
    initial_load.initial_load_flow()


if __name__ == "__main__":
    all_flow()

