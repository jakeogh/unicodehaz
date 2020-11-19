#!/usr/bin/env python3

from unicodedata import name

import click


@click.command()
@click.argument("codepoints", type=int, nargs=-1)
@click.option('--all', "all_codepoints", is_flag=True, help="Include unnamed codepoints in output")
@click.option('--null', is_flag=True, help="NULL terminalted output")
@click.option('--glyphs-only', is_flag=True, help="Do not print index numbers")
@click.option('--verbose', is_flag=True)
@click.option('--stats', is_flag=True, help="Only print statistics")
def cli(codepoints,
        all_codepoints,
        null,
        glyphs_only,
        verbose,
        stats,):

    # unicode is base 0x110000 1114112 https://wtanaka.com/node/8213
    named = not all_codepoints
    if null:
        line_end = "\0"
    else:
        line_end = '\n'

    unnamed_codepoints = []
    iterator = range(1114112)
    if codepoints:
        iterator = codepoints
    for index, point in enumerate(iterator):
        line = []
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
            line.append(str(index))
        printable = repr(thing)
        line.append(printable)

        if unicode_name and not glyphs_only:
            line.append(unicode_name)

        if not stats:
            line = ' '.join(line)
            print(line, end=line_end)

    if stats:
        print("last named unicode char:", last_name, repr(chr(last_name)), name(chr(last_name)))
        print("unnamed codepoints:", len(unnamed_codepoints))


if __name__ == "__main__":
    cli()
