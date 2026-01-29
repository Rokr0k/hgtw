#!/usr/bin/env python3

import os


def remove(path: str) -> None:
    if os.path.exists(path):
        os.remove(path)


remove("HGTW.ttf")
remove("HGTW.otf")
remove("HGTW.woff2")
