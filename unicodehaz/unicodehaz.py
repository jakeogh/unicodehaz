#!/usr/bin/env python3

import os
import sys
import unicodedata
from stat import S_ISFIFO
from typing import Union

import click
from clicktool import click_add_options
from clicktool import click_global_options
from clicktool import tv
from mptool import output
from mptool import unmp


def stdin_generator():
    for line in sys.stdin:
        for char in list(line):
            yield char


@click.group(no_args_is_help=True)
@click_add_options(click_global_options)
@click.pass_context
def cli(ctx,
        verbose: Union[bool, int, float],
        verbose_inf: bool,
        ):

    tty, verbose = tv(ctx=ctx,
                      verbose=verbose,
                      verbose_inf=verbose_inf,
                      )


@cli.command('codepoints')
@click.argument("codepoints", type=int, nargs=-1,)  # todo int
@click.option('--all', "all_codepoints",
              is_flag=True,
              help="Include unnamed codepoints in output",)
@click.option('--glyphs-only', is_flag=True, help="Do not print index numbers")
@click.option('--stats', is_flag=True, help="Only print statistics")
@click.option('--start', type=int)
@click.option('--stop', type=int)
#@click.option('--utf8', is_flag=True, help="codepoints are utf8 instead of int")
@click.option('--verbose', is_flag=True)
@click.pass_context
def points(ctx,
           codepoints: tuple[str, ...],
           all_codepoints: bool,
           glyphs_only: bool,
           stats: bool,
           start: int,
           stop: int,
           verbose: Union[bool, int, float],
           verbose_inf: bool,
           ):

    tty, verbose = tv(ctx=ctx,
                      verbose=verbose,
                      verbose_inf=verbose_inf,
                      )

    # unicode is base 0x110000 1114112 https://wtanaka.com/node/8213
    named = not all_codepoints

    unnamed_codepoints = []
    if not codepoints:
        stdin_is_a_fifo = S_ISFIFO(os.fstat(sys.stdin.fileno()).st_mode)
        if stdin_is_a_fifo:
            iterator = stdin_generator()
        else:
            iterator = range(1114112)
    else:
        iterator = [c for c in ''.join(codepoints)]
    for index, point in enumerate(iterator):
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
            line.append(str(point))
        printable = repr(thing)
        line.append(printable)

        if unicode_name and not glyphs_only:
            line.append(unicode_name)

        if not stats:
            line = ' '.join(line)
            output(line, tty=tty, verbose=verbose,)

    if stats:
        print("Last named codepoint:",
              last_name,
              repr(chr(last_name)),
              unicodedata.name(chr(last_name)))
        print("Unnamed codepoints:  ", len(unnamed_codepoints))
        print()
        print(unicodedata.__doc__)


@cli.command()
@click.argument("utf8_chars", type=str, nargs=-1,)
@click.option('--glyphs-only', is_flag=True, help="Do not print index numbers")
@click.option('--stats', is_flag=True, help="Only print statistics")
@click.option('--start', type=int)
@click.option('--stop', type=int)
@click.option('--utf8', is_flag=True, help="codepoints are utf8 instead of int")
@click.option('--verbose', is_flag=True)
@click.pass_context
def chars(ctx,
          utf8_chars: tuple[str, ...],
          all_codepoints: bool,
          glyphs_only: bool,
          stats: bool,
          start: int,
          stop: int,
          verbose: Union[bool, int, float],
          verbose_inf: bool,
          ):

    tty, verbose = tv(ctx=ctx,
                      verbose=verbose,
                      verbose_inf=verbose_inf,
                      )

    # unicode is base 0x110000 1114112 https://wtanaka.com/node/8213
    named = not all_codepoints
    if utf8_chars:
        iterator = utf8_chars
    else:
        iterator = unmp(valid_types=[str,], verbose=verbose)

    unnamed_codepoints = []
    for index, point in enumerate(iterator):
        point = ord(point)
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
            line.append(str(point))
        printable = repr(thing)
        line.append(printable)

        if unicode_name and not glyphs_only:
            line.append(unicode_name)

        if not stats:
            line = ' '.join(line)
            output(line, tty=tty, verbose=verbose)
