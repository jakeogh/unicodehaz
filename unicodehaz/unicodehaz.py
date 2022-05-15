#!/usr/bin/env python3

import os
import sys
import unicodedata
from stat import S_ISFIFO
from typing import Union

import click
from asserttool import ic
from clicktool import click_add_options
from clicktool import click_global_options
from clicktool import tv
from mptool import output
from mptool import unmp

# def stdin_generator():
#    for line in sys.stdin:
#        for char in list(line):
#            yield char


def validate_codepoints(ctx, param, value):
    ic(value)
    for v in value:
        _v = int(v)
        if _v < 0 or _v > 1114111:
            raise click.BadParameter(
                f"unicode is base 0x110000 1114112, {value} is outside the range of valid codepoints (0 to 1114111)"
            )
    return value


@click.group(no_args_is_help=True)
@click_add_options(click_global_options)
@click.pass_context
def cli(
    ctx,
    verbose: Union[bool, int, float],
    verbose_inf: bool,
    dict_input: bool,
):

    tty, verbose = tv(
        ctx=ctx,
        verbose=verbose,
        verbose_inf=verbose_inf,
    )


@cli.command("stats")
@click_add_options(click_global_options)
@click.pass_context
def _stats(
    ctx,
    verbose: Union[bool, int, float],
    verbose_inf: bool,
    dict_input: bool,
):

    tty, verbose = tv(
        ctx=ctx,
        verbose=verbose,
        verbose_inf=verbose_inf,
    )

    unnamed_codepoints = []
    named_codepoints = []

    iterator = range(1114112)
    for index, _point in enumerate(iterator):
        if verbose:
            ic(index, _point)
        point = int(_point)
        thing = chr(point)
        try:
            unicode_name = unicodedata.name(thing)
            last_name = index
            named_codepoints.append(thing)
        except ValueError as e:
            # ic(e)
            unicode_name = None
            unnamed_codepoints.append(thing)

    print(
        "Last named codepoint:",
        last_name,
        repr(chr(last_name)),
        unicodedata.name(chr(last_name)),
    )

    print("Unnamed codepoints:  ", len(unnamed_codepoints))
    print("Named codepoints:  ", len(named_codepoints))
    print()
    print(unicodedata.__doc__)


@cli.command("codepoints")
@click.argument(
    "codepoints", nargs=-1, type=click.UNPROCESSED, callback=validate_codepoints
)
@click.option(
    "--all",
    "all_codepoints",
    is_flag=True,
    help="Include unnamed codepoints in output",
)
# @click.option("--glyphs-only", is_flag=True, help="Do not print index numbers")
@click.option("--start", type=int)
@click.option("--stop", type=int)
# @click.option('--utf8', is_flag=True, help="codepoints are utf8 instead of int")
@click_add_options(click_global_options)
@click.pass_context
def _codepoints(
    ctx,
    codepoints: tuple[str],
    all_codepoints: bool,
    glyphs_only: bool,
    start: int,
    stop: int,
    verbose: Union[bool, int, float],
    verbose_inf: bool,
    dict_input: bool,
):

    tty, verbose = tv(
        ctx=ctx,
        verbose=verbose,
        verbose_inf=verbose_inf,
    )

    # unicode is base 0x110000 1114112 https://wtanaka.com/node/8213
    named = not all_codepoints

    unnamed_codepoints = []
    if not codepoints:
        # iterator = unmp(valid_types=[int,], verbose=verbose)
        iterator = range(1114112)
    else:
        iterator = codepoints

    for index, _point in enumerate(iterator):
        if verbose:
            ic(index, _point)
        point = int(_point)
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
        except ValueError as e:
            # ic(e)
            unicode_name = None
            unnamed_codepoints.append(thing)

        if named:
            if not unicode_name:
                continue
        # if not glyphs_only:
        #    line.append(str(point))
        printable = repr(thing)
        line.append(printable)

        # if unicode_name and not glyphs_only:
        if unicode_name:
            line.append(unicode_name)

        _line = " ".join(line)
        output(
            _line,
            reason=_point,
            dict_input=dict_input,
            tty=tty,
            verbose=verbose,
        )


@cli.command()
@click.argument(
    "utf8_chars",
    type=str,
    nargs=-1,
)
@click.option("--glyphs-only", is_flag=True, help="Do not print index numbers")
@click_add_options(click_global_options)
@click.pass_context
def chars(
    ctx,
    utf8_chars: tuple[str, ...],
    glyphs_only: bool,
    verbose: Union[bool, int, float],
    verbose_inf: bool,
    dict_input: bool,
):

    tty, verbose = tv(
        ctx=ctx,
        verbose=verbose,
        verbose_inf=verbose_inf,
    )

    if utf8_chars:
        iterator = utf8_chars
    else:
        iterator = unmp(
            valid_types=[
                str,
            ],
            verbose=verbose,
        )

    for index, point in enumerate(iterator):
        try:
            unicode_name = unicodedata.name(point)
            last_name = index
        except ValueError as e:
            # ic(e)
            unicode_name = None

        # point = ord(point)
        # ic(point)
        # line = []
        # thing = chr(point)
        # ic(thing)
        # printable = repr(thing)
        output(
            (point, unicode_name),
            reason=None,
            dict_input=dict_input,
            tty=tty,
            verbose=verbose,
        )

        output(point, reason=None, dict_input=dict_input, tty=tty, verbose=verbose)
