#!/usr/bin/env python
import os
from subprocess import run

run(["py", "tools/build/build.py"])
print("Running Steam")
run(["C:\\Program Files (x86)\\Steam\\Steam.exe", "-applaunch", "2300"])
