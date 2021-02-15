#!/usr/bin/env python3

# https://click.palletsprojects.com/en/7.x/

import click
import os

from pathlib import Path
from datetime import datetime
from pytz import timezone

# Run PonyExpress
# Creates a post in posts and appends the link to the index.md file.


now = datetime.now(tz=timezone(f'America/Denver'))
default_title = now.strftime(f"New-Post-[%a-%H:%M::%d-%m-%Y]")
cwd = Path(os.getcwd())
posts_dir = Path(f"{cwd}/docs/posts")


header = open(f"{cwd}/docs/assets/templates/header.md", 'r')
body = open(f"{cwd}/docs/assets/templates/body.md", 'a')
footer = open(f"{cwd}/docs/assets/templates/footer.md", 'r')

index = open(f"{cwd}/docs/index.md", 'w')
index.write(f"{header.read()}")
index.write(f"{footer.read()}")


@click.command()
@click.option('--title', default=default_title, help='Enter post title text.')
def post(title):

    post_dir_name = f"{title.replace(' ', '-')}"
    os.makedirs(f"{posts_dir}/{post_dir_name}/images")
    post_file = f"{posts_dir}/{post_dir_name}/{title.replace(' ', '-')}.md"

    post = open(f"{post_file}", 'a')
    post.write(f"{header.read()}")
    post.write(f"## {title}\n")
    post.write(f"__Description__\n\n\n---")
    post.write(f"{footer.read()}")


if __name__ == '__main__':
    post()
