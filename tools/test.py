#!/usr/bin/env python3
import os
from subprocess import run

run(["py", "tools/bobby/build.py", "Clematis", "-C", "-V3.3"])
print("Running Steam")
run(["C:\\Program Files (x86)\\Steam\\Steam.exe", "-applaunch", "2300"])
