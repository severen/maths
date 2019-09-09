#!/usr/bin/env python3

# This script compiles all LaTeX documents by locating their corresponding
# Makfiles.

import subprocess

from glob import iglob
from pathlib import Path

makefiles = map(Path, iglob("**/Makefile"))

for makefile in makefiles:
    subprocess.run(["make"], cwd=makefile.parent)
