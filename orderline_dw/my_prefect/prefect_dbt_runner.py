"""
Deze module runt DBT taken.

De DBT API waarmee je vanuit python DBT aanroept is nog niet stabiel. Zie https://docs.getdbt.com/reference/programmatic-invocations 

Daarom is het verstandig om de code die DBT aanroept centraal te houden.
"""
from enum import Enum

from prefect import get_run_logger
from dbt.cli.main import dbtRunner

class DBTCommands(Enum):
    RUN = "run"
    SEED = "seed"

# TODO Beter is het om het pad uit de orderlinedw_dbt package te halen.
PATH_DBT_PROJECT = "."

def run_dbt(command, models=None):
    """
    Voert het DBT commando uit op een environment.
    :param command: Het DBT commando dat gerund moet worden.
    :param env: De environment waarop we DBT runnen.
    :param models: De modellen die DBT runt (alleen van toepassing bij het run commando) 
    """
    dbt = dbtRunner()
    logger = get_run_logger()
    if models:
        logger.info(f"Roep DBT {command.value} aan met models={models}.")
        result = dbt.invoke([command.value], project_dir=PATH_DBT_PROJECT, profiles_dir=PATH_DBT_PROJECT, models=models)
    else:
        logger.info(f"Roep DBT {command.value} aan.")
        result = dbt.invoke([command.value], project_dir=PATH_DBT_PROJECT, profiles_dir=PATH_DBT_PROJECT)
 
    # We willen de aanroepende task laten falen als DBT niet succesvol draait.
    if not result.success:
        raise result.exception

    # Als de task wel succesvol is, schrijf het resultaat naar de log.
    for r in result.result:
        logger.info(f"DBT: {r.node.name}: {r.status}")

    
    # Mocht het ooit gewenst zijn DBT als subprocess te runnen, dat doe je ongeveer zo (inclusief logging):
    # 
    # logger = get_run_logger()
    # try:
    #     # Voer het DBT commando uit en vang de output op.
    #     result = subprocess.run(f"dbt run -m telbestanden --target {config.env}", check=True, text=True, capture_output=True)
    #     # Log de standaard output naar Prefect logs.
    #     logger.info(result.stdout)
    # except subprocess.CalledProcessError as e:
    #     # Log de error output naar Prefect logs als het commando faalt.
    #     logger.error(e.stderr)
    #     raise e



