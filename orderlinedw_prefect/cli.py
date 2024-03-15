from importlib.metadata import version

import click

from orderlinedw_prefect import init as init_flow, initial_load, all as all_flow


@click.group()
@click.option('--mode', type=click.Choice(['run', 'serve']), required=True)
@click.pass_context
def main(ctx, mode):
    # Geef mode door aan de context.
    ctx.ensure_object(dict)
    ctx.obj['mode'] = mode
    

def flow_helper(flow, mode):
    if mode == 'run':
        click.echo(f"Run de flow {flow.__name__}")
        flow()
    elif mode == 'serve':
        click.echo(f"Serveer de flow {flow.__name__}")
        flow.serve(
            name = f"{flow.__name__}_deployment",
            version=version("orderlinedw_prefect")
        )


@main.command()
@click.pass_context
def initialload(ctx):
    flow_helper(flow=initial_load.initial_load_flow, mode=ctx.obj['mode'])


@main.command()
@click.pass_context
def init(ctx):
    flow_helper(flow=init_flow.init_flow, mode=ctx.obj['mode'])


@main.command()
@click.pass_context
def all(ctx):
    flow_helper(flow=all_flow.all_flow, mode=ctx.obj['mode'])


if __name__ == "__main__":
    main()
