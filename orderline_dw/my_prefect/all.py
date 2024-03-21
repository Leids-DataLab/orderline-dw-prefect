from prefect import flow

from orderline_dw.my_prefect import load
from orderline_dw.my_prefect import init

@flow
def all_flow():
    init.init_flow()
    load.full_load_flow()


if __name__ == "__main__":
    all_flow()

