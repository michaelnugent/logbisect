#!/usr/bin/env python3

import itertools
import io
import logging
import re

from datetime import datetime
from dateutil.parser import parse


log = logging.getLogger(__name__)


def bisect(f: io.TextIOWrapper, regex_src: str, dtarget: datetime) -> int:
    lb = LogBisect()
    return lb.bisect(f, regex_src, dtarget)


class LogBisect:
    def __init__(self) -> None:
        self.bisect_count = 0
        self.prev_tell = 0
        self.regex = None
        self.dtarget = None

    @staticmethod
    def find_line(f: io.TextIOWrapper, target: int) -> str:
        f.seek(target, io.SEEK_SET)
        f.readline()
        line = f.readline()
        return line

    def mid_bisect(self, f: io.TextIOWrapper, start: int, end: int) -> None:
        if f.tell() == self.prev_tell:
            f.readline()
            return
        self.prev_tell = f.tell()

        self.bisect_count += 1
        mid = int((start + end) / 2)
        line = LogBisect.find_line(f, mid)
        match = self.regex.search(line)
        p = parse(match.group())
        if self.dtarget < p:
            self.mid_bisect(f, start, mid)
        elif self.dtarget > p:
            self.mid_bisect(f, mid, end)

    @staticmethod
    def validate_min_lines(f: io.TextIOWrapper, lines: int) -> bool:
        saved_pos = f.tell()
        f.seek(0, io.SEEK_END)
        end = f.tell()
        f.seek(0, io.SEEK_SET)

        for _ in itertools.repeat(None, lines):
            line = f.readline()
            if not line and f.tell() >= end:
                f.seek(saved_pos, io.SEEK_SET)
                return False

        f.seek(saved_pos, io.SEEK_SET)
        return True

    @staticmethod
    def readback(f: io.TextIOWrapper) -> None:
        pos = f.tell()
        while pos >= 0:
            f.seek(pos)
            if f.read(1) == "\n":
                break
            pos -= 2

    def searchback(self, f: io.TextIOWrapper, dtarget: datetime):
        linetime = dtarget
        while linetime == dtarget:
            LogBisect.readback(f)
            saved = f.tell()
            match = self.regex.search(f.readline())
            linetime = parse(match.group())
            f.seek(saved, io.SEEK_SET)

    def bisect(self, f: io.TextIOWrapper, regex_src: str, dtarget: datetime) -> int:
        self.regex = re.compile(regex_src)
        self.dtarget = dtarget
        start = 0
        f.seek(0, io.SEEK_END)
        end = f.tell()
        self.mid_bisect(f, start, end)
        self.searchback(f, dtarget)
        return f.tell()
