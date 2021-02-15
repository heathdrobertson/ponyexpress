#!/usr/bin/env python3

# https://click.palletsprojects.com/en/7.x/

import click
import os

from pathlib import Path
from datetime import datetime
from pytz import timezone

# Run PonyExpress
# Creates a post in posts and appends the link to the index.md file.


now = datetime.now(tz=timezone('America/Denver'))
default_title = now.strftime('**%a %H:%M** [*%d-%m-%Y*]')
cwd = Path(os.getcwd())
posts_dir = Path(f'{cwd}/docs/posts')

index = open(f'{cwd}/docs/index.md', 'w')
header = open(f'{cwd}/template/header.md', 'r')
footer = open(f'{cwd}/template/footer.md', 'r')

@click.command()
@click.option('--title', default=default_title, help="Enter a post title")

def main(title):

    dir_name = now.strftime('%m-%d-%Y-%H-%M')
    post_dir_name = f'{dir_name}-{title}'
    os.makedirs(f'{posts_dir}/{post_dir_name}/images')
    post_file = f'{posts_dir}/{post_dir_name}/{title}.md'

    post = open(f'{post_file}', 'a')
    post.write(f'{header.read()}')
    post.write(f'## {title}\n')
    post.write(f'__Description__\n\n\n---')
    post.write(f'{footer.read()}')

    file = header.read() + footer.read()
    index.write(f'{file}')


if __name__ == '__main__':
    main()
