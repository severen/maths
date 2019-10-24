#!/usr/bin/env python3

# Compile all LaTeX documents by locating the corresponding Makfiles.

import subprocess

from glob import iglob
from pathlib import Path

makefiles = map(Path, iglob("**/Makefile"))

for makefile in makefiles:
    subprocess.run(["make"], cwd=makefile.parent)
