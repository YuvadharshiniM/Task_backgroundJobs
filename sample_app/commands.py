import click
@click.command("hello")
def hello():
    click.echo("Hello, this is Yuvadharshini!")
commands = [
    hello
]