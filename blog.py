#!/usr/bin/env python3

# built-in modules
import os
from pathlib import Path

# 3rd party
import click

# local modules


def make_dirs(force=False):
    cwd = Path(os.getcwd())
    os.makedirs(Path(f"{cwd}/docs/assets/templates"), exist_ok=force)
    os.makedirs(Path(f"{cwd}/docs/assets/images"), exist_ok=force)
    os.makedirs(Path(f"{cwd}/docs/posts"), exist_ok=force)


@click.command()
@click.option('--overwrite', prompt=True, default=False, type=bool)
def force_dir(overwrite):
    if overwrite==True:
        click.echo(f"Welcome to Newblogton!")
        make_dirs(force=True)
    else:
        click.echo(f"Hi-Yo, Silver! Away!")


def newblogton():
    try:
        make_dirs()
    except  FileExistsError:
        print("Directories exist! Would you like reset PonyExpress? If so enter: True")
        force_dir()


    # make dirs:
        # docs
            # assets
                # images
                # templates
            # posts
    # /docs/assets/tempaltes
        # Build index header and footer
        # Build post header and footer

if __name__=='__main__':
    newblogton()
