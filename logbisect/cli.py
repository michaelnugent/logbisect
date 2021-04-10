#!/usr/bin/env python3

import io
from datetime import datetime

import click

from .logbisect import bisect


@click.command()
@click.option("-f", "--filename", required=True, help="file to operate on")
@click.option(
    "-r",
    "--regex",
    required=True,
    help="regex to describe how to find the date in a log line",
)
@click.option(
    "-t",
    "--timestamp",
    required=True,
    type=click.DateTime(formats=["%Y-%m-%d %H:%M:%S"]),
    help="timestamp to find",
)
@click.option(
    "-n", "--number", default=10, type=int, help="number of lines to print (0=to EOF)"
)
@click.option(
    "-p",
    "--pos",
    default=False,
    is_flag=True,
    help="print out position, but not data, and exit",
)
def begin(
    filename: str,
    regex: str,
    timestamp: datetime,
    number: int,
    pos: bool,
) -> None:
    with open(filename, "r") as f:
        f.seek(0, io.SEEK_END)
        endpos = f.tell()
        f.seek(0, io.SEEK_SET)
        position = bisect(f, regex, timestamp)

        if pos:
            print(position)
            return

        i = 0
        while True:
            print(f.readline().strip())
            if number > 0:
                i += 1
                if i >= number:
                    break
            if f.tell() == endpos:
                break


if __name__ == "__main__":
    begin()  # pylint: disable=E1120
