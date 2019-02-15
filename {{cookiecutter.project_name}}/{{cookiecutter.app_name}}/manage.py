import click
from flask.cli import FlaskGroup

from {{cookiecutter.app_name}}.app import create_app


def create_{{cookiecutter.app_name}}(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_{{cookiecutter.app_name}})
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """
    Init application, create database tables
    """
    from {{cookiecutter.app_name}}.extensions import db
    click.echo("create database")
    db.create_all()
    click.echo("done")


if __name__ == "__main__":
    cli()
