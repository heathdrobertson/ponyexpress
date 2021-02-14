#!/usr/bin/env python3
import click

from datetime import datetime
from pytz import timezone

# Run PonyExpress
# Creates a post in posts and appends the link to the index.md file.

title = now.strftime('**%a %H:%M** [*%d-%m-%Y*]')

@click.command()
@click.option('--title', default=title, help="Enter a post title")

def main():
    now = datetime.now(tz=timezone('America/Denver'))
    file_name = now.strftime('%m-%d-%Y-%H-%M')

    print("Now:")
    print(now)
    print("File Name:")
    print(file_name)
    print("Title:")
    print(title)


#    post = open(f'{file_name}.md', 'w')
#    post.write(f'### {title}\n')
#    post.write(f'__Description__\n\n\n---')


if __name__ == '__main__':
    main()
