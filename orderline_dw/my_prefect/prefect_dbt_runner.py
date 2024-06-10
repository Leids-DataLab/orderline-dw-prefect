"""
Deze module runt DBT taken.

De DBT API waarmee je vanuit python DBT aanroept is nog niet stabiel. Zie https://docs.getdbt.com/reference/programmatic-invocations 

Daarom is het verstandig om de code die DBT aanroept op één plek te houden (encapsulatie).
"""
import logging
from enum import Enum

from prefect import get_run_logger
from prefect_dbt import DbtCoreOperation
from dbt.cli.main import dbtRunner

class DBTCommands(Enum):
    RUN = "run"
    SEED = "seed"
    TEST = "test"
    SNAPSHOT = "snapshot"


def _run_dbt_with_dbt_invoke(command, models=None):
    dbt = dbtRunner()
    if models:
        result = dbt.invoke([command.value, "--models", models])
    else:
        result = dbt.invoke([command.value])
 
    logger = get_run_logger()

    # We willen de aanroepende task laten falen als DBT niet succesvol draait.
    if not result.success:
        if result.exception:
            # Zo gooien we de oorspronkelijke fout in DBT door.
            raise result.exception
        else:
            for r in result.result:
                logger.info(f"DBT: {r.node.name}: {r.status}")            

    # Als de task wel succesvol is, schrijf het resultaat naar de log.
    for r in result.result:
        logger.info(f"DBT: {r.node.name}: {r.status}")


def _run_dbt_with_subprocess(command, models=None):
    pass
    # Mocht het ooit gewenst zijn DBT als subprocess te runnen, dat doe je ongeveer zo (inclusief logging):
    # 
    # logger = get_run_logger()
    # # Voer het DBT commando uit en vang de output op.
    # result = subprocess.run(f"dbt run -m telbestanden --target {config.env}", check=True, text=True, capture_output=True)
    # # Log de standaard output naar Prefect logs.
    # logger.info(result.stdout)


def _run_dbt_with_prefect_dbt(command, models=None, vars={}):
    if models:
        dbt_command = f"dbt {command.value} --models {models}"
    else:
        dbt_command = f"dbt {command.value}"

    dbt_task = DbtCoreOperation(
        commands=[dbt_command],
        project_dir=".",
        profiles_dir=".",
        vars=vars
    )

    dbt_task.run()


def run_dbt(command, models=None, vars={}):
    """
    Voert het DBT commando uit op een environment.
    :param command: Het DBT commando dat gerund moet worden.
    :param models: De modellen die DBT runt (alleen van toepassing bij het run commando) 
    """
    _run_dbt_with_prefect_dbt(command, models, vars)
