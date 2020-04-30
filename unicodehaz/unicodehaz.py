#!/usr/bin/env python3

import click
from unicodedata import name


@click.command()
@click.option('--verbose', is_flag=True)
@click.option('--named', is_flag=True)
def cli(named, verbose):
    # unicode is base 0x110000 1114112 https://wtanaka.com/node/8213
    for index, point in enumerate(range(1114112)):
        thing = chr(point)
        try:
            unicode_name = name(thing)
            last_name = index
        except ValueError:
            unicode_name = None

        if named:
            if not unicode_name:
                continue

        print(index, end=" ")
        printable = repr(thing)
        print(printable, end=" ")
        if unicode_name:
            print(unicode_name)
        else:
            print()

    #print("last named unicode char:", last_name, repr(chr(last_name)), name(chr(last_name)))


if __name__ == "__main__":
    cli()
