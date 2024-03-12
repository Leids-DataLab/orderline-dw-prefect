from importlib.metadata import version

import click

from orderlinedw_prefect import initial_load


@click.group()
@click.option('--mode', type=click.Choice(['run', 'serve']), required=True)
@click.pass_context
def main(ctx, mode):
    # Geef mode door aan de context.
    ctx.ensure_object(dict)
    ctx.obj['mode'] = mode


@main.command()
@click.pass_context
def initialload(ctx):
    mode = ctx.obj['mode']
    if mode == 'run':
        click.echo(f"Run de init flow voor environment TODO.")
        initial_load.initial_load_flow()
    elif mode == 'serve':
        click.echo(f"Serveer de init flow voor environment TODO.")
        initial_load.initial_load_flow.serve(
            name="initial_load_deployment",
            version=version("orderlinedw_prefect")
        )



if __name__ == "__main__":
    main()
