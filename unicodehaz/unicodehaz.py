#!/usr/bin/env python3

from unicodedata import name

import click


@click.command()
@click.argument("codepoints", type=int, nargs=-1)
@click.option('--named', is_flag=True)
@click.option('--null', is_flag=True)
@click.option('--glyphs-only', is_flag=True)
@click.option('--verbose', is_flag=True)
@click.option('--stats', is_flag=True)
def cli(codepoints,
        named,
        null,
        glyphs_only,
        verbose,
        stats,):
    # unicode is base 0x110000 1114112 https://wtanaka.com/node/8213
    unnamed_codepoints = []
    iterator = range(1114112)
    if codepoints:
        iterator = codepoints
    for index, point in enumerate(iterator):
        thing = chr(point)
        try:
            unicode_name = name(thing)
            last_name = index
        except ValueError:
            unicode_name = None
            unnamed_codepoints.append(thing)

        if named:
            if not unicode_name:
                continue
        if not glyphs_only:
            print(index, end=" ")
        printable = repr(thing)
        print(printable, end=" ")

        if null:
            line_end = "\0"
        else:
            line_end = '\n'

        if unicode_name and not glyphs_only:
            print(unicode_name, end=line_end)
        else:
            print(end=line_end)

    if stats:
        print("last named unicode char:", last_name, repr(chr(last_name)), name(chr(last_name)))
        print("unnamed_codepoints:", len(unnamed_codepoints))


if __name__ == "__main__":
    cli()
