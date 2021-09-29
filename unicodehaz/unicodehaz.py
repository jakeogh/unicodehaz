#!/usr/bin/env python3

import sys
import unicodedata

import click


@click.command()
@click.argument("codepoints", type=str, nargs=-1,)
@click.option('--all', "all_codepoints",
              is_flag=True,
              help="Include unnamed codepoints in output",)
@click.option('--null', is_flag=True, help="NULL terminalted output")
@click.option('--glyphs-only', is_flag=True, help="Do not print index numbers")
@click.option('--stats', is_flag=True, help="Only print statistics")
@click.option('--start', type=int)
@click.option('--stop', type=int)
@click.option('--utf8', is_flag=True, help="codepoints are utf8 instead of int")
@click.option('--verbose', is_flag=True)
def cli(codepoints: tuple[str, ...],
        all_codepoints: bool,
        null: bool,
        glyphs_only: bool,
        stats: bool,
        start: int,
        stop: int,
        utf8: bool,
        verbose: bool,
        ):

    # unicode is base 0x110000 1114112 https://wtanaka.com/node/8213
    named = not all_codepoints
    if null:
        line_end = "\0"
    else:
        line_end = '\n'

    unnamed_codepoints = []
    assert len(codepoints) == 1

    if not codepoints:
        iterator = range(1114112)
    else:
        iterator = codepoints
    for index, point in enumerate(iterator):
        if verbose:
            print(index, point, file=sys.stderr)
        if utf8:
            point = ord(point)
        else:
            point = int(point)
        if start:
            if point < start:
                continue
        if stop:
            if point > stop:
                continue
        line = []
        thing = chr(point)
        try:
            unicode_name = unicodedata.name(thing)
            last_name = index
        except ValueError:
            unicode_name = None
            unnamed_codepoints.append(thing)

        if named:
            if not unicode_name:
                continue
        if not glyphs_only:
            #line.append(str(index))
            line.append(str(point))
        printable = repr(thing)
        line.append(printable)

        if unicode_name and not glyphs_only:
            line.append(unicode_name)

        if not stats:
            line = ' '.join(line)
            print(line, end=line_end)

    if stats:
        print("Last named codepoint:",
              last_name,
              repr(chr(last_name)),
              unicodedata.name(chr(last_name)))
        print("Unnamed codepoints:  ", len(unnamed_codepoints))
        print()
        print(unicodedata.__doc__)
