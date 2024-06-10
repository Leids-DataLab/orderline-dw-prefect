"""
Dit is de CLI voor deze package. Hiermee kun je vanuit de CLI flows runnen of serven.
"""
from importlib.metadata import version

import click
from prefect import serve

from orderline_dw.my_prefect import init_and_full_load as init_and_full_load_flow, load
from orderline_dw.my_prefect import init as init_flow


@click.group()
@click.option('--mode', type=click.Choice(['run', 'serve']), required=True)
@click.pass_context
def main(ctx, mode):
    # Geef mode door aan de context.
    ctx.ensure_object(dict)
    ctx.obj['mode'] = mode
    

def flow_helper(flow, mode):
    """
    Deze functie runt of servet de meegegeven flow.
    :param flow: De flow.
    :param mode: Bepaalt of de flow gerund of geserved wordt.
    """
    if mode == 'run':
        click.echo(f"Run de flow {flow.__name__}")
        flow()
    elif mode == 'serve':
        click.echo(f"Serveer de flow {flow.__name__}")
        flow.serve(
            name = f"{flow.__name__}_deployment",
            version=version("orderline_dw")
        )


@main.command()
@click.pass_context
def fullload(ctx):
    flow_helper(flow=load.full_load_flow, mode=ctx.obj['mode'])


@main.command()
@click.pass_context
def incrementalload(ctx):
    flow_helper(flow=load.incremental_load_flow, mode=ctx.obj['mode'])


@main.command()
@click.pass_context
def init(ctx):
    flow_helper(flow=init_flow.init_flow, mode=ctx.obj['mode'])


@main.command()
@click.pass_context
def initandfullload(ctx):
    flow_helper(flow=init_and_full_load_flow.init_and_full_load_flow, mode=ctx.obj['mode'])


@main.command()
@click.pass_context
def serveallflows(ctx):
    d1 = init_flow.init_flow.to_deployment(name = "init_flow_deployment", version=version("orderline_dw"))
    d2 = load.full_load_flow.to_deployment(name = "full_load_flow_deployment", version=version("orderline_dw"))
    d3 = load.incremental_load_flow.to_deployment(name = "incremental_load_flow_deployment", version=version("orderline_dw"))
    d4 = init_and_full_load_flow.init_and_full_load_flow.to_deployment(name = "init_and_full_load_flow_deployment", version=version("orderline_dw"))
    serve(d1, d2, d3, d4)


if __name__ == "__main__":
    main()
