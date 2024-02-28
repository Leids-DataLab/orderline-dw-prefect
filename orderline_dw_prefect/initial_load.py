from prefect import task, flow


@task
def oltp2staging():
    pass


@task
def staging2dmsales():
    pass


@flow
def initial_load_flow():
    task_oltp2staging = oltp2staging()
    staging2dmsales(wait_for=[task_oltp2staging])


if __name__ == "__main__":
    initial_load_flow()
